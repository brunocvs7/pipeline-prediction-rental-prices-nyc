import os


def sanitize_path(s):
    """Standard path

    Args:
        s (string): path

    Returns:
        s: path corrected
    """
    return os.path.abspath(os.path.expanduser(os.path.expandvars(s)))
