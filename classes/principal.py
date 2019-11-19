class principal:
    def __init__ (self):
        self.grade = ""
        self.niveau =  1
        self.rang = 0
        self.classement = 0
        self.image = 0
        self.image2 = 0
        self.image3 = 0
        self.num = 0
        self.post = []
        self.life = 0
        self.damage = 0
        self.bouclier = 0
        self.activation = 0
        self.rekt = [0,100,200,400,600,900,1200,1600,2000,2400,2900,3400,3900,4500,5000,5600,6200,6900,7600,8400,9200]
        self.graduation = 0
        self.listeplane1 = ["Planète volcanique des Territoires de la","de la Bordure Extérieure. C'est ici que","Dark Vador affronta son ancien maître","Obi-Wan Kenobi dans un duel, manifestant","ainsi son basculement 'définitif' vers le","Côté Obscur de la Force."]
        self.listeplane2 = ["Planète désertique de la Bordure Extérieure.","La planète est devenue connue pour ses","courses de modules comme la Classique de","Boonta Eve. Les Jawa, un peuple de ferrailleur,","et les Tusken, étaient des espèces","originaires de la planète."]
        self.listeplane3 = ["Planète désertique et insignifiante de la","de la Bordure Intérieure. Elle fut le","théâtre d'un important affrontement entre","l'Empire Galactique et la toute jeune","Nouvelle République."]
        self.listeplane4 = ["Planète au climat tempéré située près du","centre de la Galaxie. La planète est","cosmopolite et entièrement urbanisée, éclairée"," en permanence de jour comme de nuit.","Les océans ont été asséchés depuis bien"," des millénaires à l'époque impériale."]
        self.autotexte = "Elle est maintenant contrôlée par  :"
        self.autotexte2 = "Elle est contrôlée par votre groupe"
        self.liste_action = ""
        self.atome = ""
    
    def son(self,A):
        if A==0:
            return(self.classement.son1[0])
        if A==1:
            return(self.classement.son1[1])
        if A==2:
            return(self.classement.son1[2])

    def blessure (self,degats):
        if ( self.bouclier != 0):
            self.bouclier = self.bouclier - degats
            if(self.bouclier < 0):
                degats = self.bouclier * -1
                self.bouclier = 0
            else:
                degats = 0
        if( degats > 0):
            self.life = self.life - degats
            if(self.life <= 0):
                self.life = 0
                return False
            else:
                return True

    def name_type (self):
            if self.niveau<5:
                self.grade = self.graduation[0]
            if self.niveau>=5 and self.niveau<10:
                self.grade = self.graduation[1]
            if self.niveau>=10 and self.niveau<15:
                self.grade = self.graduation[2]
            if self.niveau>=15:
                self.grade = self.graduation[3]
    
    def role (self,a):
        if a == 0:
            from classes.personnages.jedi import jedi
            self.classement = jedi()
        if a == 1:
            from classes.personnages.rebelle import rebelle
            self.classement = rebelle()
        if a == 2:
            from classes.personnages.commerce import commerce
            self.classement = commerce()
        if a == 3:
            from classes.personnages.wookie import wookie
            self.classement = wookie()
        if a == 4:
            from classes.personnages.Fett import Fett
            self.classement = Fett()
        if a == 5:
            from classes.personnages.stormtrooper import stormtrooper
            self.classement = stormtrooper()
        if a == 6:
            from classes.personnages.droide import droide
            self.classement = droide()
        if a == 7:
            from classes.personnages.sith import sith
            self.classement = sith()
        self.grade = self.classement.grade
        self.rang = self.classement.rang
        self.image = self.classement.image1
        self.image2 = self.classement.image2
        self.image3 = self.classement.image3
        self.num = self.classement.nombre_personnage
        self.post = self.classement.post
        self.life = self.classement.life
        self.damage = self.classement.damage
        self.bouclier = self.classement.bouclier
        self.activation = self.classement.activation
        self.graduation = self.classement.graduation
        self.liste_action = self.classement.plaquer
        self.atome = [self.liste_action + "1",self.liste_action + "2",self.liste_action + "3"]

def cliquable(clic):
    if clic == 1:
        a = 0
        b = 4
        return([a,b])
    if clic == 2:
        a = 4
        b = 8
        return([a,b])
    return(0)

def calculette1(sens,vrai,x,y):
    if sens == 1:
        j = 437
        k = 289
    if sens == -1:
        j = vrai[0]
        k = vrai[1]
        x = 437
        y = 289
    return([j,k,x,y])

def calculette2(j,k,x,y):
    while x!=j:
        if x<j:
            a = 1
            x = x+1
        else:
            a = -1
            x = x-1
        if y<k:
            b = 1
            y = y+1
        else:
            b= - 1
            y = y-1
        return([a,b,x,y])
