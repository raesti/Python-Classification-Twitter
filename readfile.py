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

                            #init variable
frek={}
count = []
factory=StemmerFactory()
stemmer=factory.create_stemmer()
class Readfile:
    def __init__(self):
        pass
    def readdict(self):
        kamus = open('D:\SKRIPSI\Program\data\data_kamus.csv', 'r').read().lower()
        return kamus
    def readstopword(self):
        stopword = open('D:\SKRIPSI\Program\data\stopwordID.csv', 'r').read().lower()
        return stopword
    def readtesting(self):
        testing = open('D:SKRIPSI\Program\data\testing.csv','r').read().lower()
        return testing
    def readtrainig(self, ekonomi, entertaimen, kesehatan, olahraga, teknologi):
        ekonomi = open('D:\SKRIPSI\Program\data\data_training_ekonomi.csv', 'r').read().lower()
        entertaimen = open('D:\SKRIPSI\Program\data\data_training_entertaimen.csv', 'r').read().lower()
        kesehatan = open('D:\SKRIPSI\Program\data\data_training_kesehatan.csv', 'r').read().lower()
        olahraga = open('D:\SKRIPSI\Program\data\data_training_olahraga.csv', 'r').read().lower()
        teknologi = open('D:\SKRIPSI\Program\data\data_training_teknologi.csv', 'r').read().lower()
        return ekonomi,entertaimen,kesehatan,olahraga,teknologi

    def __init__(self,ekonomi):
        self.ekonomi = ekonomi

    def readekonomi(self):
        training_ekonomi = self.readekonomi.open('D:\SKRIPSI\Program\data\data_training_ekonomi.csv', 'r').read().lower()
        return training_ekonomi
