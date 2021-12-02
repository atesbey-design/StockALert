import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel("StockList.xlsx")


def StokArtırma(ürün,a):
    data[ürün - 1:ürün]["Stok Adedi"]=data[ürün - 1:ürün]["Stok Adedi"]+a

    data.to_excel("StockListYeni.xlsx")
    print(data)

def StokAzaltma(ürün, a):

    if a>data[ürün-1:ürün]["Stok Adedi"]:
        print("Bu işlemi yapabilecek bir stok adediniz yoktur.")
    else:
        data[ürün - 1:ürün]["Stok Adedi"] = data[ürün - 1:ürün]["Stok Adedi"] - a
        data.to_excel("StockListYeni.xlsx")
        print(data)


def grafikGöster():
    ürünAdedi = [data[0:1]["Stok Adedi"], data[1:2]["Stok Adedi"], data[2:3]["Stok Adedi"], data[3:4]["Stok Adedi"],
                 data[3:4]["Stok Adedi"], 0]
    ürünListesi = ["Bilgisayar", "Telefon", "Ssd", "Ekran Kartı", "Televizyon", ""]
    plt.pie(ürünAdedi,
            labels=ürünListesi,
            colors=["#00ff00", "g", "r", "b", "m"],
            autopct='%1.1f%%',
        shadow=True
            )
    plt.title("ÜRÜN STOK GRAFİĞİ")
    plt.legend()
    plt.show()

def main():
    print("STOK ADEDİ SİSTEMİ\n")
    print(data)

while(True):
    secim = int(input("Hangi işlemi yapmak istersiniz \n1-STOKLARI GÖSTER\n2-STOK EKLE\n3-STOK SİL  \n"))
    if secim==1:
        grafikGöster()
    elif secim==2:
        ürün=int(input("Hangi ürüne işlem yapmak istersiniz\n 1-Bilgisayar\n2-Telefon\n3-Ssd\n4Ekran Kartı\n5-Televizyon"))
        adet=int(input("Ne kadar ürün eklemek istersiniz: "))
        StokArtırma(ürün,adet)
    elif secim==3:
        ürün=int(input("Hangi ürüne işlem yapmak istersiniz  \n 1-Bilgisayar  \n2-Telefon\n3-Ssd \n4Ekran Kartı  \n5-Televizyon  "))
        adet=int(input("Ne kadar ürün silmek istersiniz: "))
        StokAzaltma(ürün,data)
    else:
        break
main()

