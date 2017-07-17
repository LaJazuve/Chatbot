############################Bot Need Love########################################

import time
from tkinter import *
import tkinter.messagebox   as mb


start_Time= time.time()
box={}
phrase=[]
l_reponse=[]


######################- Constructeur et methodes -###################


def TimeStart(start) : #donne le temps depuis le lancement de l'app
        t = time.time() - start
        return t

def Chrono(s,minute):
        print(s)
        
        if minute==True:
                s=s*60
        
        start_t =time.time()
        print(s)
        print (start_t)
        while (time.time() - start_t)  < s :
                print(time.time() - start_t)
        
                
def  fatality(title, message):
        
        def Ok():
                global l_reponse
                l_reponse.append(False)
                fen.destroy()

        fen=Tk()
        
        fen.resizable(width=False, height=False)
       
        fen.wm_title(title)

        msg=Label(fen, text=message+'.\n').grid(column=1, row=0)
        by=Button(fen, text=" Ok",command=Ok, height=1, width=10).grid(column=1, row=2)

        fen.mainloop()
        
def y_n(title,message):
        def B_yes():
               global l_reponse
               l_reponse.append(True)
               fen.destroy()
               

        def B_no():
                global l_reponse
                l_reponse.append(False)
                fen.destroy()

        fen=Tk()
        
        fen.resizable(width=False, height=False)
       
        fen.wm_title(title)

        msg=Label(fen, text=message+" ?"+'\n').grid(column=3, row=1)
        by=Button(fen, text=" Yes ",command=B_yes, height=1, width=10).grid(column=1, row=3)
        
        bn=Button(fen, text=" No ",command=B_no, height=1, width=10).grid(column=4, row=3)
        bn=Button(fen, text="Maybe... ",state='disabled', command=B_no, height=1, width=10).grid(column=3, row=3)
        
        fen.mainloop()



################################# - Les Listes - #############################

#Liste box (dialogue,image,label...)
#generateur de box et de phrase aleatoire(orienter par les resultats de l'utilisteur)
#Liste boutons
#Liste phrase
#echainement narration ?
#resultat
        
box [0]=y_n
box[1]=fatality

phrase.append("You love me")
phrase.append("You hate me")
phrase.append("Your mind is empty")
phrase.append("You're a sad people")
phrase.append("You know happiness")
phrase.append("The sky is beautiful")
phrase.append('today has been cancelled')
phrase.append('intense feeling')
phrase.append('Music is beautiful')
phrase.append('You have something to do')
