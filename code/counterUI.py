import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import csv
import modelOutputInterface as mOI
import predictor
import os
from shutil import copyfile

def showUI(outputHandler):
    root= tk.Tk()
    root.state('zoomed')

    root.title("Cell Counting Application")
    root.minsize(1000, 1000)

    canvas=tk.Canvas(root, width=1000, height=1000, relief="raised")
    canvas.pack()

    titleLabel=tk.Label(root, text="Cell Counting Application!", font=("helvetica", 14))
    canvas.create_window(500, 25, window=titleLabel)

    browseLabel=tk.Label(root, text="Browse for image:", font=("helvetica", 10))
    canvas.create_window(500, 50, window=browseLabel)

    imageNameLabel=tk.Label(root, text="", font=("helvetica", 10))
    canvas.create_window(500, 125, window=imageNameLabel)

    errorLabel=tk.Label(root, text="", font=("helvetica", 10))
    canvas.create_window(500, 250, window=errorLabel)

    countLabel=tk.Label(root, text="", font=("helvetica", 10))
    canvas.create_window(500, 150, window=countLabel)

    def browseDirectory():
        dirName = filedialog.askdirectory(mustexist=True)

        # which image to process
        index = tk.IntVar(value=0)

        if (dirName):
            nextButton=tk.Button(text="Next Image", command=lambda : index.set(index.get() + 1), bg="brown", fg="white", font=("helvetica", 9, "bold"))
            canvas.create_window(500, 240, window=nextButton)

            filenames = os.listdir(dirName)
            while index.get() < len(filenames):
                filename = filenames[index.get()]
                if filename.endswith(".png") or filename.endswith(".jpg"):
                    # valid image, process it
                    print('Processing:', os.path.join(dirName, filename))
                    processImage(os.path.join(dirName, filename))
                else:
                    # skip this one, go to next
                    print('Not an image:', filename)
                    index.set(index.get() + 1)
                    continue

                # wait until nextButton is pressed
                nextButton.wait_variable(index)
            
    def processImage(filename):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            background_image=ImageTk.PhotoImage(Image.open(filename))
        else:
            imageNameLabel.config(text="")
            countLabel.config(text="")
            errorLabel.config(text="Please input a valid relative or absolute file location")
            errorLabel.lift()
            return

        errorLabel.config(text="")

        count = predictor.predict(filename)

        predictionFile = Image.open(os.path.abspath("predictions.png"))
        imageHeight, imageWidth = predictionFile.size
        areaHeight = root.winfo_height()-250
        areaWidth = root.winfo_width()
        heightRatio = areaHeight/imageHeight
        widthRatio = areaWidth/imageWidth
        ratio = min(heightRatio, widthRatio)
        newHeight = int(imageHeight*ratio)
        newWidth = int(imageWidth*ratio)
        predictionFile = predictionFile.resize((newHeight, newWidth), Image.ANTIALIAS)
        background_image=ImageTk.PhotoImage(predictionFile)

        background_label=tk.Label(root, image=background_image)
        background_label.place(x=int((areaWidth-newWidth)/2.0), y=250, height=newHeight, width=newWidth)
        root.photo = background_image
        root.grid()

        imageNameLabel.config(text="Image is: "+filename)
        imageNameLabel.lift()

        countLabel.config(text="There are "+str(count)+" cells in this image")
        countLabel.lift()

        def writeToCSV():
            filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV", "*.csv"),("All Files", "*.*")))
            if filepath is None:
                return
            with open(filepath, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["This is the information for "+str(filename)])
                writer.writerow(["Number of cells is: "+str(count)])

        downloadCSVButton=tk.Button(text="Download information about file", command=writeToCSV, bg="brown", fg="white", font=("helvetica", 9, "bold"))
        canvas.create_window(500, 180, window=downloadCSVButton)

        def downloadImage():
            filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("Image", "*.png *.jpg"),("All Files", "*.*")))
            if filepath is None:
                return
            copyfile("predictions.png", filepath)

        downloadImageButton=tk.Button(text="Download prediction image", command=downloadImage, bg="brown", fg="white", font=("helvetica", 9, "bold"))
        canvas.create_window(500, 210, window=downloadImageButton)

    def browseFilesys():
        filename = filedialog.askopenfilename()
        processImage(filename)

    browseButton=tk.Button(text="Browse", command=browseFilesys, bg="brown", fg="white", font=("helvetica", 9, "bold"))
    canvas.create_window(500, 100, window=browseButton)

    browseButton2=tk.Button(text="Browse Directory", command=browseDirectory, bg="brown", fg="white", font=("helvetica", 9, "bold"))
    canvas.create_window(600, 100, window=browseButton2)

    root.mainloop()
