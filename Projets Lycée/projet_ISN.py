import pygame
import time
import random

pygame.init()



surfaceW = 1280 #Dimension de la fenêtre / Largeur
surfaceH = 720 #Dimension de la fenêtre / Longueur

class Menu :
    """ Création et gestion des boutons d'un menu """
    def __init__(self, application, *groupes) :
        self.couleurs = dict(
            normal=(250, 250, 250),
            survol=(0, 200,0 ),
        )
        font = pygame.font.SysFont('Helvetica', 24, bold=True)
        # noms des menus et commandes associées
        items = (
            ('JOUER', application.quitter),
            #('QUITTER', application.jeu)
        )
        x = surfaceW/2
        y = surfaceH/2
        self._boutons = []
        for texte, cmd in items :
            mb = MenuBouton(
                texte,
                self.couleurs['normal'],
                font,
                x,
                y,
                200,
                50,
                cmd
            )
            self._boutons.append(mb)
            y += 120
            for groupe in groupes :
                groupe.add(mb)

    def update(self, events) :
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self._boutons :
            # Si le pointeur souris est au-dessus d'un bouton
            if bouton.rect.collidepoint(*posPointeur) :
                # Changement du curseur par un quelconque
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # Changement de la couleur du bouton
                bouton.dessiner(self.couleurs['survol'])
                # Si le clic gauche a été pressé
                if clicGauche :
                    # Appel de la fonction du bouton
                    bouton.executerCommande()
                break
            else :
                # Le pointeur n'est pas au-dessus du bouton
                bouton.dessiner(self.couleurs['normal'])
        else :
            # Le pointeur n'est pas au-dessus d'un des boutons
            # initialisation au pointeur par défaut
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def detruire(self) :
        pygame.mouse.set_cursor(*pygame.cursors.arrow) # initialisation du pointeur



class MenuBouton(pygame.sprite.Sprite) :
    """ Création d'un simple bouton rectangulaire """
    def __init__(self, texte, couleur, font, x, y, largeur, hauteur, commande) :
        super().__init__()
        self._commande = commande

        self.image = pygame.Surface((largeur, hauteur))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.texte = font.render(texte, True, (0, 0, 0))
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (largeur/2, hauteur/2)

        self.dessiner(couleur)

    def dessiner(self, couleur) :
        self.image.fill(couleur)
        self.image.blit(self.texte, self.rectTexte)

    def executerCommande(self) :
        # Appel de la commande du bouton
        self._commande()



class Jeu :
    """ Simulacre de l'interface du jeu """
    def __init__(self, jeu, *groupes) :
        self._fenetre = jeu.fenetre
        jeu.fond = (255, 255, 255)



    def update(self, events) :
        self._fenetre.blit(self.texte, self.rectTexte)
        for event in events :
            if event.type == self._CLIGNOTER :
                self.creerTexte()
                break

    def detruire(self) :
        pygame.time.set_timer(self._CLIGNOTER, 0) # désactivation du timer


class Application :
    """ Classe maîtresse gérant les différentes interfaces du jeu """
    def __init__(self) :
        pygame.init()
        pygame.display.set_caption("MENU DE JEU")

        self.fond = (150,)*3

        self.fenetre = pygame.display.set_mode((surfaceW,surfaceH))
        # Groupe de sprites utilisé pour l'affichage
        self.groupeGlobal = pygame.sprite.Group()
        self.statut = True

    def _initialiser(self) :
        try:
            self.ecran.detruire()
            # Suppression de tous les sprites du groupe
            self.groupeGlobal.empty()
        except AttributeError:
            pass

    def menu(self) :
        # Affichage du menu
        self._initialiser()
        self.ecran = Menu(self, self.groupeGlobal)

    def jeu(self) :
        # Affichage du jeu
        self._initialiser()
        self.ecran = Jeu(self, self.groupeGlobal)

    def quitter(self) :
        self.statut = False


    def update(self) :
        events = pygame.event.get()

        for event in events :
            if event.type == pygame.QUIT :
                self.quitter()
                return

        self.fenetre.fill(self.fond)
        self.ecran.update(events)
        self.groupeGlobal.update()
        self.groupeGlobal.draw(self.fenetre)
        pygame.display.update()



app = Application()
app.menu()

clock = pygame.time.Clock()

while app.statut :
    app.update()
    clock.tick(30)



largeur = 720
longueur = 1280

screen = pygame.display.set_mode((longueur, largeur))
ecran_titre = pygame.display.set_caption("nom du jeu")

# chargement de quelques éléments du jeu
Bonus1 = pygame.image.load("teh.png")
perso = pygame.image.load("Img_D.png")
Bonus2 = pygame.image.load("piece.png")
marron = (180, 75, 0)
A= (255, 255, 255)

perso_x = 50
perso_y = 519
screen.blit(perso, (perso_x, perso_y))

# défintion de la dimension des plates-formes
platf_longeur = 100
platf_largeur = 35
# définiton de la police et de la taille du texte affiché sur l'écran
font = pygame.font.SysFont("Arial", 30, bold=False, italic=False)
screen.fill(A)
k = 1  #constante de déplacement
v = 1 # constante de vitesse
keys = pygame.key.get_pressed()
pygame.display.flip()

