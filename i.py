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

# Variable pour gérer l'état de pause
en_pause = False

def init_game():
    pyxel.init(160, 120, title="Pong")

    # Configurer les notes de la mélodie
    pyxel.sound(0).set("c3", "p", "3", "n", 10)  # C4
    pyxel.sound(1).set("a2", "p", "3", "n", 10)  # A3
    pyxel.sound(2).set("g2", "p", "3", "n", 10)  # G3

    # Jouer la mélodie au démarrage
    pyxel.play(0, 0)
    pyxel.play(1, 1)
    pyxel.play(2, 2)
    pyxel.play(1, 1)

    pyxel.run(update, draw)

def update():
    global position_balle, vitesse_balle, score, afficher_out, en_pause

    # Si le jeu est en pause, ne pas mettre à jour la position de la balle et de la raquette
    if en_pause:
        if pyxel.btnp(pyxel.KEY_R):
            reset_balle()
            en_pause = False
        return

    # Mise à jour de la position de la balle
    position_balle[0] += vitesse_balle[0]
    position_balle[1] += vitesse_balle[1]

    # Rebond de la balle sur les bords
    if position_balle[1] <= 0 or position_balle[1] >= pyxel.height:
        vitesse_balle[1] *= -1
        pyxel.play(0, 0)  # Jouer le son
    if position_balle[0] >= pyxel.width or position_balle[0] <= 0:
        vitesse_balle[0] *= -1
        pyxel.play(0, 0)  # Jouer le son
        if position_balle[0] <= 0:
            score += 1
            afficher_out = True
            en_pause = True

    # Contrôles de la raquette
    if pyxel.btn(pyxel.KEY_Z) and position_raquette[1] > 0:
        position_raquette[1] -= vitesse_raquette
    if pyxel.btn(pyxel.KEY_S) and position_raquette[1] < pyxel.height - hauteur_raquette:
        position_raquette[1] += vitesse_raquette

    # Collision de la balle avec la raquette
    if (position_raquette[0] <= position_balle[0] <= position_raquette[0] + largeur_raquette and
        position_raquette[1] <= position_balle[1] <= position_raquette[1] + hauteur_raquette):
        vitesse_balle[0] *= -1
        pyxel.play(0, 0)  # Jouer le son

def reset_balle():
    global position_balle, vitesse_balle, afficher_out
    position_balle = [80, 60]
    vitesse_balle = [2, 2]
    afficher_out = False

def draw():
    pyxel.cls(0)
    pyxel.circ(position_balle[0], position_balle[1], 2, 7)
    pyxel.rect(position_raquette[0], position_raquette[1], largeur_raquette, hauteur_raquette, 7)

    # Afficher le score
    pyxel.text(5, 5, f"Score: {score}", 7)

    # Afficher le message "OUT"
    if afficher_out:
        pyxel.text(70, 60, "OUT!", 8)
        pyxel.text(70, 70, "Press 'R' to continue", 8)

init_game()
