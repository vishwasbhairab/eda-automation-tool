import streamlit as st
import pandas as pd
import os
import sys
import tempfile
from pathlib import Path

# Add the project root to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the EDA tools
from eda_tools.sweetviz_report import generate_sweetviz_report
from eda_tools.pandas_profile import generate_pandas_profile
from eda_tools.dtale_viewer import launch_dtale

st.set_page_config(
    page_title="EDA Automation Tool",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    st.title("📊 EDA Automation Tool")
    st.markdown("""
    Upload your dataset and generate comprehensive exploratory data analysis reports with a single click.
    Choose from multiple popular EDA libraries including Sweetviz, Pandas Profiling, and DTale.
    """)
    
    # File uploader
    uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx", "xls"])
    
    if uploaded_file is not None:
        try:
            # Determine file type and read accordingly
            file_extension = uploaded_file.name.split(".")[-1]
            
            if file_extension.lower() == "csv":
                df = pd.read_csv(uploaded_file)
            elif file_extension.lower() in ["xlsx", "xls"]:
                df = pd.read_excel(uploaded_file)
            
            # Display basic info about the dataset
            st.subheader("Dataset Overview")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Rows", df.shape[0])
            with col2:
                st.metric("Columns", df.shape[1])
            with col3:
                memory_usage = df.memory_usage(deep=True).sum()
                st.metric("Memory Usage", f"{memory_usage / 1048576:.2f} MB")
            
            # Show a sample of the data
            st.subheader("Data Sample")
            st.dataframe(df.head(10))
            
            # Sidebar for EDA tool selection
            st.sidebar.header("EDA Tools")
            eda_tool = st.sidebar.radio(
                "Select EDA Tool",
                ["Sweetviz", "Pandas Profiling (ydata-profiling)", "DTale"]
            )
            
            # Set up a temp directory for saving reports
            temp_dir = tempfile.mkdtemp()
            
            # Tool-specific options and report generation
            if eda_tool == "Sweetviz":
                st.subheader("Sweetviz Report Options")
                
                # Sweetviz specific options
                target_column = st.selectbox(
                    "Select target column (optional)",
                    ["None"] + list(df.columns),
                )
                
                compare_file = st.file_uploader(
                    "Upload a comparison dataset (optional)", 
                    type=["csv", "xlsx", "xls"]
                )
                
                compare_df = None
                if compare_file is not None:
                    file_ext = compare_file.name.split(".")[-1]
                    if file_ext.lower() == "csv":
                        compare_df = pd.read_csv(compare_file)
                    elif file_ext.lower() in ["xlsx", "xls"]:
                        compare_df = pd.read_excel(compare_file)
                    
                    st.write("Comparison dataset loaded:")
                    st.dataframe(compare_df.head(5))
                
                if st.button("Generate Sweetviz Report"):
                    with st.spinner("Generating Sweetviz Report..."):
                        target = None if target_column == "None" else target_column
                        report_path = generate_sweetviz_report(
                            df, 
                            target_column=target, 
                            compare_df=compare_df,
                            output_dir=temp_dir
                        )
                        
                        # Display the report in an iframe
                        st.subheader("Sweetviz Report")
                        report_html = open(report_path, 'r', encoding='utf-8').read()
                        st.components.v1.html(report_html, height=600, scrolling=True)
                        
                        # Download button for the report
                        with open(report_path, "rb") as file:
                            st.download_button(
                                label="Download Sweetviz Report",
                                data=file,
                                file_name="sweetviz_report.html",
                                mime="text/html"
                            )
            
            elif eda_tool == "Pandas Profiling (ydata-profiling)":
                st.subheader("Pandas Profiling Options")
                
                # Pandas Profiling specific options
                minimal_mode = st.checkbox("Minimal mode (faster)", value=False)
                
                if st.button("Generate Pandas Profile"):
                    with st.spinner("Generating Pandas Profile... This may take a while for large datasets."):
                        report_path = generate_pandas_profile(
                            df, 
                            minimal=minimal_mode,
                            output_dir=temp_dir
                        )
                        
                        # Display the report in an iframe
                        st.subheader("Pandas Profile Report")
                        report_html = open(report_path, 'r', encoding='utf-8').read()
                        st.components.v1.html(report_html, height=600, scrolling=True)
                        
                        # Download button for the report
                        with open(report_path, "rb") as file:
                            st.download_button(
                                label="Download Pandas Profile Report",
                                data=file,
                                file_name="pandas_profile_report.html",
                                mime="text/html"
                            )
            
            else:  # DTale
                st.subheader("DTale Interactive Viewer")
                st.warning("DTale will launch in a new browser tab. Close it when you're done.")
                
                if st.button("Launch DTale Viewer"):
                    with st.spinner("Launching DTale..."):
                        dtale_url = launch_dtale(df)
                        st.markdown(f"DTale is running at: [{dtale_url}]({dtale_url})")
                        st.markdown("Click the link above to open DTale in a new tab.")
                        
                        # Launch in iframe (may not work in all environments)
                        try:
                            st.components.v1.iframe(dtale_url, height=600, scrolling=True)
                        except Exception as e:
                            st.error(f"Could not embed DTale: {str(e)}")
                            st.info("Please use the link above to access DTale.")
        
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Please make sure your file is in the correct format.")

if __name__ == "__main__":
    main()