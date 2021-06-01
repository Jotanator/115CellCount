import os
import sys
import inspect
import modelOutputInterface as mOI
import TestModelOutputHandler as TMO


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


import counterUI


def modelOutputDummyTest():
    outputHandler = TMO.TestModelOutputHandler()
    counterUI.showUI(outputHandler)  #any exceptions is a failure

if __name__ == '__main__':
    modelOutputDummyTest()
