import os
import sys

arg1 = sys.argv[1]

if arg1=="list":
    os.system("svn ls https://github.com/Uncoded-AI/Object-Detection-Models/trunk/YoloV4/weights/")
