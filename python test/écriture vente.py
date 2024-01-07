from prettytable import PrettyTable
import matplotlib
from tkinter import * 
from tkinter import ttk


###  Tableau de bord d'utilisation des futures fonctions  ###

window = Tk()
window.title("Guyz.prod mode de comptabilité")
window.geometry("1000x700")
window.iconbitmap("COMPTA.jpeg") # logo dans le titre de la fenêtre
window.config(background="#9984BF")

frame = Frame(window, bg="#9984BF")


# bouton écriture vente #

frame.pack(expand=YES)

###  écriture  Vente   ###

#def écriture_Vente():
    #window = Tk()
    #window.title("Guyz.prod mode de comptabilité")
    #window.geometry("1000x700")
    #window.iconbitmap("COMPTA.jpeg") # logo dans le titre de la fenêtre
    #window.config(background="#9984BF")

    #frame = Frame(window, bg="#9984BF") 
    #e = Entry(window, width=50, bg="white",fg="black", borderwidth="5",)
    #e.pack()
    #e.get

    Date_day = int(input("Vous allez choisir la date de l'écriture comptable en 3 temps, d'abord le jour "))
    #my_label1 = Label(window, text=e.get())
    #my_label1.pack()
    #Date_day = my_label1
    
    Date_month = int(input("choissez le mois pour l'écriture comptable "))


    Date_year = int(input("choissez l'année  pour l'écriture comptable "))


    prix_vente_HT = int(input("indiquez le prix de vente HT de la marchandise en € ! "))


    Taux_TVA = 0.2
    TVA = Taux_TVA * prix_vente_HT
    Prix_TTC = prix_vente_HT + TVA
    


    
    Date_écriture = (str(Date_day)+"/"+str(Date_month)+"/"+str(Date_year))

    print ("prix de vente HT :",prix_vente_HT) 
    print("comptabilisation du",Date_écriture)
    print("Vous avez une TVA collectée de :", TVA)
    print("Le client vous doit :", Prix_TTC)

    ## mise ne forme du tableau ## 
    
    tableau_vente = PrettyTable(['compte', Date_écriture,'débit', 'crédit'])
    tableau_vente.add_row(['707', 'Vente de marchandises', '' ,str(prix_vente_HT)])
    tableau_vente.add_row(['44571', 'TVA collectée', "", str(TVA)])
    tableau_vente.add_row(['411', 'clients', str(Prix_TTC), ''])

    print(tableau_vente)

    en.title("comptabilisation de la vente du", Date_écriture)
   screen.geometry

    #window = Tk()
    #window.title("Comptabilisation de la vente au " +str(Date_écriture))
    #window.geometry("600x420")

   # frame = Frame(window)

    #Label_title = Label(frame, text = str(tableau_vente), font=("Arial", 20))
    #Label_title.pack()
  
    #frame.pack(expand=YES)

    #window.mainloop()


  # window = Tk()
  # window.title("Comptabilisation vente du " +str(Date_écriture))
  # window.geometry("600x420")
   #window.minsize("")
   #window.iconbitmap("") #mettre le nom du fichier asssocié au logo


#écriture_Vente()

vente_button= Button(frame, text="Vente", font=("Arial", 20), bg="#9984BF", fg="black", command=écriture_Vente)
vente_button.pack(fill=X) 
### fin fonction écriture vente ###

##################################

##   charge à payé et facture à recevoir  ##




# affichage de la fenêtre # 
window.mainloop()