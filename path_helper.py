"""Path helper for Streamlit app - handles both local and Streamlit Cloud"""
import os

def get_data_path(filename):
    """Get the correct path for data files regardless of environment.

    ``path_helper`` lives in the project root (the same folder as
    ``Home.py``).  Previously I was taking ``dirname(dirname(file))``
    which accidentally walked up one extra level, resulting in paths
    like ``C:\\Users\\esklehrer\\Documents\\data\\questions.json``
    instead of ``C:\\Users\\esklehrer\\Documents\\Quiz master\\data\\...``.

    By using ``dirname(__file__)`` only we remain in the project root
    and the returned path is correct both locally and on Streamlit
    Cloud.
    """
    app_root = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(app_root, "data", filename)
