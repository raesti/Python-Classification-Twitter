# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 10:56:26 2017

@author: resti
"""
import collections
import math
import csv
from collections import Counter
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from readfile import Readfile
from dictionary import Dictionary
r = Readfile
d = Dictionary

class Naivebayes:
    # init variable
    frek = {}
    count = []
    stemmed = []
    stemmed2 = []
    unik=[]
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    # melakukan pengecekan kemunculan kata dalam suatu kategori
    def frekuensidatauji(self, datauji,klasifikasi):
        frekuensi_uji={}
        for kata in datauji:
            for key1,value1 in klasifikasi.items():
                for val in value1:
                    if kata == val and kata in value1 and val in value1 :
                        kk = key1+','+kata
                        if kk not in frekuensi_uji:
                            frekuensi_uji[kk] =1
                        else:
                            frekuensi_uji[kk] +=1
        return frekuensi_uji

    # menghitung klasifikasi
    def klasifikasi(self,ujites,datatesting,klasifikasi,kataunik):
        probabilitas = {}
        hasilklasifikasi = ''
        nilaiakhir = {}
        likelihood=0

        for key, value in klasifikasi.items():
            # likelihood = 0
            for key1, value1 in datatesting.items():
                for kata in ujites:
                    kk = key+','+kata
                    if key+','+kata == key1 and kk not in probabilitas:
                        likelihood = (value1 + 1.0) / float((len(value) + len(kataunik)))
                    elif kata in key1 and kk not in probabilitas:
                        likelihood =  1.0 / float((len(value) + len(kataunik)))
                    elif key+','+kata == key1 and kk in probabilitas:
                        likelihood = float((value1 + 1.0)) / float((len(value) + len(kataunik)))
                    elif kata in key1 and kk in probabilitas:
                        likelihood =  float(1.0) / float((len(value) + len(kataunik)))
                    probabilitas[kk] = likelihood
        # print probabilitas
        prior = 100.0 / 500
        # print prior
        for key3,value3 in klasifikasi.items() :
            for key2,value2 in probabilitas.items():
                if key3+',' in key2:
                    prior *= value2
                nilaiakhir[key3]=prior
            prior=100.0/500

        # for key2, value2 in klasifikasi.items():
        #     p = 1
        #     pp = 1
        #     for charlie, delta in probabilitas.items():
        #         p *= float(delta)
        #     pp *= float(p * prior)
        #     nilaiakhir[key2] = pp
        akhir = 0
        for ini, nilai in nilaiakhir.items():
            if akhir < nilai:
                akhir = nilai
            else:
                akhir = akhir
        for isi, hasil in nilaiakhir.items():
            if hasil == akhir:
                hasilklasifikasi=isi

        return hasilklasifikasi

    # menghitung akurasi
    def akurasi(self,datalati):
        databenar=0
        datasalah=0
        for data in datalati:
            if data[0] == data[3]:
                databenar += 1
            else:
                datasalah += 1

        print ' data benar sekarang : ',databenar
        print ' data salah sekarang : ',datasalah
        akurasiakhir = float(databenar)/float((datasalah+databenar))
        print akurasiakhir
        return akurasiakhir

    # menghitung akurasi
    def akurasinofeature(self, datalati):
        databenar = 0
        datasalah = 0
        for data in datalati:
            if data[0] == data[2]:
                databenar += 1
            else:
                datasalah += 1

        print ' data benar sekarang : ', databenar
        print ' data salah sekarang : ', datasalah
        akurasiakhir = float(databenar) / float((datasalah + databenar))
        print akurasiakhir
        return akurasiakhir
    # akurasi treshold
    # def akurasitres(self,datauji):
    #     akurasi=0
    #     databenar = 0
    #     datasalah = 0
    #     treshold =0.1
    #     for data in datauji:
    #         print treshold
    #         if treshold == data[2]:
    #             if data[0] == data[3]:
    #                 databenar += 1
    #             else:
    #                 datasalah += 1
    #             print ' data benar sekarang : ', databenar
    #             print ' data salah sekarang : ', datasalah
    #         akurasi = float(databenar) / float((datasalah + databenar))
    #         print 'akurasi data dengan threshold ',treshold,':',akurasi
    #         # elif treshold > 1.0:
    #         #     break
    #         treshold += 0.1
    #
    #     return akurasi
    # mencari akurasi setiap threshold
    # def akurasifeature(self,datauji):
    #     akurasi = 0
    #     databenar = 0
    #     datasalah = 0
    #     Threshold = 0.1
    #     c=0.1
    #     while True:
    #         if Threshold == c:
    #             for a in datauji:
    #                 if a[0] == a[3]:
    #                     databenar += 1
    #                 else:
    #                     datasalah += 1
    #                 akurasi = float(databenar)/float(databenar+datasalah)
    #             Threshold += 0.1
    #             c += 0.1
    #         else:
    #             break
    #     return akurasi

    # baru dipake
    # def naivebayes(self, datatesting, klasifikasi,kataunik):
    #     a = {}
    #     probabilitas = {}
    #     nilaiakhir = {}
    #     hasilklasifikasi={}
    #     prior = 1.0 / 5
    #     b = 0
    #     for key,value in klasifikasi.items():
    #         for nilai in value:#kemungkinan ada kesalahan diperulanagan ini!
    #             for d in datatesting:
    #                 if nilai == d:
    #                     b += 1
    #                 a[d] = b
    #                 b=0
    #             likelihood = 0
    #             for isi in datatesting:
    #                 for alpha,bravo in a.items():
    #                     if isi == alpha:
    #                         if  bravo != 0:
    #                             likelihood += (bravo + 1.0) / (len(value) + len(kataunik))
    #                         elif bravo == 0:
    #                             likelihood += 1.0 / (len(value) + len(kataunik))
    #                 probabilitas[isi] = likelihood
    #                 likelihood = 0
    #     print a
    #     print probabilitas
    #     p = 0
    #     for key,value in klasifikasi.items():
    #         for charlie, delta in probabilitas.items():
    #             p += prior * delta
    #         nilaiakhir[key]=p
    #     akhir=0
    #     for ini,nilai in nilaiakhir.items():
    #         if akhir < nilai:
    #             akhir = nilai
    #         else:
    #             akhir = akhir
    #     for isi,hasil in nilaiakhir.items():
    #         if hasil == akhir:
    #             hasilklasifikasi[akhir]=isi
    #     return nilaiakhir,hasilklasifikasi

    # def tiapkategori(self,kategori):
    #     kalimat=[]
    #     for k,v in kategori.items():
    #         for d in v.split():
    #             kalimat.append(d)
    #     return kalimat

    # def unik(self,kategori):
    #     kataunik=[]
    #     for k,v in kategori.items():
    #         for kata in v.split():
    #             if kata not in kataunik:
    #                 kataunik.append(kata)
    #     return kataunik
    #
    #
    #
    # def kemunculan(self,testing,kategori):
    #     a={}
    #     b=0
    #     for d in testing:
    #         for k, v in kategori.items():
    #             for e in v:
    #                 if e == d:
    #                     b += 1
    #         a[d] = b
    #         b = 0
    #     return a
    #
    #
    # def pembobotan(self, banyakkelass):
    #     pembobotan = 1.0/banyakkelass
    #     return pembobotan
    #
    # def ConditionalProbability(self,testing, kemunculan,kategori,semua):
    #     likelihood = 0
    #     probabilitas={}
    #     for a in testing:
    #         for b,c in kemunculan.items():
    #             if a==b:
    #                 if c != 0:
    #                     likelihood += (c + 1.0)/(len(kategori)+len(semua))
    #                 else:
    #                     likelihood += 1.0/(len(kategori)+len(semua))
    #         probabilitas[a]=likelihood
    #         likelihood=0
    #     return probabilitas
    #
    # def Posterior(self,probabilitas,pembobotan):
    #     p=pembobotan
    #     for a,b in probabilitas.items():
    #         p+=p*b
    #     return  p
    #
