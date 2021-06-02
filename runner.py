import os
import sys
import inspect


# Get the code directory of the project for importing UI
ROOT_DIR = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.join(ROOT_DIR, "code"))


import counterUI


# Run UI
if __name__ == '__main__':
    counterUI.showUI(None)
