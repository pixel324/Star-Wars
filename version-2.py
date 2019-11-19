#----------Importation----------#
import pygame
from pygame.locals import *
from random import *
from classes.principal import *

#----------Codes Couleurs----------#
YELLOW = 255, 177, 58
YELL = 255, 255, 0
BLACK = 0, 0, 0
BLUE = 75, 213, 238
Red = 255, 0, 0
WHITE = 255,255,255

#----------Initialisation Pygame----------#
pygame.init()
pygame.font.init()

#----------Importation Des Sons----------#
son = pygame.mixer.Sound("Musiques/WARS.wav")
sonmenu = pygame.mixer.Sound("Musiques/batle.wav")

#----------Importation Des Polices----------#
font = pygame.font.Font('Polices/SWCrawlBody.ttf', 45)
fontsup = pygame.font.Font('Polices/SWCrawlBody.ttf', 20)
font2 = pygame.font.Font('Polices/SWCrawlTitle.ttf', 70)
font3 = pygame.font.Font('Polices/FRABK.TTF', 50)

#----------Création De La Fenètre----------#
cheese = 0
cool = 0
x = True
fenetre = pygame.display.set_mode((600, 600))
pygame.display.set_caption('STAR WARS')
fenetre.fill(BLACK)
pygame.draw.rect(fenetre, WHITE, (49,49,502,512))
pygame.draw.rect(fenetre, BLACK, (50,50,500,510))
fond_pres = pygame.image.load("Images/presentation.png").convert()
fenetre.blit(fond_pres,(50,50))
pygame.draw.rect(fenetre, WHITE, (140,450,120,40))
pygame.draw.rect(fenetre, WHITE, (340,450,120,40))
pygame.draw.rect(fenetre, WHITE, (250,520,100,40))
while x==True:
    if cheese == 0:
        pygame.draw.rect(fenetre, Red, (141,451,118,38))
        pygame.draw.rect(fenetre, BLACK, (341,451,118,38))
    else:
        pygame.draw.rect(fenetre, BLACK, (141,451,118,38))
        pygame.draw.rect(fenetre, Red, (341,451,118,38))

    message1 = fontsup.render("Plein Ecran", 0, WHITE)
    message2 = fontsup.render("1024x768", 0, WHITE)
    message3 = fontsup.render("Lancer", 0, BLACK)
    fenetre.blit(message1,(150,458))
    fenetre.blit(message2,(350,458))
    fenetre.blit(message3,(270,527))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cool = 1
            x = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x>140 and x<260 and y>450 and y<490:
                cheese = 0
                x = True
            if x>340 and x<460 and y>450 and y<490:
                cheese = 1
                x = True
            if x>250 and x<350 and y>520 and y<560:
                x = False
if cool == 0:
    if cheese == 0:
        fenetre = pygame.display.set_mode((1024, 768),FULLSCREEN)
    if cheese == 1:
        fenetre = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('STAR WARS')

#----------Importation Des Images----------#

#--Images générique et menu--#
fond = pygame.image.load("Images/Menu-generique/espace.jpg").convert()
titre = pygame.image.load("Images/Menu-generique/titre.png").convert()
jouer = pygame.image.load("Images/Menu-generique/jouer.png").convert()
options = pygame.image.load("Images/Menu-generique/options.png").convert()
quitter = pygame.image.load("Images/Menu-generique/quitter.png").convert()
zone = pygame.image.load("Images/Menu-generique/zone.png").convert(24)
vaisseau = pygame.image.load("Images/Menu-generique/vaisseau.png").convert()
vaisseau = pygame.transform.scale(vaisseau,(100,100))
vaisseau = pygame.transform.rotate(vaisseau, 40)

#--Images utilitaires--#
optionnel = pygame.image.load("Images/Utilitaires/optionnel.png").convert()
background = pygame.image.load("Images/Utilitaires/background.jpg").convert()
conf = pygame.image.load("Images/Utilitaires/confrontation.png").convert()
plaque = pygame.image.load("Images/Utilitaires/plaque.png").convert_alpha()
pointeur = pygame.image.load("Images/Utilitaires/pointeur.png").convert_alpha()
pointeur = pygame.transform.scale(pointeur,(120,80))
plateau = pygame.image.load("Images/Utilitaires/plateau.png").convert_alpha()
select = pygame.image.load("Images/Utilitaires/selection.png").convert_alpha()
select2 = pygame.image.load("Images/Utilitaires/selection2.png").convert_alpha()
gris = pygame.image.load("Images/Utilitaires/gris.png").convert_alpha()
sonore = pygame.image.load("Images/Utilitaires/barre de sons.png").convert()
réu = pygame.image.load("Images/Utilitaires/ok.png").convert()
réu = pygame.transform.scale(réu,(40,40))

#--Images planetes--#
coruscant = pygame.image.load("Images/Planetes/Coruscant.png").convert_alpha()
jakku = pygame.image.load("Images/Planetes/jakku.png").convert_alpha()
mustafar = pygame.image.load("Images/Planetes/mustafar.png").convert_alpha()
tatoine = pygame.image.load("Images/Planetes/tatoine.png").convert_alpha()

#--Images maps--#
map1 = pygame.image.load("Images/Maps/combat_coruscant.jpg").convert_alpha()
map2 = pygame.image.load("Images/Maps/combat_jakku.jpg").convert_alpha()
map3 = pygame.image.load("Images/Maps/combat_mustafar.jpg").convert_alpha()
map4 = pygame.image.load("Images/Maps/combat_tatoine.jpg").convert_alpha()

#--Images rôles possibles--#
role1 = pygame.image.load("Images/Roles/role1.png").convert_alpha()
role2 = pygame.image.load("Images/Roles/role3.png").convert_alpha()
role3 = pygame.image.load("Images/Roles/role2.png").convert_alpha()
role4 = pygame.image.load("Images/Roles/role4.png").convert_alpha()
role5 = pygame.image.load("Images/Roles/role5.png").convert_alpha()
role6 = pygame.image.load("Images/Roles/role6.png").convert_alpha()
role7 = pygame.image.load("Images/Roles/role7.png").convert_alpha()
role8 = pygame.image.load("Images/Roles/role8.png").convert_alpha()

