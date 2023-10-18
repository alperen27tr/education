istenen_islem = int(
    input(
        """
                    Yüzey Alanı Hesaplamak İçin ==> 1
                    Hacim Hesaplamak İçin ==> 2
                    """
    )
)
pi = 3

if istenen_islem == 1:
    istenen_sekil_y = int(
        input(
            """
    Küp için ==> 1
    Dikdörtgen Prizma İçin ==> 2
    Küre için ==> 3
    Silindir İçin ==> 4
    """
        )
    )
    if istenen_sekil_y == 1:
        a = int(input("Bir kenar uzunluğunu giriniz: "))
        sonuc_kup_yuzey = 6 * a * a
        print(sonuc_kup_yuzey)

    if istenen_sekil_y == 2:
        a = int(input("Uzun kenar: "))
        b = int(input("Kısa kenar: "))
        c = int(input("Yükseklik: "))
        sonuc_dik_yuzey = 2 * a * b + 2 * a * c + 2 * b * c
        print(sonuc_dik_yuzey)

    if istenen_sekil_y == 3:
        r = int(input("Yarı Çapı: "))
        sonuc_kure_yuzey = 4 * pi * r * r
        print(sonuc_kure_yuzey)

    if istenen_sekil_y == 4:
        r = int(input("Yarı Çapı: "))
        h = int(input("Yükseklik: "))
        sonuc_silindir_yuzey = (2 * pi * r * h) + (pi * r * r) + (pi * r * r)
        print(sonuc_silindir_yuzey)


if istenen_islem == 2:
    istenen_sekil_h = int(
        input(
            """
    Küp İçin ==> 1
    Dikdörtgen Prizma İçin ==> 2
    Küre İçin ==> 3
    Silindir İçin ==> 4 
    """
        )
    )

    if istenen_sekil_h == 1:
        a = int(input("Bir kenar uzunluğunu giriniz: "))
        sonuc_kup_hacim = a * a * a
        print(sonuc_kup_hacim)

    if istenen_sekil_h == 2:
        a = int(input("Uzun kenar: "))
        b = int(input("Kısa kenar: "))
        c = int(input("Yükseklik: "))
        sonuc_dik_hacim = a * b * c
        print(sonuc_dik_hacim)

    if istenen_sekil_h == 3:
        r = int(input("Yarı Çapı: "))
        sonuc_kure_hacim = 4 / 3 * pi * r * r * r
        print(sonuc_kure_hacim)

    if istenen_sekil_h == 4:
        r = int(input("Yarı Çapı: "))
        h = int(input("Yükseklik: "))
        sonuc_silindir_hacim = pi * r * r * h
        print(sonuc_silindir_hacim)
