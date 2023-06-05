import pytest
import sys
import os
print(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(rf"{os.path.abspath(os.path.dirname(os.getcwd()))}/FinalExam_2023")
from lib.PPM.PPM import PPM
if __name__ == "__main__":
    pytest.main([f"{os.path.abspath(os.path.dirname(os.getcwd()))}/FinalExam_2023/test/Test_PPM.py"])
    pytest.main([f"{os.path.abspath(os.path.dirname(os.getcwd()))}/FinalExam_2023/test/Test_PPMWindow.py"])