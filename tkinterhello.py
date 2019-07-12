from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Willkommen bei roeschke&roeschke")
window.geometry('600x400')
lbl = Label(window, text="Hallo Welt!")
lbl.grid(column=0, row=0)
 
def buttonclicked():
    lbl.configure(text="Button wurde geklickt!")
    messagebox.showinfo('Nachrichten Box', 'Danke fürs anklicken und viel Spass beim Nürnberg Digital Festival 2019!')
    btn.destroy
 
def buttonexit():
    exit()

btn = Button(window, text="Klick mich", command=buttonclicked)
btn.grid(column=6, row=6)
btnExit = Button(window, text="Beenden", command=buttonexit)
btnExit.grid(column=9, row=9)
window.mainloop()