"""
This module provides integration with ydata-profiling (formerly pandas-profiling) for EDA.
"""

import os
import pandas as pd
from ydata_profiling import ProfileReport
from pathlib import Path


def generate_pandas_profile(df, minimal=False, output_dir=None):
    """
    Generate a pandas profiling report from a pandas DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to analyze
    minimal : bool, optional
        If True, generates a minimal report (faster but less comprehensive)
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
        
    output_path = os.path.join(output_dir, "pandas_profile_report.html")
    
    # Configure profile settings based on minimal mode
    if minimal:
        profile = ProfileReport(
            df, 
            minimal=True,
            title="Pandas Profiling Report (Minimal Mode)"
        )
    else:
        profile = ProfileReport(
            df,
            title="Pandas Profiling Report",
            explorative=True
        )
    
    # Save the report
    profile.to_file(output_path)
    
    return output_path