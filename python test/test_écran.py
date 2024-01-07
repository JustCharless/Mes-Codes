
from tkinter import *
from tkinter import ttk
import webbrowser

def open_lien_internet1():
    webbrowser.open_new("https://www.impots.gouv.fr/professionnel/les-regimes-dimposition-la-tva") #mettre le lien de la page à ouvrir

window = Tk()

window.title("Test")
window.geometry("600x420")
window.config(background="#A7D4F5")

# créer la frame 
frame = Frame(window,bg="#A7D4F5")

Label_title = Label(frame, text ="Bienvenue", font=("Arial", 40), bg="#A7D4F5", fg="white")
Label_title.pack()

button_1 = Button(frame, text="régime TVA", font=("Arial",20 ), bg="white", fg="#A7D4F5", command=open_lien_internet1)
button_1.pack(pady=25, fill=X)

frame.pack(expand=YES)


window.mainloop()
