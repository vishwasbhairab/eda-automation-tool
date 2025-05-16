"""
This module provides integration with DTale for interactive data exploration.
"""

import os
import pandas as pd
import dtale
import socket
from contextlib import closing


def find_free_port():
    """Find a free port on localhost."""
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


def launch_dtale(df):
    """
    Launch DTale with the given DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to visualize
        
    Returns:
    --------
    str
        URL to access the DTale instance
    """
    # Find a free port to run DTale on
    port = find_free_port()
    
    # Launch DTale with the DataFrame
    d = dtale.show(df, subprocess=False, port=port)
    
    # Return the URL where DTale is accessible
    return f"http://localhost:{port}"