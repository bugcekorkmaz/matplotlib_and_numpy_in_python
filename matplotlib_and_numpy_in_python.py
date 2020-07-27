# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:14:15 2020

@author: Gaming
"""

from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


class Arazi():
    def __init__(self,en,boy,sensor_sayisi,hortum_sayisi,sinir_degeri):
        self.en=en
        self.boy=boy
        self.sensor_sayisi=sensor_sayisi
        self.hortum_sayisi=hortum_sayisi
        self.sinir_degeri=sinir_degeri
    def goster(self):
        print(" En :",self.en,"\n","Boy :",self.boy,"\n","Sensor sayisi : ",self.sensor_sayisi,"\n","Hortum sayisi : ",self.hortum_sayisi,"\n","Sınır Değeri : ",self.sinir_degeri)
        

            
    
en=int(input("En :"))
boy=int(input("Boy :" ))   
sensor_sayisi=int(input("Sensor sayisi :"))
hortum_sayisi=int(input("Hortum Sayisi :"))
sinir_degeri=int(input("Sınır Değeri : "))
arazi1=Arazi(en,boy,sensor_sayisi,hortum_sayisi,sinir_degeri)
arazi1.goster()

fig, ax = plt.subplots()  
ax.plot(en,boy)
ax.set_xlim(0, en)
ax.set_ylim(0,boy)


def sensor_hesapla():
       
    x = 1
    a = 0
    b = 0
    while (a+1)*(b+1) <= sensor_sayisi:
        x = x+1
        y = int((boy*x)/en)
        b = y-1
        a = x-1
    print(int(a*b) ,"sensor yeterli olacaktir")

    kenar = en/x
    print("Kenar uzunlugu SENSOR = ",kenar)
    C = (en - (a - 1)*kenar)/2
    D = (boy - (b - 1)*kenar)/2

    listex=[]
    liste1=[]
    for i in range(a):
        liste1.append(C+(kenar*i))
    degerx=(a*b)/len(liste1)

    for i in range(a):
        for j in range(int(degerx)):
            listex.append(C+(kenar*i))
    
    dondurS=[]
    dondurS.extend(listex)
    dizix=np.array(listex,dtype=int)
    """print(" x listesi = ",dizix)"""

    
    liste2=[]
    listey=[]
    for i in range(b):
        liste2.append(D+(kenar*i))
    degery=(a*b)/len(liste2)
    for i in range(int(degery)):
        listey.extend(liste2)
    dondurS.extend(listey)
    diziy=np.array(listey,dtype=int)
    """print(" y listesi = ",diziy)"""


    plt.scatter(dizix,diziy, color='b')
    plt.xlabel('X Düzlemi')
    plt.ylabel('Y Düzlemi')
    plt.title('Arazi haritası')
    plt.show()
    return dondurS
    
def hortum_hesapla():
       
    x = 1
    a = 0
    b = 0
    while (a+1)*(b+1) <= hortum_sayisi:
        x = x+1
        y = int((boy*x)/en)
        b = y-1
        a = x-1
    print(int(a*b) ,"hortum yeterli olacaktir")
    kenar = en/x
    print("Kenar uzunlugu HORTUM = ",kenar)
    C = (en - (a - 1)*kenar)/2
    D = (boy - (b - 1)*kenar)/2
    
    listex=[]
    liste1=[]
    for i in range(a):
        liste1.append(C+(kenar*i))
    degerx=(a*b)/len(liste1)

    for i in range(a):
        for j in range(int(degerx)):
            listex.append(C+(kenar*i))

    dondurH=[]
    dondurH.extend(listex)
    dizix=np.array(listex,dtype=int)
    """print(" x listesi = ",dizix)"""

    
    liste2=[]
    listey=[]
    for i in range(b):
        liste2.append(D+(kenar*i))
    degery=(a*b)/len(liste2)
    for i in range(int(degery)):
        listey.extend(liste2)
    dondurH.extend(listey)
    diziy=np.array(listey,dtype=int)
    """print(" y listesi = ",diziy)"""


    plt.scatter(dizix,diziy, color='r',s=130)
    plt.show()

    return(dondurH)




def sulama_hesapla(diziH,diziS):
    kenar=diziH[0]
    sensorsayisi=int(len(diziS)/2)
    """print("Sensor Sayisi = ", sensorsayisi)"""
    sensor=[]
    sensor=np.floor(1024*np.random.random(sensorsayisi))
    print("Random Sensör Degerleri : ",sensor)   
    sensor_X=[]
    sensor_Y=[]
    for i in range(int(sensorsayisi)):
        sensor_X.append(diziS[i])
    sensor_X=np.array(sensor_X,dtype=int)
    """print("Sensorun X değerleri",sensor_X)"""
    for i in range(int(sensorsayisi)):
        sensor_Y.append(diziS[sensorsayisi])
        sensorsayisi+=1
    sensor_Y=np.array(sensor_Y,dtype=int)
    """print("Sensorun Y değerleri",sensor_Y)"""
    
    hortumsayisi=int(len(diziH)/2)
    """print("Hortum Sayisi = ", hortumsayisi)"""
    hortum_X=[]
    hortum_Y=[]
    for i in range(int(hortumsayisi)):
        hortum_X.append(diziH[i])
    hortum_X=np.array(hortum_X,dtype=int)
    """print("Hortumun X değerleri",hortum_X)"""
    for i in range(int(hortumsayisi)):
        hortum_Y.append(diziH[hortumsayisi])
        hortumsayisi+=1
    hortum_Y=np.array(hortum_Y,dtype=int)

    """print("Hortumun Y değerleri",hortum_Y)"""
 
    
    diziSonuc_X=[]
    for i in range(len(hortum_X)):
        for j in range(len(sensor_X)):
            diziSonuc_X.append(abs(hortum_X[i]-sensor_X[j]))
            
    """print("Hortumla Her Bir Sensorun Uzaklığı X = ",diziSonuc_X)"""

    diziSonuc_Y=[]
    for i in range(len(hortum_Y)):
        for j in range(len(sensor_Y)):
            diziSonuc_Y.append(abs(hortum_Y[i]-sensor_Y[j]))
            
    """print("Hortumla Her Bir Sensorun Uzaklığı Y = ",diziSonuc_Y)"""
    deger=[]
    for i in range(len(sensor_X)*len(hortum_X)):
        deger.append((sqrt(diziSonuc_X[i]**2 + diziSonuc_Y[i]**2))-kenar)
        
    """print("degerler = ",deger)"""
    diziDeger=[]
    son=[]
    jj=[]
    bolum=0
    deneme=0
    for i in range(len(sensor_X)*len(hortum_X)):
        if deger[i]<0 :
            j=int(i/len(sensor_X))
            k=i%len(sensor_X)
            print(j+1,". hortum",k+1,". sensor","sensor değeri",sensor[k])
            son.append(0)
            son[j]+=sensor[k]
            diziDeger.append(sensor[k])

            if j != deneme:
                jj.append(bolum)
                deneme=j
                bolum=0
                
            bolum+=1
    jj.append(jj[0])

    print(jj)
    
    for i in range(len(hortum_X)):
        son[i]/=jj[i]
        print(i+1,". hortumu ortalaması",son[i])

        if(son[i]>sinir_degeri):
            son[i]=son[i]-sinir_degeri
            print(i+1,". hortum ",son[i]/10,"saniye suladı")
        else:
            print(i+1,". hortum sulamaya gerek yok")
        

    
   
sulama_hesapla(hortum_hesapla(),sensor_hesapla())





