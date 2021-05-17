import tkinter as tk

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


import modelOutputInterface as mOI
import tests.TestModelOutputHandler as TMO
import counterUI

def minimalUITest():
    root, canvas = counterUI.initUI()
    counterUI.showUI(root)
    
def customElementUITest():
    root, canvas = counterUI.initUI()
    counterUI.appHeader(root, canvas)
    
    label=tk.Label(root, text="Example Label")
    label.config(font=("helvetica", 14))
    canvas.create_window(500, 55, window=label)
    
    fakeButton=tk.Button(text="Dummy Button", command= None, bg="brown", fg="white", font=("helvetica", 9, "bold"))
    canvas.create_window(500, 100, window=fakeButton)
    
    counterUI.showUI(root)

def modelOutputDummyTest():
    outputHandler = TMO.TestModelOutputHandler()
    root, canvas = counterUI.initUI()
    counterUI.appHeader(root, canvas)  #any exceptions is a failure
    counterUI.showFileUploadButton(root, canvas, outputHandler)
    counterUI.showUI(root)
    

if __name__ == '__main__':
    minimalUITest()
    customElementUITest()
    modelOutputDummyTest()
