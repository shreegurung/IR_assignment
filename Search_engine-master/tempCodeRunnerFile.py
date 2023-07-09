from tkinter import *
import tkinter as tk
window = tk.Tk()
window.title("Publication Search")
window.geometry("600x650")
window.configure(bg="#111D88")
window.resizable(0,0)
from PIL import ImageTk, Image
img=(Image.open("coventry-university-logo.png"))
imgg=img.resize((200,200))
imggg=ImageTk.PhotoImage(imgg)

lbl=Label(window,image=imggg,bg="#111D88")
lbl.pack(side=TOP)
# Create and position the search label
label = tk.Label(window, text="Enter author name or title name:",fg="white",font=("Arial", 20,"italic"),bg="#111D88")
label.pack(pady=10)

# Create and position the search entry
entry = tk.Text(window,height=10,width=30,font=("Arial", 20))
entry.pack()

# Create and position the search button
button = tk.Button(window, text="Search",font=("Arial", 20),bg="#10164B",fg="white")
button.pack(pady=10)


# Start the main event loop
window.mainloop()
