# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 10:56:26 2017

@author: resti
"""

import math
import re
import csv
# simpan={}
# semua=[]
# ketemu = {}
# ketemulagi={}
# pecah=[]
# ketemuan={}
frekuen = {}
perkalian={}
hasil=[]
daftarkata = []
katabaru = []
rey = []

class Cosine:
    def __init__(self):
        pass


    def frekuensi(self,matrik,kataunik):
        for ada in kataunik:
            wew = []
            for aha in kataunik:
                jmlditemukan=0
                if ada +','+ aha in matrik:
                    jmlditemukan = matrik.get(ada + ',' + aha)
                if aha + ',' + ada in matrik:
                    jmlditemukan = matrik.get(aha + ',' + ada)
                wew.append(jmlditemukan)
            frekuen[ada] = wew
        # print frekuen
        return frekuen

    def cosinesimilarity(self,frekuensi):
        hasil=0
        for q,w in frekuensi.items():
            for e,r in frekuensi.items():
                for y in range(len(w)):
                    if q != e:
                        hasil += w[y]*r[y]
                perkalian[q+'-'+e]=hasil
                hasil=0

        kata = []
        akhir = []
        for u,i in perkalian.items():
            for o,p in frekuensi.items():
                for z,x in frekuensi.items():
                    if o+'-'+z == u and i != 0:
                        kuadrat1 = sum([c*c for c in p])
                        kuadrat2 = sum([v*v for v in x])
                        akar = math.sqrt(kuadrat1) * math.sqrt(kuadrat2)
                        # print akar
                        cosine = i/akar
                        kata.append(u)
                        kata.append(cosine)
                        akhir.append(kata)
                        kata=[]
                kuadrat1=0
                kuadrat2=0
                akar=0
                cosine=0
        # print akhir
        return akhir

    def buatbar(self,liskata):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''
        for kata in liskata:
            no_punct = ""
            for char in kata[1]:
                if char not in punctuations:
                    no_punct = no_punct + char
                elif char in punctuations:
                    no_punct = no_punct + ''
            kata[1] = no_punct
        for value in liskata:
            baris = re.split(r'\s',value[1])
            value[1]=baris
        return liskata

    def query(self,angka,kata):
        nilaitreshold = float(angka)
        dokum = open('D:\SKRIPSI\Program\data\cosine.csv')
        dat = csv.reader(dokum, delimiter=',')
        kaka = []
        for row in dat:
            row[1] = float(row[1])
            kaka.append(row)
        hasil = []
        treshol = nilaitreshold
        daftarkata = []
        katabaru = []
        rey = []

        if treshol <= 1.0 :
            for data in kata:
                for doko in data[1]:
                    for a in kaka:
                        if a[1] > treshol and a[1] <= 1.0 and doko in a[0]:
                            isi = a[0], a[1]
                            if isi not in hasil:
                                hasil.append(isi)
                for b in hasil:
                    baru = re.split(r'-', b[0])
                    rey.append(baru)
                for da in data[1]:
                    katabaru.append(da)
                    for rere in rey:
                        if da == rere[0]:
                            if rere[1] not in katabaru:
                                katabaru.append(rere[1])
                isi = data[0],katabaru, treshol
                if isi not in daftarkata:
                    daftarkata.append(isi)
                    # print treshol, daftarkata
                coba = open('D:\SKRIPSI\Program\data\hasilfeatureexpansion.csv', 'a')
                csv_coba = csv.writer(coba)
                csv_coba.writerows(daftarkata)
                del hasil[0:]
                del rey[0:]
                del daftarkata[0:]
                del katabaru[0:]
            treshol += 0.1
        return kata


    # def query(self,angka,kata):
    #     nilaitreshold = float(angka)
    #     dokum = open('D:\SKRIPSI\Program\data\cosine.csv')
    #     dat = csv.reader(dokum, delimiter=',')
    #     kaka = []
    #     for row in dat:
    #         row[1] = float(row[1])
    #         kaka.append(row)
    #     hasil = []
    #     treshol = nilaitreshold
    #     daftarkata = []
    #     katabaru = []
    #     rey = []
    #     while True:
    #         if treshol <= 1.0 :
    #             for data in kata:
    #                 for doko in data[1]:
    #                     for a in kaka:
    #                         if a[1] > treshol and a[1] <= 1.0 and doko in a[0]:
    #                             isi = a[0], a[1]
    #                             if isi not in hasil:
    #                                 hasil.append(isi)
    #                 for b in hasil:
    #                     baru = re.split(r'-', b[0])
    #                     rey.append(baru)
    #                 for da in data[1]:
    #                     katabaru.append(da)
    #                     for rere in rey:
    #                         if da == rere[0]:
    #                             if rere[1] not in katabaru:
    #                                 katabaru.append(rere[1])
    #                 isi = data[0],katabaru, treshol
    #                 if isi not in daftarkata:
    #                     daftarkata.append(isi)
    #                 # print treshol, daftarkata
    #                 coba = open('D:\SKRIPSI\Program\data\hasilfeatureexpansion.csv', 'a')
    #                 csv_coba = csv.writer(coba)
    #                 csv_coba.writerows(daftarkata)
    #                 del hasil[0:]
    #                 del rey[0:]
    #                 del daftarkata[0:]
    #                 del katabaru[0:]
    #             treshol += 0.1
    #         elif treshol > 1.0 :
    #             break
    #     return kata

    def hitunghitung(self,angka,kata):
        nilaitreshold = float(angka)
        dokum = open('D:\SKRIPSI\Program\data\cosine.csv')
        dat = csv.reader(dokum, delimiter=',')
        kaka = []
        hasil = []
        treshol = nilaitreshold
        daftarkata = []
        katabaru = []
        rey = []
        for row in dat:
            row[1] = float(row[1])
            kaka.append(row)

        for data in kata:
            for doko in data[1]:
                for a in kaka:
                    if a[1] > treshol and a[1] <= 1.0 and doko in a[0]:
                        isi = a[0], a[1]
                        if isi not in hasil:
                            hasil.append(isi)
            for b in hasil:
                baru = re.split(r'-', b[0])
                rey.append(baru)
            for da in data[1]:
                katabaru.append(da)
                for rere in rey:
                    if da == rere[0]:
                        if rere[1] not in katabaru:
                            katabaru.append(rere[1])
            isi = data[0],katabaru, treshol
            if isi not in daftarkata:
                daftarkata.append(isi)
            print treshol, daftarkata
            del hasil[0:]
            del rey[0:]
            del daftarkata[0:]
            del katabaru[0:]
        return kata

        # for term in test:
        #     for key,value in matrix.items():
        #         if term +',' in key:
        #             ketemu[key]=value
        #
        # for alpha,beta in ketemu.items():
        #     pecah.append(re.split(r',',alpha))
        #
        # for k,v in matrix.items():
        #     for charlie in pecah:
        #         if charlie[1] +',' in k:
        #             ketemulagi[k]=v
        #
        # ada=[]
        # for kata in kataunikkamus:
        #     for delta,echo in ketemulagi.items():
        #         if kata+',' in delta:
        #             ada.append(echo)
        #     ketemuan[kata]=ada
        #     ada=[]
        #
        # lis=[]
        # for fooxtrot,golf in ketemu.items():
        #     lis.append(golf)
        #
        # a=0
        # cos={}
        # perkalian=[]
        # hasil=0
        # for hotel,india in ketemuan.items():#kemungkinan mulai salah disini atau di perulangan sebelumnya
        #     for i in range(len(lis)):
        #         if a >= len(india):
        #             perkalian.append(hasil)
        #             hasil=0
        #             break
        #         else:
        #             hasil += lis[i] * india[i]
        #             cos[hotel]=hasil
        #         a +=1
        #     a=0
        #
        # nilai=0
        # akhir={}
        # for juliet,kilo in cos.items():
        #     for lima,mike in ketemuan.items():
        #         kuadrat1 = sum([x * x for x in lis])
        #         kuadrat2 = sum([y * y for y in mike])
        #         akar = math.sqrt(kuadrat1) * math.sqrt(kuadrat2)
        #         cosine = kilo/akar
        #         akhir[juliet]=cosine
        #     kuadrat2=0
        #     kuadrat1=0
        #     akar=0
        #     cosine=0
        # return akhir


    # def perhitungan(self,testing,matrik,kataunik):
    #
    #     for kata in testing:
    #         dates = list(set(kata.split()))
    #
    #     ketemu = {}
    #     for term in dates:
    #         for key,value in matrik.items():
    #             if term + ',' in key:
    #                 ketemu[key]=value
    #
    #     sesuatu=[]
    #     for key,value in ketemu.items():
    #         sesuatu.append(re.split(r',',key))
    #
    #     ketemulagi={}
    #     for key,value in matrik.items():
    #         for alpha in sesuatu:
    #             if alpha[1] + ',' in key:
    #                 ketemulagi[key]=value
    #
    #     ada=[]
    #     for key,values in ketemulagi.items():
    #         ada.append(re.split(r',',key))
    #
    #     ketemuan={}
    #     nilai=[]
    #     for term in kataunik:
    #         for bravo,charlie in ketemulagi.items():
    #             if term + ',' in bravo:
    #                 nilai.append(charlie)
    #         ketemuan[term]=nilai
    #         nilai=[]
    #
    #     lis=[]
    #     for delta,echo in ketemu.items():
    #         lis.append(echo)
    #
    #     a=0
    #     aa={}
    #     perkalian=[]
    #     hasil = 0
    #     for foxtrot,golf in ketemuan.items():
    #         for i in range(len(lis)):
    #             if a >= len(golf):
    #                 perkalian.append(hasil)
    #                 hasil = 0
    #                 break
    #             else:
    #                 hasil += lis[i] * golf[i]
    #                 aa[foxtrot] = hasil
    #             a +=1
    #         a = 0
    #
    #     hasilakhir={}
    #     for a,b in aa.items():
    #         for c,d in ketemuan.items():
    #             kuadrat1 = sum([x * x for x in lis])
    #             kuadrat2 = sum([y * y for y in d])
    #             akar = math.sqrt(kuadrat1) * math.sqrt(kuadrat2)
    #             cosine = b / akar
    #             hasilakhir[a] = cosine
    #         kuadrat1 = 0
    #         kuadrat2 = 0
    #         akar = 0
    #         cosine = 0
    #
    #     baru=[]
    #     for a in dates:
    #         for b in kataunik:
    #             if a == b :
    #                 baru.append(a)
    #     cosinesim={}
    #     for c in baru:
    #         cosinesim[c]=hasilakhir
    #
    #     nilai = 0
    #     cosinus={}
    #     for yes, ya in cosinesim.items():
    #         for isi,has in ya.items():
    #             if nilai < has:
    #                 nilai = has
    #         else:
    #             nilai = nilai
    #         for e,f in hasilakhir.items():
    #             if nilai==f:
    #                 cosinus[e]=f
    #     return cosinesim,cosinus