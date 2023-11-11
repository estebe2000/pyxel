import pyxel

# Variables de la balle
position_balle = [80, 60]
vitesse_balle = [2, 2]

# Variables de la raquette
position_raquette = [10, 60]
largeur_raquette = 2
hauteur_raquette = 20
vitesse_raquette = 2

# Variable de score
score = 0

# Variable pour afficher le message "OUT"
afficher_out = False

def init_game():
    pyxel.init(160, 120, title="Pong")
    pyxel.run(update, draw)

def update():
    global position_balle, vitesse_balle, score, afficher_out

    # Mise à jour de la position de la balle
    position_balle[0] += vitesse_balle[0]
    position_balle[1] += vitesse_balle[1]

    # Rebond de la balle sur les bords supérieur et inférieur
    if position_balle[1] <= 0 or position_balle[1] >= pyxel.height:
        vitesse_balle[1] *= -1

    # Contrôles de la raquette
    if pyxel.btn(pyxel.KEY_Z) and position_raquette[1] > 0:
        position_raquette[1] -= vitesse_raquette
    if pyxel.btn(pyxel.KEY_S) and position_raquette[1] < pyxel.height - hauteur_raquette:
        position_raquette[1] += vitesse_raquette

    # Collision de la balle avec la raquette
    if (position_raquette[0] <= position_balle[0] <= position_raquette[0] + largeur_raquette and
        position_raquette[1] <= position_balle[1] <= position_raquette[1] + hauteur_raquette):
        vitesse_balle[0] *= -1

    # Balle touche le mur de gauche
    if position_balle[0] <= 0:
        score += 1
        afficher_out = True
        reset_balle()

def reset_balle():
    global position_balle, vitesse_balle
    position_balle = [80, 60]
    vitesse_balle = [2, 2]

def draw():
    pyxel.cls(0)
    pyxel.circ(position_balle[0], position_balle[1], 2, 7)
    pyxel.rect(position_raquette[0], position_raquette[1], largeur_raquette, hauteur_raquette, 7)

    # Afficher le score
    pyxel.text(5, 5, f"Score: {score}", 7)

    # Afficher le message "OUT"
    if afficher_out:
        pyxel.text(70, 60, "OUT!", 8)

init_game()
