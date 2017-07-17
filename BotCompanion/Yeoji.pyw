####Chatbot BNC - Surnom : yeoji (contrat. yeojeonhi)##########
###Yeoji - Corps, Ame et Esprit.                       #############
#Corps


import os

from tkinter import *
from tkinter.filedialog import *
import tkinter.colorchooser as clr

import time
import pickle#sauvegarde des parametre

import Esprit
import Memory

animeNum=0 #numero de la frame courant
mem={} #variable local qui reçoit les donnee de Ame.alive

#### analyse , prise de decision, la partie logique, L'ia


### ajout jeu commun  pour joueur en rivalité avec l'ia et cooperation (notion d'apprendtissage )
###mettre tout ça dans tools ?


####fair une interface graphique pour la gestion et creation des animes ?
##class gestion_anime:
 
def play_anime(frq, win, widget, frames,img):

        global animeNum

        loadImage = frames.Frames[animeNum]
       # widget.create_image(576/2, 323/2, image = loadImage) ###on utilise itemconfig maintenant, IC remplace l'image, create_image en créer une autre, les image s'accumule pour rien
        widget.itemconfig( img, image=loadImage)
        
        if animeNum< len(frames.Frames)-1:
                animeNum +=1
        else:
                animeNum = 0

        win.after(frq, play_anime, frq,win , widget, frames,img)
               
        
class animation:

        def __init__(self, name,dossier):

                self.name=name
                self.Frames=[]
                self.nameF= os.listdir(dossier)
                
                for nom in self.nameF:
                        
                        fram = PhotoImage(file = dossier+'\\'+nom)
                        self.Frames.append(fram)



###interface

def TimeStart(start) : #donne le temps depuis le lancement de l'app
        t = time.time() - start
        return t


def Chrono(s):
        print(s)
        start_t =round  (time.time())
        print (start_t)
        while round(time.time() - start_t)  < s :
                print(round(time.time() - start_t))

        return True


def displayOptionsText ():
	 couleur = clr.askcolor()
	 mem['text_color'] =couleur[1]
	 Esprit.save(mem)# sauvegarde
	 messages.config(foreground = mem['text_color'] )


def displayOptionsBG ():
	 couleur = clr.askcolor()
	 mem['text_bg'] =couleur[1]
	 Esprit.save(mem)# sauvegarde
	 messages.config(background = mem['text_bg'] )



def displayProfil():
        
        def validate_name():
                
                #global  profil_name
                mem['user_name'] = in_name.get()
                Esprit.save(mem)#sauvegarde donnée
                profilfen.destroy()
                
                
		
        profilfen=Toplevel()
        profilfen.resizable(width=False, height=False)
        profilfen.wm_title("Profil")

        Name=Label(profilfen, text="Name : "+ mem['user_name'])
        Name.grid(column=0, row = 0)
        

        input_name=StringVar()
        in_name=Entry(profilfen, text=input_name)
        in_name.grid(column=2, row = 0)

        ok=Button(profilfen, text="OK", command = validate_name)
        ok.grid(column=0,row=1)

        profilfen.mainloop()


def Enter_pressed(event):
        input_get = input_field.get() 

        if (input_get != ""):

	
                    messages.config(state="normal")
                    messages.insert(END, '\n'+ mem['user_name']+" :"+'\n'+input_get+'\n')
                    messages.config(state="disabled")
                    messages.see("end")
                    # label = Label(window, text=input_get)
                    input_user.set("")
                    # label.pack()
    
if os.path.exists("Ame.alive"): ##la ça va mais peut etre prevoir un ajout en cas de modif de memory alors que l'ame est déjà bien travailler

   mem=Esprit.load()

else:
   Esprit.save(Memory.Memory)
   mem=Esprit.load()
   
window = Tk()
##window.geometry('500x385')
window.resizable(width=False, height=False)

window.wm_title("BotCompanion")

NameBot = Label(window, text="Yeoji")
NameBot.grid(row=0, column=0, columnspan=1)


messages = Text(window, state="disabled", height=20, width=30, foreground=mem["text_color"])
messages.grid(column=1, row=1)

input_user = StringVar()
input_field = Entry(window, width= 40, text=input_user)
input_field.grid(column=1,row=2)
input_field.bind('<KeyPress-Return>', Enter_pressed)
can = Canvas(window, height=323, width=576, bg="black")
cam = PhotoImage(file="Corps\\cam.gif")
lectimg=can.create_image(576/2, 323/2, image = cam)
can.grid(column=0,row=1)

menuBar = Menu(window)
window['menu'] = menuBar

sousMenu = Menu(menuBar)
Menuopt=Menu(sousMenu)

menuBar.add_cascade(label='Menu', menu=sousMenu)
sousMenu.add_cascade(label='Options', menu=Menuopt)
Menuopt.add_command(label="ColorBackground", command=displayOptionsBG)
Menuopt.add_command(label="ColorText", command=displayOptionsText)
sousMenu.add_command(label='Profil', command=displayProfil)

###test creation anime
anime_zero = animation("test", 'Corps\\animewtf')
#anime_zero = animation("test", ['Corps\\0.gif', 'Corps\\1.gif', 'Corps\\2.gif']) ###essayer de trouver une methode pour pouvoir utiliser des jpeg et non des gifs
play_anime( 10,window, can, anime_zero ,lectimg)#frq=milliseconde

window.mainloop()





