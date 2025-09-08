def count_inf(vals: list[float], seuil: float = 3):
    return sum(1 for v in vals if v < seuil)

ma_liste = [10, 25, 140, 100, 2.5, 1]
print(count_inf(ma_liste))