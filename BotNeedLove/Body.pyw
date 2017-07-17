### IA depressive


###note : constructor pour les box = un eliste de bouton, une de texte, une de logo, une de style et associer aléatoirement tout ça
######comment rndre tout ça interessant? narration? introspection du user ? que faire des resultats?


import Mind as ame
from random import randrange

while True:
        
       ame.Chrono(randrange(120),True)
       ame.box[  randrange( len(ame.box) )  ]("- BotNeedLove 0.0 - ", ame.phrase[ randrange( len( ame.phrase) )])
