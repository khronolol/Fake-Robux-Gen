from tkinter import *
from time import *
import webbrowser

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    time_label.after(1000,update)
def click():
    handle = webbrowser.get()
    handle.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


window = Tk()

time_label = Label(window,font=("Arial",16),fg="#b59cb3",bg="#23282e")
time_label.pack()

day_label = Label(window,font=("Arial",25,"bold"))
day_label.pack()

date_label = Label(window,font=("Arial",30))
date_label.pack()

window.geometry("420x420")
window.title("Free Robux Now!")

icon = PhotoImage(file='icon.png')
window.iconphoto(True,icon)
window.config()

image = PhotoImage('file=robux.png')

button = Button(window,
                text="Generate robux",
                command=click,
                font=("Segoe UI",35),
                fg="#6557ff",
                bg="gray",
                activeforeground="#6557ff",
                activebackground="gray",
                state=ACTIVE,)

button.pack()




update()

window.mainloop()
