import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import csv
import modelOutputInterface as mOI

def initUI():
    root = tk.Tk()
    root.title("Cell Counting Application")

    canvas1=tk.Canvas(root, width=1000, height=1000, relief="raised")
    canvas1.pack()
    
    return root, canvas1
    
def showUI(root):
    root.mainloop()


def appHeader(root, canvas1, outputHandler):
    label1=tk.Label(root, text="Cell Counting Application!")
    label1.config(font=("helvetica", 14))
    canvas1.create_window(500, 25, window=label1)

    
def showFileUploadButton(root, canvas1, outputHandler):
    label2=tk.Label(root, text="Browse for image:")
    label2.config(font=("helvetica", 10))

    canvas1.create_window(500, 50, window=label2)

    browseButton=tk.Button(text="Browse", command= lambda: (browseFilesys(root, canvas1, outputHandler)), bg="brown", fg="white", font=("helvetica", 9, "bold"))
    canvas1.create_window(500, 100, window=browseButton)
    
def browseFilesys(root, canvas1, outputHandler):
    filename = filedialog.askopenfilename()
    try:
        background_image=ImageTk.PhotoImage(Image.open(filename))
    except:
        label3=tk.Label(root, text="Please input a valid relative or absolute file location", font=("helvetica", 10))
        canvas1.create_window(500, 250, window=label3)
        return
    background_label=tk.Label(root, image=background_image)
    background_label.place(x=0, y=150, relwidth=1, relheight=1)
    root.photo = background_image
    root.grid()

    label3=tk.Label(root, text="Image is: "+filename, font=("helvetica", 10))
    canvas1.create_window(500, 125, window=label3)

    countMsg = "There are "+ str(outputHandler.getPrediction()) + " cells in this image"
    label4=tk.Label(root, text=countMsg, font=("helvetica", 10))
    canvas1.create_window(500, 150, window=label4)
    
    showCSVDownloadButton(canvas1, filename, 17, 0.4)
    

def showCSVDownloadButton(canvas1, filename, number, percent):
    downloadButton=tk.Button(text="Download information about file", command= lambda: (writeToCSV(filename, number, percent)), bg="brown", fg="white", font=("helvetica", 9, "bold"))
    canvas1.create_window(500, 200, window=downloadButton)
    
def writeToCSV(filename, number, percent):
    with open(filename+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["This is the information for "+str(filename)])
        writer.writerow(["Number of cells is: "+str(number)])
        writer.writerow(["Percent of alive cells is: "+str(percent*100)+"%"])
        writer.writerow(["This is all hardcoded"])