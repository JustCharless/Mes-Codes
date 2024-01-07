# générateur de mot de passe
import string
from random import randint, choice
from tkinter import * 

#def generate_password(): 
   # password_min = 6
   # password_max = 12
  #  all_chars = string.ascii_letters + string.punctuation + string.digits
  #  password = "".join(choice(all_chars) for x in range(randit(password_min, password_max))
  #  password_entry.delete(0, END)
  #  password_entry.insert(0, password)

# fenêtre 
window = Tk()
window.title("générateur de mot de passe")
window.geometry("1200x700")
window.iconbitmap("eda.png") # logo dans le titre de la fenêtre
window.config(background="#A7D4F5")

#frame principale 

frame = Frame(window, bg="#A7D4F5")


#création d'une image
width = 500
height = 500
image = PhotoImage(file="goku.png").zoom(35).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg="#A7D4F5", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image) #espace pour la création graphique
canvas.pack()
  
#création sous boite
#right_frame = Frame(frame, bg="#A7D4F5")

#création titre
label_title = Label(frame, text="mot de passe", font=("Arial", 20), bg="#A7D4F5", fg="white")
label_title.pack()

#password_entry = Entry(right_frame,font=("Arial", 20), bg="#A7D4F5", fg="white")
#password_entry.pack()


#création bouton
#génération_password_button= Button(right_frame, text="Générer", font=("Arial", 20), bg="#A7D4F5", fg="white", command=generate_password)
#génération_password_button.pack(fill=X) 

#sous à doit de la frame principale
#right_frame.pack(row=0, column=1, sticky=W)

frame.pack(expand=YES)


#affichage de la fenêtre 
window.mainloop()
