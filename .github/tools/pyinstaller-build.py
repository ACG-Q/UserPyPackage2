# -*- coding: utf-8 -*-
import os
import subprocess
import sys

def find_files(directory, extension):
    """
    Find files with a given extension in a directory.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                return os.path.join(root, file)
    return None

def build_with_pyinstaller(spec_file):
    """
    Build a project using PyInstaller.
    """
    subprocess.check_call(['pyinstaller', spec_file])

def run(project_directory):
    spec_file = find_files(project_directory, '.spec')

    if spec_file:
        print(f"Found .spec file: {spec_file}, building with PyInstaller...")
        build_with_pyinstaller(spec_file)
    else:
        print("No available .spec found.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pyinstaller-build.py <project_directory>")
        sys.exit(1)
    
    project_directory = sys.argv[1]
    run(project_directory)
