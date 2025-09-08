def est_superieur(val: float, seuil: float = 10) -> bool :
    if val > seuil:
        return True
    else:
        return False

print(est_superieur(5))