class velo :

    def __init__ ( self , marque : str, taille_pneu : int, couleur : str, nb_vitesse : int):
        self.marque = marque
        self.taille_penu = taille_pneu
        self.couleur = couleur
        self.nb_vitesse = nb_vitesse
        self.vitesse_initiale = 1

    def gear_up(self) -> int:
        if self.vitesse_initiale < self.nb_vitesse:
            self.vitesse_initiale += 1
        return self.vitesse_initiale

    def gear_down(self) -> int:
        if self.vitesse_initiale > 1:
            self.vitesse_initiale -=1
        return self.vitesse_initiale

if __name__ == "__main__":
    mon_velo = velo("Git-Bike", 26, "rouge", 7)
    print(f"Vitesse initiale : {mon_velo.vitesse_initiale}")
    print(f"Augmentation de la vitesse : {mon_velo.gear_up()}")
    print(f"Diminution de la vitesse : {mon_velo.gear_down()}")