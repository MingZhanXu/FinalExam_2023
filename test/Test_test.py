import pytest
import sys
import os
print(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(rf"{os.path.abspath(os.path.dirname(os.getcwd()))}/FinalExam_2023")
from lib.PPM.PPM import PPM