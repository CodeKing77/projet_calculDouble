from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from PIL import Image , ImageTk  #Import de la bibliothèque PIL pour l'affichage des images dans la fenêtre principale

def afficherNombre(event) :  #Fonction qui permet d'afficher len nombre saisi dans le label
    recupererNombre = zoneDeSaisieDuNombre.get()
    labelDuNombre["text"] = f"{recupererNombre}"


def calcul():  #Fonction qui permet de calculer le double du nombre saisi  
    nombre = zoneDeSaisieDuNombre.get()
    
    if nombre.isnumeric():
        nombre = int(nombre)
        doubleDuNombre = nombre * 2 
        resultatVariable.set(f"{doubleDuNombre}")
    else :
        while True :
            showerror("Erreur" , "Veuillez Entrer un nombre entier Positif")
            return   #Pour empêcher l'affichage permanent de la boite de dialogue
        


def calculDuDouble(event):  #Fonction qui permet de calculer le double du nombre saisi
    calcul()   #Importation de la fonction calcul

#Programmtion du bouton Annuler
def annulation():
    zoneDeSaisieDuNombre.delete(0, END)
    zoneAffichageDuResultat.delete(0, END)
    labelDuNombre["text"] = ""



#Création et configuration de la fenêtre principale
fenetre = Tk()
fenetre.title("Calcul du Double ")  #Affichage du Titre de la fenêtre principale
fenetre.geometry("680x450")
fenetre.eval("tk::PlaceWindow . ")   #Pour centrer la fenetre principale
fenetre.resizable(width=False , height=False)
fenetre.config(background="skyblue")   #Couleur d'arriere plan de la fenêtre


# Charger l'image pour l'icône de la fenêtre
icon_path = "C:/Users/lenovo/Desktop/MyApps/projet_calculDouble/calculDouble.png" 
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
fenetre.iconphoto(False, icon_photo)

#Ajout des Widgets 
labelDeSaisie = Label(fenetre , text="Entrer la valeur du Nombre :")
labelDeSaisie.place_configure(x=50 , y=100)

labelDuResultat =Label(fenetre, text="Le résultat du double 2*")
labelDuResultat.place_configure(x=50 , y=250)


labelDuNombre = Label(fenetre, text="")
labelDuNombre.place_configure(x=180 , y=250)


zoneDeSaisieDuNombre = Entry(fenetre)
zoneDeSaisieDuNombre.place(x=280 , y=92, width=350 , height=30)
zoneDeSaisieDuNombre.bind('<KeyRelease>' , afficherNombre)   #Permet de lier  l'éènement de la frappe de clavier à la fonction afficherNombre()
zoneDeSaisieDuNombre.bind('<Return>', calculDuDouble)   #Permet de lier l'évènement de l'appui sur le bouton Entré du clavier à la fonction calculDouble()


resultatVariable = StringVar()
zoneAffichageDuResultat = Entry(fenetre, textvariable=resultatVariable)
zoneAffichageDuResultat.place(x=280 , y=240, width=350 , height=30)



#Ajout des Boutons 
boutonCalculer = Button(fenetre, text='Calculer', command=calcul)
boutonCalculer.place_configure(x=300 , y=350)


boutonAnnuler = Button(fenetre, text='Annuler', command=annulation)
boutonAnnuler.place_configure(x=450 , y=350)


#Affichage de la fenêtre principale
fenetre.mainloop()