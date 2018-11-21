# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 10:56:26 2017

@author: resti
"""

import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
class Preprocess:
    def __init__(self):
        pass

    def buatlist(self,dokumen):
        lisbaris=[]
        for baris in dokumen:
            lisbaris.append(baris)
        return lisbaris

    def proses(self,liskata):

        # penghilangan karakter tidak penting
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''
        for kata in liskata:
            no_punct = ""
            for char in kata[1]:
                if char not in punctuations:
                    no_punct = no_punct + char
                elif char in punctuations:
                    no_punct = no_punct + ' '
            kata[1] = no_punct

        # cek stemmer
        stemmer = factory.create_stemmer()
        for bb in liskata:
            dokumen = re.split(r'\s', bb[1])
            gabung = ''
            for a in range(len(dokumen)):
                hasil = stemmer.stem(str(dokumen[a]))
                gabung += ' ' + hasil
            bb[1] = gabung

        # filtering
        stopword = open('D:\SKRIPSI\Program\data\stopwordID.csv', 'r').read().lower()
        stopwordlist = re.split(r'\n', stopword)
        for kolom in liskata:
            kaka = re.split(r'\s', kolom[1])
            fil = ''
            for b in kaka:
                if b not in stopwordlist:
                    fil += ' ' + b
            kolom[1] = fil

        # tokenisasi
        for value in liskata:
            baris = re.split(r'\s',value[1])
            value[1]=baris
            del value[1][0]

        return liskata

    def pembuatankamus(self,datakamus):
        semuakamus=[]
        for kamus in datakamus:
            e = kamus[1].split()
            if e not in semuakamus:
                semuakamus.append(e)


#
# import collections
# import math
# import csv
# from collections import Counter
# import re
# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# factory = StemmerFactory()
# # stemmer = factory.create_stemmer()
#
# class Preprocessing():
#     def __init__(self):
#         pass
#     # init variable
#     stemmed = []
#     unik = []
#
#     def punctuation(self,document):
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''
#         no_punct = ""
#         for char in document:
#             if char not in punctuations:
#                 no_punct = no_punct + char
#             elif char in punctuations:
#                 no_punct = no_punct + ' '
#         bersih = no_punct
#         return bersih
#
#     def stemming(self,bersih):
#         stemmer = factory.create_stemmer()
#         dok_baru = re.split(r'\n',bersih)
#         for dok in range(dok_baru.__len__()):
#             dok_baru[dok] = stemmer.stem(dok_baru[dok])
#         return  dok_baru
#
#
#     def filter(self,dok_baru):
#         kata = []
#         stopword = open('D:\SKRIPSI\Program\data\stopwordID.csv', 'r').read().lower()
#         stopwordlist = re.split(r'\n', stopword)
#         for data in dok_baru:
#             kata.append(re.split(r'\s',data))
#
#         kata_bersih =[]
#         for isi in kata:
#             word=""
#             for tes in isi:
#                 if tes not in stopwordlist:
#                     word = word + tes + " "
#             kata_bersih.append(word)
#         return kata_bersih
#
#
#     def value(self,kata_bersih):
#         key=0
#         dictio={}
#         for x in kata_bersih:
#             dictio[key]=x
#             key += 1
#         return dictio
#
#     def unik(self, dictio):
#         kata_unik=[]
#         for key,value in dictio.items():
#             for nilai in value.split():
#                 if nilai not in kata_unik:
#                     kata_unik.append(nilai)
#         return kata_unik
#
#     def sentence(self,dictio):
#         tiap_dokumen ={}
#         for key,value in dictio.items():
#             ada = list(set(value.split()))
#             tiap_dokumen[key]=ada
#         return tiap_dokumen
#
#     def nilai(self,kata_unik, tiap_dokumen):
#         value ={}
#         a=0
#         for kata in kata_unik:
#             for k,v in tiap_dokumen.items():
#                 for isi in v:
#                     if isi == kata:
#                         a += 1
#             value[kata]=a
#             a=0
#         return value
#
#     def tokenize(self,tiap_dokumen):
#         token = re.split(r'\s',dokumen)
#         return token
#
