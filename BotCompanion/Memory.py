####Chatbot BNC - Surnom : yeoji (contrat. yeojeonhi)
###Yeoji - Corps, Ame et Esprit.
#Ame 

#Stockage des donné connu par Yeoji ainsi que ce qu'elle enregistre (+ valeur de clarté
#(si elle a accés plus ou moins facilement a l'information)+condition(systeme clef>porte à la madeleine de proust)


#faire mail ben

#####################GESTION DE DONNEE#############################
#Ame
### concept (personne, lieux,activité,phrase,vocabulaire, objet)
### planification (futur)
### souvenir, valeur emotionnel, stat pavlovienne , empirique/theorique (passé)
###resultat analyse  envie , emotion, caractére, volonté (present)
###une envie emerge, jt vol contre ;
###actions/capacité
#######fichuer temporaire la vrai memoire sera un fichir raw sauvegarder
#########les methode de gestion  seront dans la classe, dans tool ? ou ici ? 

####Emotion voir whlle, 3 etats par emotion, voir une systeme de jauge en 30 point ? 10 par stades ?
##differend etat de temporalité, que ce soit pour les souvenir, les conversation et les emotion : 2 stade court terme/long terme, voir court terme, moyen terme et long terme

##pour analyse texte, on decompose les phrase (par point'.') , voir si c'est une phrase nominale ou verbale. si verbale , 
#trouver le sujet le verbe et le complement, consulter le dictionnaire recupérer les valeur emotionnel, calculer la reaction, se reporter au sujet de la phrase et de la conversation, 
#voir les probabilité d'apprentissage , construir une phrase de reponse(tour par tour dans un premier temps)
#la reaction va egalement etre stocker dasn les souvenir et modifier son etat d'ame et comportement  en changeant les stat (stat emotion , bon/mauvais pour ses emotion, et stat pavlovienne (reponse coherente ou non))

#systeme d'apprentissage pavlovien ? quand la reponse donnée est coherente j'appuis sur un bouton qui enverra un stimulie pour dire que c'est une bonne reponse.a l'inverse envoyer un stimulie negatif

#ajout de commande speciale, pour consulter les donnée dans le chat directement genre "!:nom_de_l'element_a_verifier"



Memory={}##peut etre voir la gestion de donnée via un module approprier ex : sql

####slot Options de jeu
Memory['user_name'] = "None"
Memory['text_color'] = "#000000"
Memory['text_bg'] = "#ffffff"

####slot Langage
Memory['Pronoms'] = ['je','tu','il','elle','vous','nous','ils','elles']
Memory['Hello'] = ['hey','coucou','salut','bonjour','hello','yo']

