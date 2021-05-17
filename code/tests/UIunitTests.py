import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


import modelOutputInterface as mOI
import tests.TestModelOutputHandler as TMO
import counterUI

def modelOutputDummyTest():
    outputHandler = TMO.TestModelOutputHandler()
    root, canvas = counterUI.initUI()
    counterUI.appHeader(root, canvas, outputHandler)  #any exceptions is a failure
    counterUI.showFileUploadButton(root, canvas, outputHandler)
    counterUI.showUI(root)
    

if __name__ == '__main__':
    modelOutputDummyTest()
