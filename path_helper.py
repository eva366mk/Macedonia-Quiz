"""Path helper for Streamlit app - handles both local and Streamlit Cloud"""
import os

def get_data_path(filename):
    """Get the correct path for data files regardless of environment"""
    # Get the app root directory
    app_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(app_root, "data", filename)
    return data_path
