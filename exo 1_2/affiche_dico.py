def affiche_dico(d: dict, prefixe: str) -> None:
    for k, v in d.items():
        print(f"{prefixe} {k}: {v}")

mon_dictionaire = {"nom" : "albert", "prenom" : "arnauld", "travail" : "professeur"}
prefixe_texte = "Info ->"
print(affiche_dico(mon_dictionaire, prefixe_texte))