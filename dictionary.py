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
from preprocessing import Preprocess

p = Preprocess
simpan = {}
semua = []

class Dictionary:
    def __init__(self):
        pass

    # # menyimpan array dari tiap dokumen
    # def dokumen(self, kata):
    #     for kata1 in kata:
    #         for kata2 in kata1[1]:
    #             print kata2
    #     ab=[]
    #     for value in kata:
    #         print value[1]
    #     # for key, value in kata.items():
    #     #     hasil = list(set(value.split()))
    #     #     simpan[key] = hasil
    #     # return simpan

    # menyimpan semua term dalam array
    def unik(self, kata):#membuat array baru yang isinya unik
        for kata1 in kata:
            for kata2 in kata1[1]:
                if kata2 not in semua:
                    semua.append(kata2)
        # for key, value in kata.items():
        #     for b in value.split():
        #         if b not in semua:
        #             semua.append(b)
        return semua

    def muncul(self, unik, dokumen):
        a = 0
        kemunculan = {}
        for alpha in unik:
            for value in dokumen:
                for beta in value[1]:
                    if alpha == beta:
                        a += 1
            kemunculan[alpha] = a
            a = 0
        return kemunculan


    # menyimpan kata kedalam matrix
    def matrik(self, kataunik, simpan):
        matrix = {}
        for kata in kataunik:
            for hasil in simpan:
                for item in hasil[1]:
                    if kata in hasil[1] and item in hasil[1]:
                        k = kata + ',' + item
                        if k not in matrix:
                            matrix[k] = 1
                        else:
                            matrix[k] += 1
        return matrix

    def lis(self,testing):
        for a in testing:
           uji = list(set(a.split()))
        return uji

    # menghitung nilai treshold
    def treshold(self,treshold,data,kata):
        hasiltreshold = []
        for dataku in data:
            for kataku in kata:
                if kataku[1] > treshold and kataku[1] < 1.0 and dataku in kataku[0]:
                    isi = kataku[0],kataku[1]
                    hasiltreshold.append(isi)
        return hasiltreshold

    # membuat dictionary karegori
    def kategori(self,data):
        hasil1=[]
        hasil2=[]
        hasil3=[]
        hasil4=[]
        hasil5=[]
        tempekonomi = {}
        tempentertaimen = {}
        tempkesehatan={}
        tempolahraga={}
        tempteknologi={}
        total = {}
        for a in data:
            if a[2] == 'ekonomi':
                for b in a[1]:
                    hasil1.append(b)
                tempekonomi[a[2]] = hasil1
            elif a[2] == 'entertaiment':
                for c in a[1]:
                    hasil2.append(c)
                tempentertaimen[a[2]] = hasil2
            elif a[2] == 'kesehatan':
                for d in a[1]:
                    hasil3.append(d)
                tempkesehatan[a[2]] = hasil3
            elif a[2] == 'olahraga':
                for e in a[1]:
                    hasil4.append(e)
                tempolahraga[a[2]] = hasil4
            elif a[2] == 'teknologi':
                for f in a[1]:
                    hasil5.append(f)
                tempteknologi[a[2]] = hasil5

        total.update(tempkesehatan)
        total.update(tempekonomi)
        total.update(tempentertaimen)
        total.update(tempolahraga)
        total.update(tempteknologi)
        return total

    # menyiapkan semua kata unik untuk dokumen latih
    def uniksemua(self,kategori1,kategori2,kategori3,kategori4,kategori5):
        uniksemua=[]
        for k,v in kategori1.items():
            for kata in v.split():
                if kata not in uniksemua:
                    uniksemua.append(kata)

        for k,v in kategori2.items():
            for kata in v.split():
                if kata not in uniksemua:
                    uniksemua.append(kata)

        for k,v in kategori3.items():
            for kata in v.split():
                if kata not in uniksemua:
                    uniksemua.append(kata)

        for k,v in kategori4.items():
            for kata in v.split():
                if kata not in uniksemua:
                    uniksemua.append(kata)

        for k,v in kategori5.items():
            for kata in v.split():
                if kata not in uniksemua:
                    uniksemua.append(kata)
        return uniksemua

    # mengumpulkan semua dokumen menjadi satu dokumen
    def semuakata(self,kategori1,kategori2,kategori3,kategori4,kategori5):
        kate1=[]
        for key,value in kategori1.items():
            for isi in value.split():
                kate1.append(isi)

        kate2 = []
        for key, value in kategori2.items():
            for isi in value.split():
                kate2.append(isi)

        kate3 = []
        for key, value in kategori3.items():
            for isi in value.split():
                kate3.append(isi)

        kate4 = []
        for key, value in kategori4.items():
            for isi in value.split():
                kate4.append(isi)

        kate5 = []
        for key, value in kategori5.items():
            for isi in value.split():
                kate5.append(isi)

        klasifikasi={'ekonomi':kate1,'entertaimen':kate2,'kesehatan':kate3,'olahraga':kate4,'teknologi':kate5}
        return klasifikasi

