from random import randint
from random import random


# Madeni para atış hesabı
def madeni_para(n=10000):
    """Bu fonksiyon ile yazı tura atışı n defa simüle edilip
    sonucun olasılığı hesaplanmaktadır"""
    tura = 0
    for _ in range(n):
        if randint(0, 1) == 0:
            tura += 1

    return tura / n


# Zar atış hesabı
def zar(n=10000):
    """Bu fonksiyon ile zar atışı n defa simüle edilip
    sonucun olasılığı hesaplanmaktadır"""
    bir = 0
    for _ in range(n):
        if randint(0, 5) == 0:
            bir += 1

    return bir / n


# Zar ve para atışı hesabı
def zar_ve_para(n=10000):
    """Bu fonksiyon ile zar ve para atışı n defa simüle edilip
    sonucun olasılığı hesaplanmaktadır"""
    sayac = 0
    for _ in range(n):
        if randint(0, 1) == 0 and randint(0, 5) == 0:
            sayac += 1

    return sayac / n

# Torbadan top çekme hesabı
def top_cekme(n=10000):
    """Bu fonksiyon ile bir torbadan çekilen top n defa simüle edilip
    sonucun olasılığı hesaplanmaktadır"""
    pass


# Torbadan 2 top çekme hesabı
def top_cekme2(n=10000):
    """Bu fonksiyon ile iki adet torbadan çekilen top n defa simüle edilip
    sonucun olasılığı hesaplanmaktadır"""
    pass


# Pi sayısı hesabı
def pi(n=10000):
    """Bu fonksiyon ile rastgele seçlen n noktanın
    bir kareye iç teğen olan dairenin içinde olma olasılığı hesaplanır
    ve Pi sayısı elde edilir"""
    daire_alani = 0
    for _ in range(n):
        x = 2 * (random() - 0.5)
        y = 2 * (random() - 0.5)
        uzaklik = pow(pow(x, 2) + pow(y, 2), 0.5)
        if uzaklik < 1:
            daire_alani += 1

    return 4 * daire_alani / n


if __name__ == "__main__":
    # print("Madeni para: ", madeni_para(), 1 / 2)
    # print("Zar: ", zar(), 1 / 6)
    # print("Zar + Para: ", zar_ve_para(), 1 / 6 * 1 / 2)
    print(pi(n=1000_000))
