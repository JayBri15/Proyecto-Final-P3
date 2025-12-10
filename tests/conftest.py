# Root conftest to add paths
import sys
import os

# Add tests/automation to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'automation'))
