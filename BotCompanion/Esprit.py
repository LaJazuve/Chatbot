####Chatbot BNC - Surnom : yeoji (contrat. yeojeonhi)##########
###Yeoji - Corps, Ame et Esprit.                       ##########
#Esprit


#liste des methode et class uriliser par l'ia

import pickle

name=""


def save(donnee):

        with open('Ame.alive','wb') as fichier:
                
                pickler = pickle.Pickler(fichier)
                pickler.dump(donnee)

def load():

        with open('Ame.alive','rb') as fichier:
                depickler = pickle.Unpickler(fichier)
                donnee=depickler.load()
        return donnee



                


                #input
                #analyse
                #reaction
                #constructor msg
                #output

                

                
