# EDA Automation Tool

A comprehensive Streamlit-based application for automating Exploratory Data Analysis (EDA). This tool integrates multiple popular EDA libraries including Sweetviz, Pandas Profiling (ydata-profiling), and DTale to provide robust data insights with minimal effort.

![EDA Automation Tool](https://eda-automation-tool.streamlit.app/)

## Features

- **Data Upload & Preview**
  - Support for CSV and Excel files
  - Automatic data type detection and parsing
  - Quick dataset overview with key metrics
  
- **Multiple EDA Tools Integration**
  - **Sweetviz**: Generate visual EDA reports with target analysis and comparison capabilities
  - **Pandas Profiling**: Generate detailed statistical analysis reports with interactive visualizations
  - **DTale**: Explore data interactively with powerful visualization capabilities
  
- **Report Management**
  - View reports inline within the application
  - Export reports in HTML format for sharing or offline viewing
  - Compare datasets for before/after analysis
  
- **Advanced Options**
  - Target variable selection for supervised learning analysis
  - Comparison dataset upload for comparative analysis
  - Configurable report generation settings

## Screenshots

![Data Upload](https://via.placeholder.com/400x250?text=Data+Upload)
![Sweetviz Report](https://via.placeholder.com/400x250?text=Sweetviz+Report)
![Pandas Profiling](https://via.placeholder.com/400x250?text=Pandas+Profiling)
![DTale Explorer](https://via.placeholder.com/400x250?text=DTale+Explorer)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/eda-automation-tool.git
cd eda-automation-tool
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```


## Usage

1. Launch the application :
```bash
streamlit run streamlit_app.py
```

3. Navigate to the URL provided in your terminal (typically http://localhost:8501)

4. Upload your dataset (CSV or Excel format)

5. Choose your preferred EDA tool from the sidebar:
   - Sweetviz for quick visual reports
   - Pandas Profiling for comprehensive statistical analysis
   - DTale for interactive exploration

6. Configure tool-specific options if needed

7. Generate and view your EDA report

8. Download the report for offline use or sharing

## Project Structure

```
├── streamlit_app.py                     # Main Streamlit application
├── requirements.txt           # Project dependencies
├── eda_tools/                 # EDA integration modules
│   ├── __init__.py
│   ├── sweetviz_report.py     # Sweetviz integration
│   ├── pandas_profile.py      # Pandas Profiling integration
│   ├── dtale_viewer.py        # DTale integration
```
9. Streamlit based application link: https://eda-automation-tool.streamlit.app/
## Dependencies

- **Core**:
  - Python 3.8+
  - Streamlit 1.22.0
  - Pandas 1.5.3
  - NumPy 1.23.5
  
- **EDA Libraries**:
  - Sweetviz 2.1.3
  - ydata-profiling 4.5.1
  - DTale 2.14.1
  
- **Additional**:
  - OpenPyXL 3.1.2 (Excel support)
  - Matplotlib 3.7.2
  - Seaborn 0.12.2

## Troubleshooting

### Common Issues and Solutions

#### Blank Streamlit Page
- Check if Streamlit is properly installed
- Ensure Python path is correctly set
- Try using one of the provided launcher scripts

#### NumPy VisibleDeprecationWarning Error
- Run the patch_sweetviz.py script
- Ensure NumPy version 1.23.5 is installed
- Use the provided launcher scripts which include automatic patching

#### Report Generation Errors
- Ensure all dependencies are correctly installed
- Check if your dataset is properly formatted
- For large datasets, try using the "minimal" option in Pandas Profiling

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/vishwasbhairab/eda-automation-tool/issues).

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the web application framework
- [Sweetviz](https://github.com/fbdesignpro/sweetviz) for automated EDA visualization
- [ydata-profiling](https://github.com/ydataai/ydata-profiling) for comprehensive profiling reports
- [DTale](https://github.com/man-group/dtale) for interactive data exploration
