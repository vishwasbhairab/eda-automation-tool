"""
This module provides integration with Sweetviz library for EDA visualization.
"""

import os
import pandas as pd
import sweetviz as sv
from pathlib import Path


def generate_sweetviz_report(df, target_column=None, compare_df=None, output_dir=None):
    """
    Generate a Sweetviz EDA report from a pandas DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The main DataFrame to analyze
    target_column : str, optional
        The name of the target column for analysis
    compare_df : pandas.DataFrame, optional
        An optional second DataFrame to compare with the main DataFrame
    output_dir : str, optional
        Directory to save the output report
        
    Returns:
    --------
    str
        Path to the generated HTML report file
    """
    # Create a default output directory if none specified
    if output_dir is None:
        output_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(output_dir, exist_ok=True)
        
    output_path = os.path.join(output_dir, "sweetviz_report.html")
    
    # Generate the appropriate type of report based on inputs
    if compare_df is not None:
        # Comparative analysis
        report = sv.compare([df, "Main Dataset"], [compare_df, "Comparison Dataset"], target_column)
    elif target_column is not None:
        # Analysis with target feature
        report = sv.analyze(df, target_feat=target_column)
    else:
        # Basic analysis
        report = sv.analyze(df)
    
    # Save the report
    report.show_html(output_path, open_browser=False)
    
    return output_path