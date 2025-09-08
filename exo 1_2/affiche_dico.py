def affiche_dico(a: dict, b: str) -> None:
    for k, v in a.items():
        print(f"{b} -> {k}: {v}")

mon_dictionaire = {"nom" : "albert", "prenom" : "arnauld", "travail" : "professeur"}
prefixe_texte = "Info"
print(affiche_dico(mon_dictionaire, prefixe_texte))