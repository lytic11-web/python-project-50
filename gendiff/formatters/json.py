"""JSON formatter for diff output."""

import json


def format_json(diff):
    """
    Format diff tree to JSON string.
    
    Args:
        diff: diff tree
        
    Returns:
        JSON string with indentation
    """
    return json.dumps(diff, indent=2, ensure_ascii=False)
