from pathlib import Path
import os

print(Path.cwd())  # cwd = Current Working Directory

os.chdir("C:\\Windows\\System32")
print(Path.cwd())