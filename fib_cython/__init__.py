import pyximport
import sys
import os


pyximport.install()

os.chdir(os.path.dirname(__file__))
sys.path.append(os.getcwd())

import fibonacci
