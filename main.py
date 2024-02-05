# okey taşları oluşturup dağıtan fonksiyon
import random

renkler = ["sarı", "mavi", "kırmızı", "siyah"]
oyuncular = {"burak": [], "bekir": [], "merve": [], "Ayda": []}
taslar = []
okey = None
def taslarıOlustur():
    taslar.append(["sahte"])
    taslar.append(["sahte"])
    for renk in renkler:
        for i in range(1, 14):
            taslar.extend([[renk, i]] * 2)  # bu kod iki kez eklenmesini sağlar

def okeyOlustur():
    global okey
    okey = random.choice(taslar)
    taslar.remove(okey)
    print(okey)

def taslariDagit(oyuncu):
   for i in range(21):
     tas = random.choice(taslar)
     oyuncu.append(tas)
     taslar.remove(tas)
   print(oyuncu)

def main():

    taslarıOlustur()
    okeyOlustur()
    taslariDagit(oyuncular["burak"])
    taslariDagit(oyuncular["bekir"])
    taslariDagit(oyuncular["merve"])
    taslariDagit(oyuncular["Ayda"])


if __name__ == "__main__":
    main()
