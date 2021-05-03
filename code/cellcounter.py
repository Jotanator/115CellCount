import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import csv

root= tk.Tk()

root.title("Cell Counting Application")

canvas1=tk.Canvas(root, width=1000, height=1000, relief="raised")
canvas1.pack()

label1=tk.Label(root, text="Cell Counting Application!")
label1.config(font=("helvetica", 14))
canvas1.create_window(500, 25, window=label1)

label2=tk.Label(root, text="Browse for image:")
label2.config(font=("helvetica", 10))
canvas1.create_window(500, 50, window=label2)

def browseFilesys():
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

	label4=tk.Label(root, text="Some text about count here", font=("helvetica", 10))
	canvas1.create_window(500, 150, window=label4)

	number = 14;
	percent = .40

	def writeToCSV():
		with open(filename+'.csv', 'w', newline='') as file:
			writer = csv.writer(file)
			writer.writerow(["This is the information for "+str(filename)])
			writer.writerow(["Number of cells is: "+str(number)])
			writer.writerow(["Percent of alive cells is: "+str(percent*100)+"%"])
			writer.writerow(["This is all hardcoded"])

	downloadButton=tk.Button(text="Download information about file", command=writeToCSV, bg="brown", fg="white", font=("helvetica", 9, "bold"))
	canvas1.create_window(500, 200, window=downloadButton)

browseButton=tk.Button(text="Browse", command=browseFilesys, bg="brown", fg="white", font=("helvetica", 9, "bold"))
canvas1.create_window(500, 100, window=browseButton)

root.mainloop()
