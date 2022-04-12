from http.client import NOT_FOUND
from typing import Any
from datetime import datetime

def Response(success: bool = True, payload: Any = None, error: Any = None) -> dict:
    '''
    Returns a dict formated response

    - Default values:
        - success: bool = True
        - payload: Any = None
        - error: Any = None
    '''
    return {
        'success': success,
        'payload': payload,
        'error': error,
    }

def Error(code: int = NOT_FOUND, description: Any = None) -> dict:
    '''
        Returns a dict with error info
    - Default values:
        - code: bool = NOT_FOUND (500)
        - description: Any = None
    '''
    return {
        'code': code,
        'description': description
    }
