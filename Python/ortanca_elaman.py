def ortanca_eleman(liste):
    liste_sayisi = len(liste)
    # listenin eleman sayısı tek sayıysa
    if liste_sayisi % 2 == 1:
        ortanca_indekx = int((liste_sayisi+1)/2)-1
        return liste[ortanca_indekx]
    # listenin eleman sayısı çift sayıysa
    else:
        ortanca_indekx_1 = int(liste_sayisi/2)-1
        ortanca_indekx_2 = ortanca_indekx_1 + 1
        return (liste[ortanca_indekx_1] + liste[ortanca_indekx_2])/2

# örnek kullanım
liste = [2, 7, 5, 3, 6, 5]
print(ortanca_eleman(liste)) # çıktı: 4.5
