import os
import subprocess
print("welcome to the world of python codin")
print("I want to be hero in python")
p1 = subprocess.check_output(["python","--version"],text=True)
ls_process = subprocess.Popen(["ls"])
print(p1)
print(ls_process)