# attribution des coordonnées de base des bonus/objets
Bonus1_x = 670
Bonus1_y = 200
Bonus2_x = 610
Bonus2_y = 428

# gestion du temps
secondes = clock.tick()/1000.0 #écoulement du temps en millisecondes
temps = 60

score = 0
lose_x = 100000 # ces grandes valeurs c'est pour éviter que l'on voit les textes avant le moment choisi
lose_y = 100000
End = 5
end_x = 10000
end_y = 10000
score_Tx = 640
score_Ty = 55
Chrono_x = 590
Chrono_y = 25

pygame.display.update()
sortieJeu = False
# Boucle principale
while not sortieJeu:
   score_texte = font.render('score:' + str(score), 1, (0, 0, 0,))
   secondes = clock.tick()/1000.0 # mettre à jour l'horloge, calcul le nombre de millisecondes
   temps -= (secondes)
   Chrono = font.render('temps restant:' + str(temps), 1, (255, 0, 0))
   lose = font.render('Bien joué votre score est de:' +  str(score), 1, (0, 0, 0,))
   Endgame = font.render('fin du jeu dans:' + str(End + temps), 1, (0, 0, 0))

   for event in pygame.event.get():

           if event.type == pygame.QUIT:
               sortieJeu = True
               time.sleep(1)

   keys = pygame.key.get_pressed()

   if keys[pygame.K_SPACE]:

    A = (238, 232, 205)

   elif keys[pygame.K_LEFT] and 0 <perso_x:
       perso_x += -k*v
   elif keys[pygame.K_RIGHT] and perso_x<longueur-(k*5) :
       perso_x += k*v
   elif keys[pygame.K_DOWN] and perso_y<601-75:
       perso_y += k*v
   elif keys[pygame.K_UP] and perso_y>0:
      perso_y += -k*v
   elif keys[pygame.K_ESCAPE]:
      sortieJeu = True
   # défintion des paramètres des bonus/objets
   if perso_x == Bonus1_x and perso_y <= Bonus1_y: # idéalement mettre perso_y == Bonus1_y mais sa marche pas car proportion différent
      A = (127, 255, 212)
   if temps < 0:
      Chrono_x = 10000
      Chrono_y = 10000
      score_Tx = 10000
      score_Ty = 10000
      end_x = longueur/2
      end_y = largeur/2 + 40
      lose_x = longueur/2
      lose_y = largeur/2
   if temps < -5:
      sortieJeu = True
   if (End + temps) < 1: # je fais en sorte que on ne voit plus le texte affiché
      end_x = 10000
      end_y = 10000

   # défintion des paramètres des bonus/objets
   if perso_x == Bonus1_x and perso_y <= Bonus1_y: # idéalement mettre perso_y == Bonus1_y mais sa marche pas car proportion différent
      A = (255,131,250)
      Bonus1_x = round(random.randrange(200, (longueur-200)-perso_x))
      temps -= temps/2
      # fonction de placement aléatoire du bonus sous certaines conditions
   elif perso_x == Bonus2_x and perso_y <= Bonus2_y: # idéalement mettre perso_y == Bonus2_y mais sa marche pas comme si-dessus
      Bonus2_x = round(random.randrange(0, (longueur-200)-perso_x))
      Bonus2_y = round(random.randrange(0, (largeur-200)- perso_y))
      score += 1
      temps += 1

   screen.fill(A)
   plateforme1 = pygame.draw.rect(screen, marron, [600, 485, platf_longeur, platf_largeur ])
   plateforme2 = pygame.draw.rect(screen, marron, [475, 400, platf_longeur, platf_largeur ])
   plateforme3 = pygame.draw.rect(screen, marron, [375, 400, platf_longeur, platf_largeur ])
   plateforme4 = pygame.draw.rect(screen, marron, [275, 500, platf_longeur, platf_largeur ])
   plateforme5 = pygame.draw.rect(screen, marron, [600, 275, platf_longeur, platf_largeur ])
   plateforme6 = pygame.draw.rect(screen, marron, [700, 275, platf_longeur, platf_largeur ])
   plateforme7 = pygame.draw.rect(screen, marron, [800, 400, platf_longeur, platf_largeur ])
   plateforme8 = pygame.draw.rect(screen, marron, [900, 400, platf_longeur, platf_largeur ])
   plateforme9 = pygame.draw.rect(screen, marron, [200, 240, platf_longeur, platf_largeur ])
   plateforme10 = pygame.draw.rect(screen, marron, [400, 240, platf_longeur, platf_largeur])
   screen.blit(Chrono, (Chrono_x, Chrono_y))
   screen.blit(score_texte, (score_Tx, score_Ty))
   screen.blit(lose, (lose_x, lose_y))
   screen.blit(Endgame, (end_x, end_y))
   screen.blit(perso, (perso_x, perso_y))
   screen.blit(Bonus2, (Bonus2_x, Bonus2_y))
   screen.blit(Bonus1, (Bonus1_x, Bonus1_y))
   pygame.display.update()
pygame.quit()
