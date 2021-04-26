import tkinter as tk
from PIL import ImageTk, Image

root= tk.Tk()

root.title("Cell Counting Application")

canvas1=tk.Canvas(root, width=1000, height=1000, relief="raised")
canvas1.pack()

label1=tk.Label(root, text="Cell Counting Application!")
label1.config(font=("helvetica", 14))
canvas1.create_window(500, 25, window=label1)

label2=tk.Label(root, text="Input image path:")
label2.config(font=("helvetica", 10))
canvas1.create_window(500, 50, window=label2)

entry1=tk.Entry(root) 
canvas1.create_window(500, 75, window=entry1)

global background_label
global label3
global label4
global done
global once
done=False
once=False
def getPath():
	global done
	global once
	global label3
	global label4
	global background_label

	x1 = entry1.get()

	if once:
		label3.config(text="")
	once=True

	if done:
		background_label.config(image="")
		label4.config(text="")
	try:
		background_image=ImageTk.PhotoImage(Image.open(x1))
	except:
		label3=tk.Label(root, text="Please input a valid relative or absolute file location", font=("helvetica", 10))
		canvas1.create_window(500, 125, window=label3)
		return
	background_label=tk.Label(root, image=background_image)
	background_label.place(x=0, y=150, relwidth=1, relheight=1)
	root.photo = background_image
	root.grid()

	# label3=tk.Label(root, text="The number of cells is:", font=("helvetica", 10))
	label3=tk.Label(root, text="Image is: "+x1, font=("helvetica", 10))
	canvas1.create_window(500, 125, window=label3)

	label4=tk.Label(root, text="Some text about count here", font=("helvetica", 10))
	canvas1.create_window(500, 150, window=label4)

	button1.lift()
	done=True
    
button1 = tk.Button(text="Go!", command=getPath, bg="brown", fg="white", font=("helvetica", 9, "bold"))
canvas1.create_window(500, 100, window=button1)

root.mainloop()