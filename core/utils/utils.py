import sys
import re

from datetime import datetime

def logstd(msg):
    print(str(datetime.now()) + " - " + msg)
    sys.stdout.flush()

def list_remove_nones(list: list) -> list:
    ''' Removes None values from a list '''
    new_list = [i for i in list if i]
    return new_list

def is_alphanum(value: str):
    if re.search(r'[^A-z0-9]', value) or not value:
        return False
    return True