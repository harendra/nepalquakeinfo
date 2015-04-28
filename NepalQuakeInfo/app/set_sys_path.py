# -*- coding: utf-8 -*-
"""Sets sys.path for the library directories."""
import os
import sys

current_path = os.path.abspath(os.path.dirname(__file__))

# Add lib as primary libraries directory, with fallback to lib/dist
# and optionally to lib/dist.zip, loaded using zipimport.
sys.path[0:0] = [
    os.path.join(current_path,'controllers'),
    os.path.join(current_path, 'core'),
    os.path.join(current_path, 'model'),
    os.path.join(current_path,'quaketests'),
    os.path.join(current_path,'utils'),
    os.path.join(current_path,'basehandler'),
]
