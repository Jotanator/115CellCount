class UIInterface():
    # All the necessary UI components of this application

    def initUI():
        pass

    def showUI(root):
        pass

    def appHeader(root, canvas):
        pass

    def showFileUploadButton(root, canvas, func, *args):
        pass

    def browseFilesys(root, canvas, outputHandler):
        filename = filedialog.askopenfilename()
        try:
            background_image = ImageTk.PhotoImage(Image.open(filename))
        except (OSError, IOError):
            label3 = tk.Label(root,
                              text="Please input a valid "
                              + "relative or absolute file location",
                              font=("helvetica", 10))
            canvas.create_window(500, 250, window=label3)
            return
        background_label = tk.Label(root, image=background_image)
        background_label.place(x=0, y=150, relwidth=1, relheight=1)
        root.photo = background_image
        root.grid()

        label3 = tk.Label(root, text="Image is: " + filename,
                          font=("helvetica", 10))
        canvas.create_window(500, 125, window=label3)

        countMsg = "There are " + str(outputHandler.getPrediction())
        + " cells in this image"
        label4 = tk.Label(root, text=countMsg, font=("helvetica", 10))
        canvas.create_window(500, 150, window=label4)

        showCSVDownloadButton(canvas, filename, 17, 0.4)

    def showGetPredictionButton(root, canvas, func, args):
        pass

    def displayPredictionOutput(root, canvas, func, args):
        pass

    def showCSVDownloadButton(canvas, filename, number, percent):
        downloadButton = tk.Button(text="Download information about file",
                                   command=lambda: (writeToCSV(filename,
                                                               number,
                                                               percent)),
                                   bg="brown", fg="white",
                                   font=("helvetica", 9, "bold"))
        canvas.create_window(500, 200, window=downloadButton)
