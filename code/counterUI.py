import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import csv
import predictor
import os
import inspect
from shutil import copyfile


def showUI(outputHandler):
    # Initialize root
    root = tk.Tk()
    # Window is fullscreen by default
    root.state('zoomed')
    # Window title
    root.title("Cell Counting Application")
    # Window minimum size
    root.minsize(1000, 1000)
    # Create canvas
    canvas = tk.Canvas(root, width=1000, height=1000, relief="raised")
    canvas.pack()
    # Label for the title at the top of the canvas
    titleLabel = tk.Label(
        root,
        text="Cell Counting Application!",
        font=("helvetica", 14))
    canvas.create_window(500, 25, window=titleLabel)
    # Label for the browse message at the top of the canvas
    browseLabel = tk.Label(
        root,
        text="Browse for image:",
        font=("helvetica", 10))
    canvas.create_window(500, 50, window=browseLabel)
    # Label for the name of the image the user inputs
    imageNameLabel = tk.Label(root, text="", font=("helvetica", 10))
    canvas.create_window(500, 125, window=imageNameLabel)
    # Label for the error message
    errorLabel = tk.Label(root, text="", font=("helvetica", 10))
    canvas.create_window(350, 100, window=errorLabel)
    # Label for displaying the cell count
    countLabel = tk.Label(root, text="", font=("helvetica", 10))
    canvas.create_window(500, 150, window=countLabel)


    # Function to determine if a file is an image
    def isImage(filename):
        return (filename.endswith(".png") or filename.endswith(".jpg"))


    # Function if the user wants to open a directory for sequential
    # predictions on images
    def browseDirectory():
        # Open directory browser
        dirName = filedialog.askdirectory(mustexist=True)
        # Current image
        index = tk.IntVar(value=0)


        # Function to update index
        def nextIndex():
            index.set(index.get() + 1)


        # Check that the directory is valid and that the user didn't cancel
        # the opening of the directory
        if dirName:
            # Button to go to the next image
            nextButton = tk.Button(
                text="Next Image",
                command=nextIndex,
                bg="yellow",
                fg="black",
                font=("helvetica", 9, "bold"))
            # Get the filenames
            filenames = os.listdir(dirName)


            # Function to allow the directory to loop around to index 0
            def indexLoop():
                # Set index to 0 since we are at the beginning of the
                # directory
                index.set(0)    
                # Flag to check if we need to exit if there are 0 images
                # but more than 0 nonimages
                anyImages = False
                # Loop to go through the directory
                while index.get() < len(filenames):
                    # Get current filename
                    filename = filenames[index.get()]
                    # If the file is an image
                    if isImage(filename):
                        # Display next button
                        canvas.create_window(500, 240, window=nextButton)
                        # Process valid image
                        processImage(os.path.join(dirName, filename))
                        anyImages = True
                    else:
                        # Skip invalid image
                        nextIndex()
                        continue
                    # Wait until nextButton is pressed
                    nextButton.wait_variable(index)
                # Wrap around to the beginning of the directory if we need to
                if anyImages:
                    indexLoop()
            # Initiate the loop


            indexLoop()


    # Function to run predictions on an inputted image filename
    def processImage(filename):
        if not filename:
            return
        # If the file is not an image
        if not isImage(filename):
            # Display error label and bring it to the front
            errorLabel.config(text="Please input a valid image")
            errorLabel.lift()
            # Exit the function
            return
        # If we are here, the file was valid
        # Delete contents of error label
        errorLabel.config(text="")
        # Run prediction on the file and get the count
        count = predictor.predict(filename)
        # Open the new file created by the predictions
        VAL_DIR = os.path.join(os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe()))), "../val")
        predictionFile = Image.open(os.path.join(VAL_DIR, "predictions.png"))


        # Function to resize image to maximally fit inside the current window
        def resizeImage(filename):
            # Get the dimensions of the image
            imageHeight, imageWidth = filename.size
            # Get the dimensions of the current space for the image inside the
            # window
            areaHeight = root.winfo_height() - 250
            areaWidth = root.winfo_width()
            # Determine the ratios between the dimensions of the current space
            # in the window and the image
            heightRatio = areaHeight / imageHeight
            widthRatio = areaWidth / imageWidth
            # Get the smaller of the two ratios
            ratio = min(heightRatio, widthRatio)
            # Multiply the dimensions of the image by the ratio to find the
            # maximum dimensions that fit within the current space in the
            # window
            newHeight = int(imageHeight * ratio)
            newWidth = int(imageWidth * ratio)
            # Apply the resizing to the image
            filename = filename.resize((newHeight, newWidth), Image.ANTIALIAS)
            # Return the new image
            return filename, areaWidth, newHeight, newWidth


        # Resize the image to maximally fit inside the current window
        predictionFile, windowWidth, imageHeight, imageWidth = resizeImage(
            predictionFile)
        # Open the image to put it on the canvas
        background_image = ImageTk.PhotoImage(predictionFile)
        # Label to place the image on the canvas
        background_label = tk.Label(root, image=background_image)
        # Place the image
        background_label.place(
            x=int((windowWidth - imageWidth) / 2.0),
            y=250,
            height=imageHeight,
            width=imageWidth)
        root.photo = background_image
        root.grid()
        # Update image name label to the name of the image
        imageNameLabel.config(text="Image is: " + filename)
        imageNameLabel.lift()
        # Update count label to display the cell count
        countLabel.config(
            text="There are " + str(count) + " cells in this image")
        countLabel.lift()


        # Function to download information to a CSV file
        def downloadCSV():
            # Ask user for a download location
            filepath = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
            # Return if user cancelled the download
            if not filepath:
                return
            # If we are here, the user didn't cancel the download
            # Open the new file
            with open(filepath, 'w', newline='') as file:
                # Start a CSV writer to the file
                writer = csv.writer(file)
                # Write the information to the CSV
                writer.writerow(
                    ["This is the information for " + str(filename)])
                writer.writerow(["Number of cells is: " + str(count)])


        # Button to download information to a CSV
        downloadCSVButton = tk.Button(
            text="Download information about file",
            command=downloadCSV,
            bg="yellow",
            fg="black",
            font=("helvetica", 9, "bold"))
        canvas.create_window(500, 180, window=downloadCSVButton)


        # Function to download prediction image
        def downloadPredictionImage():
            # Ask user for a download location
            filepath = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=(
                    ("PNG Image", "*.png"), ("JPG Image", "*.jpg"),
                    ("All Files", "*.*")))
            # Return if user cancelled the download
            if not filepath:
                return
            # If we are here, the user didn't cancel the download
            # Copy the contents of the prediction image to the new file
            VAL_DIR = os.path.join(os.path.dirname(
                os.path.abspath(inspect.getfile(inspect.currentframe()))), "../val")
            copyfile(os.path.join(VAL_DIR, "predictions.png"), filepath)


        # Button to download prediction image
        downloadImageButton = tk.Button(
            text="Download prediction image",
            command=downloadPredictionImage,
            bg="yellow",
            fg="black",
            font=("helvetica", 9, "bold"))
        canvas.create_window(500, 210, window=downloadImageButton)


    # Function for user to open a specific image
    def browseFilesys():
        # Open file browser
        filename = filedialog.askopenfilename()
        # Predict on the image
        processImage(filename)


    # Button for user to browse for a specific image
    browseFilesysButton = tk.Button(
        text="Browse",
        command=browseFilesys,
        bg="yellow",
        fg="black",
        font=("helvetica", 9, "bold"))
    canvas.create_window(500, 100, window=browseFilesysButton)
    # Button for user to browse for a directory
    browseDirectoryButton = tk.Button(
        text="Browse Directory",
        command=browseDirectory,
        bg="yellow",
        fg="black",
        font=("helvetica", 9, "bold"))
    canvas.create_window(600, 100, window=browseDirectoryButton)
    # Window event loop
    root.mainloop()
