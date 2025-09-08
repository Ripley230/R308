def max_liste(vals: list[float]):
    if not vals:
        raise ValueError("La liste ne doit pas être vide")
    return max(vals)

ma_liste = [10 , 15 , 12.5, 100.2]
print(max_liste(ma_liste))

