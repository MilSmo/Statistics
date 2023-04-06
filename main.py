import math
import scipy.stats


def NEW(lista):
    suma = 0
    n=len(lista)
    srednia=sum(lista)/n
    for i in lista:
        suma+=(i-srednia)*(i-srednia)
    wynik=1/(n-1)*suma
    return wynik

# #typ hipotezy: 1- lewostronna
# 2 - prawostronna
# 3 - lewostronna

def HDS(probka, hip_sr, odchylenie, typ_hip, alfa):
    if odchylenie==-1:
        odchylenie=NEW(probka)
    n=len(probka)
    sr_probki = sum(probka)/n
    w = (sr_probki-hip_sr)*math.sqrt(n)/odchylenie
    if n>=30:
        if typ_hip==1:
            if w>scipy.stats.norm.ppf(1-alfa):
                print(("Hipoteza przyjeta"))
            else:
                print(("Hipoteza nieprzyjeta"))
        if typ_hip==2:
            if w<-scipy.stats.norm.ppf(1-alfa):
                print(("Hipoteza przyjeta"))
            else:
                print(("Hipoteza nieprzyjeta"))
        if typ_hip==3:
            if w<-scipy.stats.norm.ppf(1-alfa/2) or w>scipy.stats.norm.ppf(1-alfa/2):
                print(("Hipoteza przyjeta"))
            else:
                print(("Hipoteza nieprzyjeta"))

    elif n<30:
        if typ_hip==1:
            if w>scipy.stats.t.ppf(1-alfa):
                print(("Hipoteza przyjeta"))
            else:
                print(("Hipoteza nieprzyjeta"))
        if typ_hip==2:
            if w<-scipy.stats.t.ppf(1-alfa):
                print(("Hipoteza przyjeta"))
            else:
                print(("Hipoteza nieprzyjeta"))
        if typ_hip==3:
            if w<-scipy.stats.t.ppf(1-alfa/2) or w>scipy.stats.t.ppf(1-alfa/2):
                print(("Hipoteza przyjeta"))
            else:
                print(("Hipoteza nieprzyjeta"))

def porownanie_srednich(probka1, probka2, wariancja1, wariancja2, ufnosc, typ_hip):
    n1 = len(probka1)
    n2 = len(probka2)
    sr_1 = sum(probka1) / n1
    sr_2 = sum(probka2) / n2
    if wariancja1==-1 or wariancja2==-1:
        sp=((n1-1)*NEW(probka1)+(n2-1)*NEW(probka2))/(n1+n2-2)
        w=(sr_1-sr_2)/sp*math.sqrt(1/n1+1/n2)
    else:
        w = (sr_1-sr_2)/math.sqrt(wariancja1/n1+wariancja2+n2)
##################################to do

def zmienne_zalezne(probka1, probka2, sr_roznica,typ_hip, ufnosc):
    #d=lista_roznic
    d=[]
    d=probka1-probka2
    n=len(d)
    sr_d=sum(d)/n
    w=(sr_d-sr_roznica)*math.len(d)/NEW(d)
    if typ_hip == 1:
        if w > scipy.stats.t.ppf(n-1):
            print(("Hipoteza przyjeta"))
        else:
            print(("Hipoteza nieprzyjeta"))
    if typ_hip == 2:
        if w < -scipy.stats.t.ppf(n-1):
            print(("Hipoteza przyjeta"))
        else:
            print(("Hipoteza nieprzyjeta"))
    if typ_hip == 3:
        if w < -scipy.stats.t.ppf(n-1) or w > scipy.stats.t.ppf(n-1):
            print(("Hipoteza przyjeta"))
        else:
            print(("Hipoteza nieprzyjeta"))

def wariancja(probka, hip_wart, alfa, typ_hip):
    #ufnosc=alfa
    n=len(probka)
    w=(n-1)*NEW(probka)/hip_wart
    if typ_hip == 1:
        if w < scipy.stats.chi2.ppf(alfa,n-1):
            print(("Hipoteza przyjeta"))
        else:
            print(("Hipoteza nieprzyjeta"))
    if typ_hip == 2:
        if w > scipy.stats.chi2.ppf(1 - alfa,n-1):
            print(("Hipoteza przyjeta"))
        else:
            print(("Hipoteza nieprzyjeta"))
    if typ_hip == 3:
        if w < scipy.stats.t.ppf(alfa/2,n-1) or w > scipy.stats.chi2.ppf(1 - alfa / 2,n-1):
            print(("Hipoteza przyjeta"))
        else:
            print(("Hipoteza nieprzyjeta"))

def rozklad_rownomierny(probka, alfa):
    oczekiwana_war=sum(probka)/len(probka)
    suma=0
    n=len(probka)
    for p in list(probka):
        suma+=(p-oczekiwana_war)**2
    w=suma/oczekiwana_war
    if w>scipy.stats.chi2.ppf(1-alfa,n-1):
        print("Hipoteza odrzucona")
    else:
        print("Hipoteza przyjeta")

def rozklad_Poissona(probka, lambda_, alfa):
    w = 0
    n=len(probka)
    for i in range(n):
        w+=(probka[i]-scipy.stats.poisson(i+1,lambda_)**2)/scipy.stats.poisson(i+1,lambda_)
    if w>scipy.stats.chi2.ppf(alfa,n-2):
        print("Hipoteza odrzucona")
    else:
        print("Hipoteza przyjeta")

