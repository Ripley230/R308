#(1)#
class Tasse :
    matiere: str = " céramique "

    def __init__ ( self , couleur : str, contenance : int, marque : str ):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque

#(2)#
    def __str__(self) -> str:
        return (f"la tasse de matière {self.matiere}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance}ml")

#(3)#
    def definir_contenu(self, contenu : str) -> None:
        self.contenu = contenu

#(4)#
    def boire(self) -> None:
        if hasattr(self, "contenu"):
            del self.contenu
        else:
            raise AttributeError("La tasse est vide !!!")

if __name__ == "__main__":
    tasse1 = Tasse("bleu", 50, "duralex")
    print(tasse1)

    tasse1.definir_contenu("café")
    print(f"Contenu de la tasse : {tasse1.contenu}")

    tasse1.boire()
