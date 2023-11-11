import pyxel

class Menu:
    def __init__(self):
        pyxel.init(160, 120, title="Menu du Jeu")
        pyxel.sound(0).set("c3e2g3c4", "p", "7", "vffn", 25)

        self.option = 0
        self.options = ["Start", "Infos"]

        pyxel.play(0, 0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.option = (self.option + 1) % len(self.options)
        elif pyxel.btnp(pyxel.KEY_UP):
            self.option = (self.option - 1) % len(self.options)

        if pyxel.btnp(pyxel.KEY_RETURN):  # Utilisation de KEY_RETURN pour la touche Entrée
            self.select_option()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(70, 55, "Menu du Jeu", pyxel.frame_count % 16)
        for i, option in enumerate(self.options):
            color = 7 if i == self.option else 8
            pyxel.text(75, 70 + 10 * i, option, color)

    def select_option(self):
        selected_option = self.options[self.option]
        if selected_option == "Start":
            # Commencer le jeu
            print("Commencer le jeu")
        elif selected_option == "Infos":
            # Afficher les informations
            print("Afficher les informations")

Menu()
