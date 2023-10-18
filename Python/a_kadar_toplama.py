n = int(input("Bir sayı girin: "))
toplam = 0
i = 1

while i <= n:
    toplam += i
    i += 1

print("1'den {}'e kadar olan sayıların toplamı: {}".format(n, toplam))