#----------Définition de la touche échap----------#
def echapatoire(x,event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            return(x)

#----------Definition De la Plaque Du Joueur----------#
def apparition_plaque(classe,xp):
    liste = [role1,role2,role7,role8,role3,role4,role5,role6]
    font2 = pygame.font.Font('Polices/FRABK.TTF', 14)
    fondu = pygame.font.Font('Polices/FRABK.TTF', 10)
    titre = font2.render("Niveau " + str(classe.niveau), 0, Red)
    titrage = fondu.render("(" + str(xp) + " / " + str(classe.rekt[classe.niveau]) + " XP)", 0, Red)
    titre2 = font2.render(classe.grade, 0, Red)
    fenetre.blit(titre, (102,25))
    fenetre.blit(titrage, (165,27))
    fenetre.blit(titre2, (102,48))
    fenetre.blit(liste[classe.rang],(25,25))

#----------Définition de choix du role----------#
def choix_role(liste2, liste3):
    clic = 0
    liste1 = [(145,500),(315,500),(145,600),(315,600),(657,500),(827,500),(657,600),(827,600)]
    while clic >=0:
        if clic == 0 :
            fenetre.blit(conf, (0,0))
            font2 = pygame.font.Font('Polices/FRABK.TTF', 50)
            font = pygame.font.Font('Polices/SWCrawlBody.ttf', 70)
            choisir = font.render("Fait ton choix !", 0, YELLOW)
            titre = font2.render("La force", 0, YELLOW)
            titreBis = font2.render("Le Côte Obscure", 0, YELLOW)
            fenetre.blit(choisir, (300,60))
            fenetre.blit(titre, (150,360))
            fenetre.blit(titreBis, (600,360))
            pygame.display.flip()
            for event in pygame.event.get():
                valeur = echapatoire(0,event)
                if valeur == 0:
                    return(-1)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if x>0 and x<512:
                        clic = 1
                    if x>512 and x<1024:
                        clic = 2
            exposant = cliquable(clic)
            if exposant !=0:
                a = exposant[0]
                b = exposant[1]
                clic = 3
        if clic == 3:
            for i in range(a,b):
                fenetre.blit(liste2[i],liste1[i])
            pygame.display.flip()
            for event in pygame.event.get():
                valeur = echapatoire(0,event)
                if valeur == 0:
                    clic = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for i in range(a,b):
                        coop = liste1[i]
                        if x>coop[0] and x<coop[0]+50 and y>coop[1] and y<coop[1]+50:
                            v = liste3[i]
                            del liste3[i]
                            return(v)

#----------Definition Des Zones----------#
def page_bouge(liste1,liste2,act,acti):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            valeur = 0
            x, y = event.pos
            for i in liste1:
                if x>i[0] and x<i[1] and y>i[2] and y<i[3]:
                    return(liste2[valeur])
                valeur = valeur + 1
                if acti == 1:
                    if act==0:
                        if x>312 and x<712 and y>100 and y<273:
                            listeBonus = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png"]
                            for i in listeBonus:
                                a = "Images/Bonus/" + i
                                ac = pygame.image.load(a).convert_alpha()
                                fenetre.blit(ac,(0,0))
                                pygame.display.flip()
                                if i!="10.png":
                                    pygame.time.delay(100)
                            return(-7)
                if x>850 and x<1020 and y>10 and y<40:
                    return(-1)
    return(1)

#----------Definition De Mouvement La Planet Choisi (pour agrandissement)----------#
def mouvement(position,x,utilisation,sens):
    x = x+2*sens
    utilisation = pygame.transform.scale(utilisation,(x,x))
    fenetre.blit(utilisation, position)
    pygame.display.flip()
    pygame.time.delay(5)
    return(x)

#----------Definition D'Agrandissement De La Planet----------#
def agrandissement(position,sens):
    a = position[0]-1*sens
    b = position[1]-1*sens
    position = (a,b)
    return(position)

#----------Definition De Déplacement De La Planet avant----------#
def deplacement_planet(position,utilisation,a,b):
    fenetre.blit(background, position, position)
    position = position.move(1*a, 1*b)
    fenetre.blit(utilisation, position)
    pygame.display.update()
    pygame.time.delay(10)
    return(position)

#----------Réglages pour le zoom avant d'une planete----------#
def calcul_deplacement(positionnement,utilisation,x,y,vrai,sens):
    resultat1 = calculette1(sens,vrai,x,y)
    j = resultat1[0]
    k = resultat1[1]
    x = resultat1[2]
    y = resultat1[3]
    while x!=j:
        resultat2 = calculette2(j,k,x,y)
        a = resultat2[0]
        b = resultat2[1]
        x = resultat2[2]
        y = resultat2[3]
        positionnement = deplacement_planet(positionnement,utilisation,a,b)
    tableau = [x,y,positionnement]
    return(tableau)

#----------Réglages pour le zoom avant d'une planete----------#
def reglage(x,y,positionnement,utilisation):
    resultat = calcul_deplacement(positionnement,utilisation,x,y,0,1)
    g = 150
    position = (437,289)
    for i in range(0,300):
        position = agrandissement(position,1)
        g =  mouvement(position,g,utilisation,1)
    tableau = [resultat[2],resultat[0],resultat[1],position]
    return(tableau)
    
#----------Réglages pour le zoom arrière d'une planete----------#
def reglage2(utilisation,position,background,planete,position2,clic,vrai,positionnement,classe,xp):
    g = 750
    for i in range(0,300):
        fenetre.blit(background, (0,0))
        fenetre.blit(plaque, (0,0))
        apparition_plaque(classe,xp)
        for i in range(0,4):
            if i!=clic:
                fenetre.blit(planete[i], position2[i])
        position = agrandissement(position,-1)
        g =  mouvement(position,g,utilisation,-1)
        pygame.display.flip()
        pygame.time.delay(10)
    calcul_deplacement(positionnement,utilisation,0,0,vrai,-1)
    
#----------Définition de clic du niveau----------#
def zone_traitement(coco):
    x = 0
    while x!=1:
        for event in pygame.event.get():
            valeur = echapatoire(0,event)
            if valeur == 0:
                return(-1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i in range(0,len(coco)):
                    if x>coco[i][0]-50 and x<coco[i][0]+170 and y>coco[i][1] and y<coco[i][1]+80:
                        return(i)

#----------placement des éléments qui ferons notre carte----------#
def plancement_partie(position,classe,xp,font4):
    fenetre.blit(background, (0,0))
    fenetre.blit(plaque, (0,0))
    apparition_plaque(classe,xp)
    fenetre.blit(mustafar, position[0])
    fenetre.blit(jakku, position[1])
    fenetre.blit(tatoine, position[2])
    fenetre.blit(coruscant, position[3])
    plaque_quitte = pygame.transform.scale(zone,(170,30))
    fenetre.blit(plaque_quitte,(850,10))
    titre2 = font4.render("Quitter la partie", 0, YELLOW)
    fenetre.blit(titre2,(850,10))
    pygame.display.flip()

#----------placement des premiers éléments sur la planete zoomé----------#
def mise_en_place_partie(boucle,font4,x,y,positionnement,utilisation,classe,liste_image_enemi,clic,réussite,act):
    plaque_quitte = pygame.transform.scale(zone,(170,30))
    fenetre.blit(plaque_quitte,(850,10))
    titre2 = font4.render("choix niveau", 0, YELLOW)
    fenetre.blit(titre2,(865,10))
                    
    if act == 0:
        positionnement = utilisation.get_rect()
        positionnement = positionnement.move(x,y)
        a = reglage(x,y,positionnement,utilisation)
    if act ==1:
        utilisation = pygame.transform.scale(utilisation,(750,750))
        fenetre.blit(utilisation,(137,-11))
        a = 0
    pygame.display.flip()
    boucle = boucle +1
                    
    font = pygame.font.Font('Polices/FRABK.TTF', 20)
    textemanuscrit = [classe.listeplane1,classe.listeplane2,classe.listeplane3,classe.listeplane4]
    texte_utile = textemanuscrit[clic]
                    
    position_b = 220
    for i in range (0,len(texte_utile)+1):
        if i<len(texte_utile):
            titre = font.render(texte_utile[i], 0, WHITE)
            fenetre.blit(titre,(350,position_b))
        else :
            if réussite[clic] == [1,1,1,1,1,1]:
                titre = font.render(classe.autotexte2, 0, WHITE)
                fenetre.blit(titre,(350,position_b+20))
                fenetre.blit(liste12[classe.rang], (650,position_b+20))
            else:
                titre = font.render(classe.autotexte, 0, WHITE)
                fenetre.blit(titre,(350,position_b+20))
                fenetre.blit(liste_image_enemi[clic], (650,position_b+15))                
        position_b = position_b +20  
        pygame.display.flip()
    return(utilisation,classe,boucle,a)

#----------placement des diffèrents éléments visuel sur la planete zoomé----------#
def placement_planete_grande(boucle,réussite,ordonnance,clic,compt):
    coco = [(180,150),(130,300),(180,500),(730,150),(780,300),(730,500)]
    pointeur_negatif = pygame.transform.flip(pointeur, True, False)
    fenetre.blit(pointeur_negatif, coco[0])
    fenetre.blit(pointeur_negatif, coco[1])
    fenetre.blit(pointeur_negatif, coco[2])
    fenetre.blit(pointeur, coco[3])
    fenetre.blit(pointeur, coco[4])
    fenetre.blit(pointeur, coco[5])
    mots = ["niveau1","niveau 2","niveau 3","niveau 4","niveau 5","niveau 6"]
    coo = [(140,170),(90,320),(140,520),(820,170),(870,320),(820,520)]
    j = 0
    font = pygame.font.Font('Polices/SWCrawlBody.ttf', 20)
    for i in mots:
        titre = font.render(mots[j], 0, WHITE)
        fenetre.blit(titre,coo[j])
        j = j+1
    boucle = 4
    for i in range(0,6):
        if i<3 and réussite[clic][i]==1:
            fenetre.blit(réu,(coo[i][0]-40, coo[i][1]-20))
        if i>=3 and réussite[clic][i]==1:
            fenetre.blit(réu,(coo[i][0]+70, coo[i][1]-20))
    pygame.display.flip()
    if boucle == 4:
        claque = zone_traitement(coco)
        if claque == -1:
            boucle = 3
        else:
            compt = 3
            boucle = 0
    if len(ordonnance)>=1:
        for i in range (0,len(ordonnance)):
            del ordonnance[0]
    return(boucle,réussite,ordonnance,compt,claque)

#----------implémentation des classes pour l'évolution du jeu----------#
def implement(classe,classe2,classe3,claque,dif,ennemi,ennemi2,ennemi3,vie_plus,attaque_plus,bouclier_plus):
    classe.life = classe.life + vie_plus
    classe2.life = classe2.life + vie_plus
    classe3.life = classe3.life + vie_plus
    classe.bouclier = classe.bouclier + bouclier_plus
    classe2.bouclier = classe2.bouclier + bouclier_plus
    classe3.bouclier = classe3.bouclier + bouclier_plus
    classe.damage = classe.damage + attaque_plus
    classe2.damage = classe2.damage + attaque_plus
    classe3.damage = classe3.damage + attaque_plus
    if claque == 0:
        if dif == 0:
            ennemi.life = ennemi.life/2
            ennemi2.life = ennemi2.life/2
            ennemi3.life = ennemi3.life/2
    else:
        if dif == 0:
            ennemi.life = ennemi.life + 50*claque
            ennemi2.life = ennemi2.life + 50*claque
            ennemi3.life = ennemi3.life + 50*claque
            ennemi.bouclier = ennemi.bouclier + 10*claque
            ennemi2.bouclier = ennemi2.bouclier + 10*claque
            ennemi3.bouclier = ennemi3.bouclier + 10*claque
            ennemi.damage = ennemi.damage + 20*claque
            ennemi2.damage = ennemi2.damage + 20*claque
            ennemi3.damage = ennemi3.damage + 20*claque
        if dif == 1:
            ennemi.life = ennemi.life + 75*claque
            ennemi2.life = ennemi2.life + 75*claque
            ennemi3.life = ennemi3.life + 75*claque
            ennemi.bouclier = ennemi.bouclier + 20*claque
            ennemi2.bouclier = ennemi2.bouclier + 20*claque
            ennemi3.bouclier = ennemi3.bouclier + 20*claque
            ennemi.damage = ennemi.damage + 25*claque
            ennemi2.damage = ennemi2.damage + 25*claque
            ennemi3.damage = ennemi3.damage + 25*claque
        if dif == 2:
            ennemi.life = ennemi.life + 100*claque
            ennemi2.life = ennemi2.life + 100*claque
            ennemi3.life = ennemi3.life + 100*claque
            ennemi.bouclier = ennemi.bouclier + 30*claque
            ennemi2.bouclier = ennemi2.bouclier + 30*claque
            ennemi3.bouclier = ennemi3.bouclier + 30*claque
            ennemi.damage = ennemi.damage + 40*claque
            ennemi2.damage = ennemi2.damage + 40*claque
            ennemi3.damage = ennemi3.damage + 40*claque
    return(classe,classe2,classe3,ennemi,ennemi2,ennemi3)

#----------Définition Fenètre Jouer----------#
def selec_plan(dif,act,init):
    compt = 1
    chou = 0
    chou2 = 0
    cliche = 0
    postureA = 0
    postureB = 0
    chocolat = -1
    implémentation = 0
    vie_plus = 0
    attaque_plus = 0
    bouclier_plus = 0
    xp = 0
    ordonnance = []
    réussite = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    font4 = pygame.font.Font('Polices/FRABK.TTF', 25)
    while compt != 0:
        if compt ==1 :
            liste12 = [role1,role2,role7,role8,role3,role4,role5,role6]
            liste13 = [0,1,2,3,4,5,6,7]
            planete = [mustafar , jakku , tatoine , coruscant]
            position = [(737,589),(237,89),(600,126),(250,476)]
            shuffle(position)
            
            liste1 = [[237,387,89,239],[250,400,475,625],[600,750,126,276],[737,887,589,739]]
            liste2 = [237,250,600,737]
            
            classe = principal()
            personnage_actuel = choix_role(liste12, liste13)

            if personnage_actuel==-1:
                return(1)
            classe.role(personnage_actuel)
            
            liste_enemi = []
            for p in range (0,len(liste13)):
                if p != classe.rang:
                    liste_enemi.append(liste13[p])
            shuffle(liste_enemi)
            liste_image_enemi = []
            liste_ordre_ennemi = []
            x = 0
            while x<4:
                w = randint(0,len(liste_enemi)-1)
                valeur = liste_enemi[w]
                if (valeur<4 and classe.rang>=4) or (valeur>4 and classe.rang<4): 
                    liste_image_enemi.append(liste12[valeur])
                    liste_ordre_ennemi.append(valeur)
                    x = x+1
            if classe == 0:
                return(1)
            compt = 2

        if compt ==2:
            deg = 0
            coup_don = 0
            couplage = 0
            classe.role(personnage_actuel)
            classe.name_type()
            plancement_partie(position,classe,xp,font4)
            boucle = 1
            while boucle !=0:
                if boucle == 1:
                    choix = 1
                    while choix == 1:
                        choix = page_bouge(liste1,liste2,act,0)
                        if choix == -1:
                            return(1)
                    for i in range(0,4):
                        if position[i][0]==choix:
                            clic = i
                    x=position[clic][0]
                    y=position[clic][1]
                    utilisation = planete[clic]
                    utilisation,classe,boucle,a = mise_en_place_partie(boucle,font4,x,y,positionnement,utilisation,classe,liste_image_enemi,clic,réussite,act)

                if boucle ==3:
                    if act == 0:
                        reglage2(utilisation,a[3],background,planete,position,clic,position[clic],a[0],classe,xp)
                        boucle = 1
                    if act == 1:
                        utilisation = pygame.transform.scale(utilisation,(150,150))
                        boucle = 0
                        compt = 2
                    plaque_quitte = pygame.transform.scale(zone,(170,30))
                    fenetre.blit(plaque_quitte,(850,10))
                    titre2 = font4.render("Quitter la partie", 0, YELLOW)
                    fenetre.blit(titre2,(850,10))
                    pygame.display.flip()
                if boucle ==2:
                    boucle,réussite,ordonnance,compt,claque = placement_planete_grande(boucle,réussite,ordonnance,clic,compt)
        if compt == 3:
            car = 0
            personalité_un = pygame.image.load(classe.image).convert_alpha()
            personalité_deux = pygame.image.load(classe.image2).convert_alpha()
            personalité_trois = pygame.image.load(classe.image3).convert_alpha()
            liste_map_combat = [map3,map2,map4,map1]
            niveau_actuel = liste_map_combat[clic]
            fenetre.blit(niveau_actuel,(0,0))
            plaque_choix = pygame.transform.scale(zone,(924,568))
            fenetre.blit(plaque_choix,(50,100))
            titre = font4.render("Choix des personnages", 0, YELLOW)
            fenetre.blit(titre,(395,110))
            titre2 = font4.render("lancer la partie", 0, YELLOW)
            fenetre.blit(titre2,(435,618))
            
            listener = [157,457,757]
            listener2=[personalité_un,personalité_deux,personalité_trois]
            for i in range (0,len(listener)):
                fenetre.blit(listener2[i],(listener[i],309))
            
            niveaunum = ["0","1","2","3"]
            
            ze = 1
            fontnum = pygame.font.Font('Polices/FRABK.TTF', 22)
            titrenum = fontnum.render(niveaunum[cliche], 0, YELLOW)
            titrenumbis = fontnum.render("/", 0, YELLOW)
            titrenum2 = fontnum.render(niveaunum[classe.num], 0, YELLOW)
            if classe.niveau<5:
                titrenummaj = fontnum.render("Disponible au niveau 5", 0, YELLOW)
                fenetre.blit(titrenummaj,(407,270))
                fenetre.blit(gris,(457,309))
            if classe.niveau<10:
                titrenummaj2 = fontnum.render("Disponible au niveau 10", 0, YELLOW)
                fenetre.blit(titrenummaj2,(707,270))
                fenetre.blit(gris,(757,309))

            fenetre.blit(titrenum,(487,530))
            fenetre.blit(titrenumbis,(500,530))
            fenetre.blit(titrenum2,(513,530))
            
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if cliche == classe.num:
                        if x>435 and x<600 and y>618 and y<648:
                            ze = 2
                            compt = 4 
                    if x>157 and x<268 and y>309 and y<459:
                        if cliche<classe.num:
                            ordonnance.append(0)
                            cliche = cliche + 1
                    if classe.niveau>=5:
                        if x>457 and x<568 and y>309 and y<459:
                            if cliche<classe.num:
                                ordonnance.append(1)
                                cliche = cliche + 1
                    if classe.niveau>=10:
                        if x>757 and x<868 and y>309 and y<459:
                            if cliche<classe.num:
                                ordonnance.append(2)
                                cliche = cliche + 1
            ennemi = principal()
            ennemi.role(liste_ordre_ennemi[clic])
            
            classe2 = principal()
            classe2.role(personnage_actuel)
            classe3 = principal()
            classe3.role(personnage_actuel)
            ennemi2 = principal()
            ennemi2.role(liste_ordre_ennemi[clic])
            ennemi3 = principal()
            ennemi3.role(liste_ordre_ennemi[clic])
            
            amigo = [classe,classe2,classe3]
            pas_amigo = [ennemi,ennemi2,ennemi3]
            
        if compt == 4:
            if implémentation == 0:
                classe,classe2,classe3,ennemi,ennemi2,ennemi3 = implement(classe,classe2,classe3,claque,dif,ennemi,ennemi2,ennemi3,vie_plus,attaque_plus,bouclier_plus)
                implémentation = 1
            cliche = 0          
            fenetre.blit(niveau_actuel,(0,0))
            plaque_titre = pygame.transform.scale(zone,(400,50))
            fenetre.blit(plaque_titre,(312,100))
            font5 = pygame.font.Font('Polices/FRABK.TTF', 48)
            titre = font5.render("Phase De Combat !", 0, YELLOW)
            fenetre.blit(titre,(315,100))
            
            plaque_info = pygame.transform.scale(zone,(200,40))
            fenetre.blit(plaque_info,(156,300))
            fenetre.blit(plaque_info,(668,300))
            font6 = pygame.font.Font('Polices/FRABK.TTF', 30)
            titre1 = font6.render("Ton équipe", 0, YELLOW)
            titre2 = font6.render("L'ennemi", 0, YELLOW)
            fenetre.blit(titre1,(186,300))
            fenetre.blit(titre2,(708,300))

            placement1 = classe.post
            placement2 = ennemi.post
            
            if classe.niveau<7:
                personalité_un_bis = pygame.image.load(ennemi.image).convert_alpha()
                act = 0
            if classe.niveau>=7 and classe.niveau<14:
                personalité_un_bis = pygame.image.load(ennemi.image2).convert_alpha()
                act = 1
            if classe.niveau>=14 :
                personalité_un_bis = pygame.image.load(ennemi.image3).convert_alpha()
                act = 2
            personalité_un_bis = pygame.transform.flip(personalité_un_bis, True, False)
            
            listage = [[(10,700),(150,650),(290,600),(584,600),(724,650),(864,700)],[(320,470),(180,520),(40,570)],[(594,470),(734,520),(874,570)]]
            listage2 = [plateau,ordonnance,personalité_un_bis]

            for i in range (0,len(listage)):
                for j in range (0,len(listage[i])):
                    if (i==1):
                        if placement1[j]==1 and j<len(ordonnance):
                            fenetre.blit(listener2[listage2[i][j]],listage[i][j])
                        else:
                            None
                    elif (i==2):
                        if placement2[j]==1:
                            fenetre.blit(listage2[i],listage[i][j])
                    else:
                        fenetre.blit(listage2[i],listage[i][j])
            pygame.display.update()
            compt = 5
            
        if compt == 5:
            x2 = True
            fontlife = pygame.font.Font('Polices/FRABK.TTF', 15)
            if chou !=0 and chocolat==0:
                fenetre.blit(select,chou)
                titrevie1 = fontlife.render("vie : "+ str(amigo[postureA].life), 0, Red)
                titrebouclier1 = fontlife.render("bouclier : "+ str(amigo[postureA].bouclier), 0, Red)
                titreattaque1 = fontlife.render("attaque : "+ str(amigo[postureA].damage), 0, Red)
                fenetre.blit(titrevie1,(chou[0],chou[1]-45))
                fenetre.blit(titrebouclier1,(chou[0],chou[1]-30))
                fenetre.blit(titreattaque1,(chou[0],chou[1]-15))
            if  chou2 !=0 and chocolat==0:
                fenetre.blit(select2,chou2)
                titrevie2 = fontlife.render("vie : "+ str(pas_amigo[postureB].life), 0, Red)
                titrebouclier2 = fontlife.render("bouclier : "+ str(pas_amigo[postureB].bouclier), 0, Red)
                titreattaque2 = fontlife.render("attaque : "+ str(pas_amigo[postureB].damage), 0, Red)
                fenetre.blit(titrevie2,(chou2[0],chou2[1]-45))
                fenetre.blit(titrebouclier2,(chou2[0],chou2[1]-30))
                fenetre.blit(titreattaque2,(chou2[0],chou2[1]-15))
            if chou !=0 and chou2 !=0 and chocolat==0:
                fenetre.blit(plaque_info,(412,700))
                fontbouton = pygame.font.Font('Polices/FRABK.TTF', 34)
                titrelabel = fontbouton.render("> Attaquez ! <", 0, YELLOW)
                fenetre.blit(titrelabel,(412,700))
            pygame.display.update()
            while x2 == True:
                fontperte = pygame.font.Font('Polices/FRABK.TTF', 30)
                
                if chocolat == -1:
                    fontbouton = pygame.font.Font('Polices/FRABK.TTF', 50)
                    titrelabel = fontbouton.render("> Votre tour de jeu <", 0, Red)
                    fenetre.blit(titrelabel,(300,190))
                    
                if chocolat == 2:
                    for i in range(0,3):
                         if pas_amigo[i].life == 0:
                             placement2[i] = 0
                    if placement2 != [0,0,0]:
                        fontbouton = pygame.font.Font('Polices/FRABK.TTF', 50)
                        titrelabel = fontbouton.render("> Tour de jeu de l'ennemi <", 0, Red)
                        fenetre.blit(titrelabel,(230,190))   
                
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        for j in listage[1]:
                            if x>j[0] and x<j[0]+111 and y>j[1] and y<j[1]+150:
                                for i in range(len(listage[1])):
                                    if listage[1][i][0] == j[0] and placement1[i]==1:
                                        chou = (j[0]+20,j[1]-50)
                                        compt = 4
                                        postureA = i
                                        x2 = False
                        for j in listage[2]:
                            if x>j[0] and x<j[0]+111 and y>j[1] and y<j[1]+150:
                                for i in range(len(listage[2])):
                                    if listage[2][i][0] == j[0] and placement2[i]==1:
                                        chou2 = (j[0]+45,j[1]-50)
                                        compt = 4
                                        postureB = i
                                        x2 = False
                        
                        if chocolat == 0:
                            if x>412 and x<612 and y>700 and y<740:
                                pas_amigo[postureB].blessure(amigo[postureA].damage)
                                perte1 = fontperte.render("-"+ str(amigo[postureA].damage), 0, Red)
                                coup_don = coup_don + amigo[postureA].damage
                                fenetre.blit(perte1,(chou2[0]+60,chou2[1]+60))
                                compt = 4
                                x2 = False
                                sontir = amigo[postureA].son(ordonnance[postureA])
                                if sontir ==1:
                                    sontir2 = pygame.mixer.Sound("Musiques/sabre.wav")
                                if sontir == 2:
                                    sontir2 = pygame.mixer.Sound("Musiques/pistolet.wav")
                                if sontir == 3:
                                    sontir2 = pygame.mixer.Sound("Musiques/force.wav")
                                sontir2.set_volume(init)
                                sontir2.play()
                                dynodio = amigo[postureA].atome[act]
                                for i in range(0,7):
                                    fenetre.blit(niveau_actuel,(0,0))
                                    fenetre.blit(perte1,(chou2[0]+60,chou2[1]+60))
                                    steel = pygame.image.load("Images/Action/" + dynodio + "/" + str(int(i+1)) + ".png").convert_alpha()
                                    fenetre.blit(steel,(chou[0]-20,chou[1]+50))
                                    fenetre.blit(listage2[2],listage[2][postureB])
                                    pygame.time.delay(100)
                                    pygame.display.update()
                                pygame.display.update()
                                pygame.time.delay(500)
                                chocolat = 1
                                couplage = couplage + 1
                                
                if placement1 == [0,0,0]:
                    win = 0
                    compt = 6
                    x2 = False
                    chocolat = 4
                    
                if placement2 == [0,0,0]:
                    win = 1
                    compt = 6
                    x2 = False
                    chocolat = 4
                               
                if chocolat == 3:
                    lot1 = []
                    lot2 = []
                    if (pas_amigo[postureB].life==0):
                        placement2[postureB] = 0
                    for a in range(0,3):
                        if placement1[a] == 1:
                            lot1.append(a)
                        if placement2[a] == 1:
                            lot2.append(a)
                    shuffle(lot2)
                    loterie = [[280,500],[140,550],[0,600]]
                    loterie2 = [(594,470),(734,520),(874,570)]
                    if car == 1:
                        max = 10000
                        for i in lot1:
                            if (amigo[i].life+amigo[i].bouclier)<max:
                                max = amigo[i].life
                                passenger = i
                        if len(lot2)!=0 and len(lot1)!=0 and placement1!=[0,0,0]:
                            amigo[lot1[passenger]].blessure(pas_amigo[lot2[0]].damage)
                            ## finir trouver erreur out of range
                            ## mettre changement perso et son (tir et son jeu)
                            perte2 = fontperte.render("-"+ str(pas_amigo[lot2[0]].damage), 0, Red)
                            fenetre.blit(perte2,(loterie[lot1[passenger]][0],loterie[lot1[passenger]][1]))
                            fenetre.blit(select2,(loterie2[lot2[0]][0]+45,loterie2[lot2[0]][1]-50))
                            deg = deg + pas_amigo[lot2[0]].damage
                            if (amigo[lot1[passenger]].life==0):
                                placement1[lot1[passenger]] = 0
                            
                    if car == 0:
                        shuffle(lot1)
                        if len(lot2)!=0 and len(lot1)!=0:
                            amigo[lot1[0]].blessure(pas_amigo[lot2[0]].damage)
                            perte2 = fontperte.render("-"+ str(pas_amigo[lot2[0]].damage), 0, Red)
                            fenetre.blit(perte2,(loterie[lot1[0]][0],loterie[lot1[0]][1]))
                            fenetre.blit(select2,(loterie2[lot2[0]][0]+45,loterie2[lot2[0]][1]-50))
                            deg = deg + pas_amigo[lot2[0]].damage
                        if (amigo[lot1[0]].life==0):
                            placement1[lot1[0]] = 0
                    chou = 0
                    chou2 = 0
                    chocolat = -2
                    pygame.display.update()
                    sontir = pas_amigo[lot2[0]].son(act)
                    if sontir ==1:
                        sontir2 = pygame.mixer.Sound("Musiques/sabre.wav")
                    if sontir == 2:
                        sontir2 = pygame.mixer.Sound("Musiques/pistolet.wav")
                    if sontir == 3:
                        sontir2 = pygame.mixer.Sound("Musiques/force.wav")
                    sontir2.set_volume(init)
                    sontir2.play()
                    dynodio = pas_amigo[lot2[0]].atome[act]
                    for i in range(0,7):
                        fenetre.blit(niveau_actuel,(0,0))
                        steel = pygame.image.load("Images/Action/" + dynodio + "/" + str(int(i+1)) + ".png").convert_alpha()
                        steel = pygame.transform.flip(steel, True, False)
                        fenetre.blit(steel,(listage[2][lot2[0]]))
                        if car == 1:
                            fenetre.blit(perte2,(loterie[lot1[passenger]][0],loterie[lot1[passenger]][1]))
                            fenetre.blit(select2,(loterie2[lot2[0]][0]+45,loterie2[lot2[0]][1]-50))
                            
                            fenetre.blit(listener2[listage2[1][passenger]],(listage[1][lot1[passenger]]))
                        if car == 0:
                            fenetre.blit(perte2,(loterie[lot1[0]][0],loterie[lot1[0]][1]))
                            fenetre.blit(select2,(loterie2[lot2[0]][0]+45,loterie2[lot2[0]][1]-50))
                            fenetre.blit(listener2[listage2[1][lot2[0]]],listage[1][lot2[0]])
                            ##soucis out of range en possible
                        pygame.time.delay(100)
                        pygame.display.update()
                    if car == 0:
                        car = car + 1
                    pygame.time.delay(500)
                    compt = 4
                    x2 = False
                    del lot1
                    del lot2

                if (chocolat== -1) or (chocolat == 2):
                    pygame.display.update()
                    pygame.time.delay(2000)
                    compt = 4
                    x2 = False
            if chocolat!=0:
                chocolat = chocolat + 1
        
        if compt == 6:
            car = 0
            fenetre.blit(niveau_actuel,(0,0))
            fenetre.blit(plaque_choix,(50,100))
            if win ==1:
                titre = font4.render("Victoire", 0, YELLOW)
                fenetre.blit(titre,(500,110))
                réussite[clic][claque] = 1

                titre2 = font4.render("Bonus :", 0, YELLOW)
                fenetre.blit(titre2,(200,368))
                titre2 = font4.render("Gain de vie : " +str(2), 0, Red)
                fenetre.blit(titre2,(235,393))
                titre2 = font4.render("Gain d'XP : " +str(100), 0, Red)
                fenetre.blit(titre2,(235,418))
                vie_plus = vie_plus + 2
                xp = xp +100

            else:
                titre = font4.render("Défaite", 0, YELLOW)
                fenetre.blit(titre,(500,110))
            titre2 = font4.render("Récapitulatif :", 0, YELLOW)
            fenetre.blit(titre2,(200,268))
            titre2 = font4.render("Nombre de tour(s) : " +str(couplage), 0, Red)
            fenetre.blit(titre2,(235,293))
            titre2 = font4.render("Nombre de dégats subits : " +str(deg), 0, Red)
            fenetre.blit(titre2,(235,318))
            titre2 = font4.render("Nombre de dégats infligés : " +str(coup_don), 0, Red)
            fenetre.blit(titre2,(235,343))

            if xp >= classe.rekt[classe.niveau]:
                classe.niveau = classe.niveau + 1
                bouclier_plus = bouclier_plus + 2
                attaque_plus = attaque_plus + 5
                xp = 0
                titre2 = font4.render("Passage au niveau " +str(classe.niveau) + "!", 0, YELLOW)
                fenetre.blit(titre2,(200,468))

            titre2 = font4.render("Revenir à la carte", 0, YELLOW)
            fenetre.blit(titre2,(435,618))
            pygame.display.update()
            x3 = True
            
            while x3 == True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if x>435 and x<620 and y>618 and y<648:
                            compt = 2
                            x3 = False
                            chocolat = -1
                            chou2 = 0
                            implémentation = 0
                            if réussite == [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]:
                                compt = 7
        if compt == 7:
                crédit = [["création du design","Pierre Maurand","Pierre Bihel","Robin Gallis"],["développement","Pierre Maurand","Robin Gallis"],["scénario","Pierre Bihel","Robin Gallis"],["animation","Pierre Maurand","Pierre Bihel","Robin Gallis"],["direction","Pierre Maurand","Pierre Bihel","Robin Gallis"],["imagerie","Pierre Bihel"],["Copyrights", "STAR WARS"]]
                position_init = 400
                position_init2 = 300
                ypos = 25
                fenetre.blit(fond, (0,0))
                for i in range(0,len(crédit)):
                    for j in range(0,len(crédit[i])):
                        if j == 0:
                            titre2 = font4.render(crédit[i][j], 0, WHITE)
                            fenetre.blit(titre2,(position_init,ypos))
                        if j != 0:
                            font51 = pygame.font.Font('Polices/FRABK.TTF', 18)
                            titre2 = font51.render(crédit[i][j], 0, WHITE)
                            fenetre.blit(titre2,(position_init2,ypos))
                        if j != (len(crédit[i])-1) and j != 0:
                            ypos = ypos + 20
                        if j == (len(crédit[i])-1) or j == 0:
                            ypos = ypos + 40
                pygame.display.flip()
                pygame.time.delay(10000)
                return(1)

#----------Définition Fenètre d'Option----------#
def option(difficul,al1,al2,init,act):
    x1 = 0
    while x1==0:
        fenetre.blit(optionnel,(0,0))
        txt = font.render("Options", 0, YELL)
        txt = pygame.transform.scale(txt,(300,100))
        fenetre.blit(txt,(350,30))
        fontbouton = pygame.font.Font('Polices/FRABK.TTF', 20)
        fontniveau = pygame.font.Font('Polices/FRABK.TTF', 12)
        
        titreson = fontbouton.render("Son :", 0, YELLOW)
        titrefaible = fontniveau.render("faible", 0, YELLOW)
        titrefort = fontniveau.render("fort", 0, YELLOW)
        fenetre.blit(titreson,(220,252))
        fenetre.blit(titrefaible,(300,282))
        fenetre.blit(titrefort,(944,282))
        fenetre.blit(sonore,(300,250))
        
        selecteur = pygame.transform.scale(select2,(28,20))
        
        plaque_bouton = pygame.transform.scale(zone,(105,25))
        fenetre.blit(plaque_bouton,(445,650))
        titrebouton = fontbouton.render("enregistrer", 0, YELLOW)
        fenetre.blit(titrebouton,(450,650))
        
        plaque_select = pygame.transform.scale(zone,(6,25))
        
        liste1 = [(288,230),(369,230),(451,230),(535,230),(617,230),(702,230),(784,230),(866,230),(946,230)]
        liste2 = [(298,252),(379,252),(461,252),(545,252),(627,252),(712,252),(794,252),(876,252),(958,252)]
        
        
        fenetre.blit(selecteur,liste1[al1])
        fenetre.blit(plaque_select,liste2[al2])
        
        titredifficulté = fontbouton.render("Niveau de difficulté :", 0, YELLOW)
        fenetre.blit(titredifficulté,(220,380))
        
        plaque_diffic = pygame.transform.scale(zone,(68,25))
        fenetre.blit(plaque_diffic,(413,380))
        fenetre.blit(plaque_diffic,(593,380))
        fenetre.blit(plaque_diffic,(773,380))
        
        if difficul == 0:
            fenetre.blit(selecteur,(435,350))
        if difficul == 1:
            fenetre.blit(selecteur,(612,350))
        if difficul == 2:
            fenetre.blit(selecteur,(790,350))
        
        titrefacile = fontbouton.render("facile", 0, YELLOW)
        fenetre.blit(titrefacile,(425,380))
        
        titremoyen = fontbouton.render("moyen", 0, YELLOW)
        fenetre.blit(titremoyen,(600,380))
        
        titredifficile = fontbouton.render("difficile", 0, YELLOW)
        fenetre.blit(titredifficile,(775,380))
        
        titredifficulté = fontbouton.render("Animation :", 0, YELLOW)
        fenetre.blit(titredifficulté,(220,508))

        fenetre.blit(plaque_diffic,(413,508))
        fenetre.blit(plaque_diffic,(593,508))

        titrefacile = fontbouton.render("Activé", 0, YELLOW)
        fenetre.blit(titrefacile,(425,508))
        
        titremoyen = fontbouton.render("Retiré", 0, YELLOW)
        fenetre.blit(titremoyen,(600,508))

        if act == 0:
            fenetre.blit(selecteur,(435,478))
        if act == 1:
            fenetre.blit(selecteur,(612,478))

        pygame.display.flip()
        y1 = 0
        while y1==0:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x>445 and x<550 and y>650 and y<675:
                        y1 = 1
                        x1 = 1
                    if x>413 and x<481 and y>380 and y<405:
                        y1 = 1
                        difficul = 0
                    if x>593 and x<661 and y>380 and y<405:
                        y1 = 1
                        difficul = 1
                    if x>773 and x<841 and y>380 and y<405:
                        y1 = 1
                        difficul = 2
                    if x>413 and x<481 and y>508 and y<533:
                        y1 = 1
                        act = 0
                    if x>593 and x<661 and y>508 and y<533:
                        y1 = 1
                        act = 1
                    for i in range(0,len(liste1)):
                        if x>liste2[i][0]-10 and x<liste2[i][0]+16 and y>liste2[i][1] and y<liste2[i][1]+25:
                            init = 0.1 + 0.1*i
                            al1 = i
                            al2 = i
                            y1 = 1
    return(1,difficul,init,al1,al2,act)

#----------Définition Du Positionement Vaisseau----------#
def mouvement_vaisseau(position):
    fenetre.blit(fond, position, position)
    position = position.move(1, 0)
    fenetre.blit(vaisseau, position)
    fenetre.blit(titre, (312,100))
    pygame.display.update()
    pygame.time.delay(1)
    return(position)

#----------Définition Du Menu----------#
def ecran_menu(act):
    fenetre.blit(fond, (0,0))
    fenetre.blit(titre, (312,100))
    fenetre.blit(zone, (112,500))
    fenetre.blit(jouer, (217,590))
    fenetre.blit(options, (442,586))
    fenetre.blit(quitter, (680,585))
    position = vaisseau.get_rect()
    position = position.move(-200,300)
    fenetre.blit(vaisseau, position)
    pygame.display.flip()
    pygame.time.delay(100)
    x = 0
    final = 1
    while True:
        liste1 = [[650,919,500,708],[112,381,500,708],[381,650,500,708]]
        liste2 = [0,3,2]
        final = page_bouge(liste1,liste2,act,1)
        if act == 0:
            if x<1300 and final==1:
                position = mouvement_vaisseau(position)
                x=x+1
        if final == 0:
            return(0)
        if final == 2:
            return(2)
        if final == 3:
            return(3)
        if final == -7:
            return(1)

#----------Définition De Positionnement Du Texte Du Générique----------#
def positionnement(label, position):
    fenetre.blit(fenetre, position, position)
    position = position.move(0, -1)
    fenetre.blit(label,position)

#----------Définition De l'Ensemble Du Générique----------#
def generique():
    titre = font3.render("Il  y  a  bien  longtemps , dans", 0, BLUE)
    titre_suite = font3.render("une galaxie très lointaine ...", 0, BLUE)
    fenetre.blit(titre,(200,340))
    fenetre.blit(titre_suite,(200,420))
    pygame.display.update()
    pygame.time.delay(5000)
    liste = ["La guerre entre les rebelles et","l'empire est a son apogee.","","Depuis  que  l'empire  a  pour",
    "objectif  de  conquerir  toutes","les planetes de la galaxie , les","rebelles semblent surpasses.","",
    "Mais  ils  ne  sont  pas  encore","accules, leurs ressources les","aiderons durant cette guerre",
    "mythique.","","","","L'empire ou les rebelles , qui","choisirez-vous ?"]
    fenetre.blit(fond, (0,0))
    position = fond.get_rect()
    titre2 = font2.render("Galaxy  conquest", 0, YELLOW)
    titre2 = pygame.transform.scale(titre2,(400,70))
    position_titre = fond.get_rect()
    position_titre = position_titre.move(300,768)
    for y in range (1,1850):
        j = 938
        fenetre.blit(fond, (0,0))
        fenetre.blit(fenetre, position_titre, position_titre)
        position_titre = position_titre.move(0, -1)
        fenetre.blit(titre2,position_titre)
        for i in liste:
            position = position.move(230,j)
            label = font.render(i, 0, YELLOW)
            positionnement(label, position)
            position = position.move(-230,-j)
            j = j+50
        position = position.move(0, -1)
        titre3 = fontsup.render("Espace",0, Red)
        titre4 = fontsup.render("pour passer",0, Red) 
        fenetre.blit(titre3, (920,700))
        fenetre.blit(titre4, (900,720))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return(1)
    return (1)

#----------Définition De l'Ordre Des Fonctions Principales----------#
def main(difficulté,def1,def2,init,act):
    son.set_volume(init)
    son.play(loops=-1, maxtime=0, fade_ms=100)
    ordre = generique()
    son.stop()
    while (ordre!=0):
        son.set_volume(init)
        sonmenu.set_volume(init)
        if (ordre == 1):
            son.play(loops=-1, maxtime=0)
            ordre = ecran_menu(act)
            son.stop()
        if (ordre == 2):
            ordre, difficulté, init, def1, def2,act = option(difficulté,def1,def2,init,act)
        if (ordre == 3):
            sonmenu.play(loops=-1, maxtime=0, fade_ms=100)
            ordre = selec_plan(difficulté,act,init)
            sonmenu.stop()
    pygame.quit()

#----------Première Vrai Mise En Route----------#
if cool == 0:
    difficulté = 0
    def1 = 1
    def2 = 1
    act = 0
    son_init = 0.2
    main(difficulté,def1,def2,son_init,act)
