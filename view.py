import csv
from preprocessing import Preprocess
from dictionary import Dictionary
from cosine import Cosine
from naivebayes import  Naivebayes
p = Preprocess()
d = Dictionary()
c = Cosine()
n = Naivebayes()
class test:
    if __name__ == '__main__':
        print '========================================================================================'
        print 'klasifikasi berita Twitter dengan Naive Bayes Berbasis Feature Expansion Cosine Similarity'
        print '========================================================================================'
        Utama = input('Sebelum Melakukan Klasifikasi Lakukan Preprocessing Terlebih Dahulu ?'
                      '\n1. Ya'
                      '\n2. Tidak'
                      '\nMasukkan Angka Pilihan : ')
        if Utama == 1:
            kamus = input('Masukkan Dokumen yang akan dijadikan Data Kamus : ')
            # latih = input('Masukkan Dokumen yang akan dijadikan Data Latih : ')
            # uji   = input('Masukkan Dokumen yang akan dijadikan Data Uji   : ')

            # proses pembuatan kamus
            dokamus = open(kamus)
            csv_dok = csv.reader(dokamus,delimiter=';')
            liskamus = p.buatlist(csv_dok)
            preprocessingkamus = p.proses(liskamus)
            # menyimpan file hasil preprocessing
            dokkamus = open('D:\SKRIPSI\Program\data\preproseskamus20.csv', 'w')
            filecsv_kamus = csv.writer(dokkamus)
            filecsv_kamus.writerows(preprocessingkamus)
            kataunik = d.unik(preprocessingkamus)
            kemunculan = d.muncul(kataunik,preprocessingkamus)
            matrik = d.matrik(kataunik,preprocessingkamus)
            frekuensi = c.frekuensi(matrik,kataunik)
            cosine = c.cosinesimilarity(frekuensi)
            # menyimpan file hasil perhitungan cosine
            dokcosine = open('D:\SKRIPSI\Program\data\cosinesim20.csv', 'w')
            filecsv_cosine = csv.writer(dokcosine)
            filecsv_cosine.writerows(cosine)
            dokamus.close()
            dokkamus.close()


            # # preprocessing data latih
            # dolatih = open(latih)
            # csv_latih = csv.reader(dolatih,delimiter=';')
            # lislatih = p.buatlist(csv_latih)
            # preprocessinglatih = p.proses(lislatih)
            # doklatih = open('D:\SKRIPSI\Program\data\hasilpreprosesdatalatih.csv', 'w')
            # filecsv_latih = csv.writer(doklatih)
            # filecsv_latih.writerows(preprocessinglatih)
            # dolatih.close()
            # doklatih.close()
            #
            # # preprocessing data uji
            # douji = open(uji)
            # csv_uji = csv.reader(douji, delimiter=';')
            # lisuji = p.buatlist(csv_uji)
            # preprocessinguji = p.proses(lisuji)
            # print preprocessinguji
            # dokuji = open('D:\SKRIPSI\Program\data\hasilpreprosesdatauji100.csv', 'w')
            # filecsv_uji = csv.writer(dokuji)
            # filecsv_uji.writerows(preprocessinguji)
            # douji.close()
            # dokuji.close()

        elif Utama == 2:
            ujilatih = open('D:\SKRIPSI\Program\data\hasilpreprosesdatalatih.csv')
            datlatih = csv.reader(ujilatih, delimiter=',')
            listlatih = p.buatlist(datlatih)
            barlatih = c.buatbar(listlatih)
            dataunik=d.unik(barlatih)
            kategori = d.kategori(barlatih)

            pilihan = input('Pilih Menu : '
                            '\n1. Pengujian '
                            '\n2. Selesai '
                            '\nMasukkan Angka Pilihan Menu :')
            # if pilihan == 1:
            #     # katabaru = []
            #     Kata = input('Klasifikasi Manual'
            #                  '\nMasukkan Kategori yang Ingin Diuji : ')
            #     print Kata
            #     # nilai =[]
            #     isi = input('Masukkan Kata yang ingin di Uji : ')
            #     # nilai.append(isi)
            #     nilai = isi
            #     testing = Kata,nilai
            #     # katabaru.append(testing)
            #     # print katabaru
            #     docoba = open('D:\SKRIPSI\Program\data\coba.csv', 'w')
            #     filecsv_coba = csv.writer(docoba)
            #     filecsv_coba.writerows(testing)
            #     preprocessinguji1 = p.proses(testing)
            #     pilih1 = input('\nMenambahkan Query Expansion ? : '
            #                    '\n1. Ya'
            #                    '\n2. Tidak '
            #                    '\nMasukkan Angka Pilihan Menu : ')
            #     if pilih1 == 1:
            #         jawab = input('Masukkan Nilai Threshold yang Diinginkan : ')
            #
            #         # hasilkamus = c.hitungthreshold(jawab,Kata)
            # #        perhitungan = nilai(Treshold)
            # #       print ' menghitung klasifikasi dengan'
            #     elif pilih1 == 2:
            #         print 'langsung proses klasifikasi'
            #     else :
            #         print 'Angka atau Pilihan yang dimasukkan tidak sesuai, terima kasih'
            if pilihan == 1:
                pilih2 = input('Pengujian : '
                               '\nPilih Menu : '
                               '\n1. Pengujian Threshold '
                               '\n2. Pengujian  Tanpa Menggunakan Feature Expansion'
                               '\n3. Pengujian Menggunakan Feature Expansion'
                               '\n4. Tampilkan Semua Pengujian'
                               '\n Masukkan Angka Pilihan Menu : ')
                if pilih2 == 1:
                    print '- melakukan pengujian dengan nilai threshold baru'
                    tres = input('masukkan batas minimal threshold yang diiginkan : ')
                    ujiuji = open('D:\SKRIPSI\Program\data\hasilpreprosesdatauji100.csv')
                    datuji = csv.reader(ujiuji,delimiter=',')
                    tresholdbaru = tres
                    # buaru = []
                    ada = p.buatlist(datuji)
                    buatlis = c.buatbar(ada)
                    hasiltreshold = c.query(tresholdbaru,buatlis) #melakukan proses feature expansion
                    ujites = open('D:\SKRIPSI\Program\data\hasilfeatureexpansion.csv')
                    datujites = csv.reader(ujites,delimiter=',')
                    baru = p.buatlist(datujites)
                    barisbaru = c.buatbar(baru)
                    # print dataunik
                    for a in barisbaru:
                        klasifikasi = n.frekuensidatauji(a[1], kategori)
                        klas = n.klasifikasi(a[1], klasifikasi, kategori, dataunik)
                        a.append(klas)
                    dohasiltreshold = open('D:\SKRIPSI\Program\data\hasilklasifikasifeatureexpansion.csv', 'w')
                    filecsv_hasil = csv.writer(dohasiltreshold)
                    filecsv_hasil.writerows(barisbaru)
                    akurasi = n.akurasi(barisbaru)
                    print 'hasil pengujian dengan menggunakan feature expansion dengan nilai threshold : ',tres, 'didapat akurasi : ',akurasi

                elif pilih2 == 2:
                   print '- memanggil dokumen yang sudah di preprocessing' \
                         '\n- melakukan proses klasifikasi tanpa menggunakan feature expansion'
                   tanpa = open('D:\SKRIPSI\Program\data\hasilpreprosesdatauji100.csv')
                   cobauji = csv.reader(tanpa, delimiter=',')
                   lis = p.buatlist(cobauji)
                   buatbaris = c.buatbar(lis)
                   for dat in buatbaris:
                       frekuen = n.frekuensidatauji(dat[1],kategori)
                       klas = n.klasifikasi(dat[1], frekuen, kategori, dataunik)
                       dat.append(klas)
                   dohasil = open('D:\SKRIPSI\Program\data\hasilklasifikasi.csv', 'w')
                   filecsv_ = csv.writer(dohasil)
                   filecsv_.writerows(buatbaris)
                   akurasi = n.akurasinofeature(buatbaris)
                   print 'hasil Akurasi pada Pengujian Tanpa Feature Expansion : ',akurasi
                elif pilih2 == 3:
                    print '- memanggil data uji yang belum dilakukan feature expansion' \
                          '\n- melakukan proses klasifikasi tanpa menggunakan feature expansion'
                    opendokumen = open('D:\SKRIPSI\Program\data\hasilklasifikasifeatureexpansion.csv')
                    dokudoku = csv.reader(opendokumen, delimiter=',')
                    dokumenbaru = p.buatlist(dokudoku)
                    barisbaru = c.buatbar(dokumenbaru)
                    akurasi = n.akurasi(dokumenbaru)
                    print ' hasil akurasi penggunaan feature expansion : ',akurasi
                elif pilih2 == 4:
                    print 'hasil akurasi semua pengujian pengujian'
                    # dengan menggunakan feature expasnion
                    opendok = open('D:\SKRIPSI\Program\data\hasilklasifikasifeatureexpansion.csv')
                    dokdok = csv.reader(opendok, delimiter=',')
                    baru = p.buatlist(dokdok)
                    barisbaru = c.buatbar(baru)
                    akurasi = n.akurasi(baru)
                    print 'hasil akurasi dengan menggunakan feature expansion : ',akurasi
                    # tanpa feature expansion
                    nofeature = open('D:\SKRIPSI\Program\data\hasilklasifikasi.csv')
                    doko = csv.reader(nofeature, delimiter=',')
                    tanpo = p.buatlist(doko)
                    newline = c.buatbar(tanpo)
                    akurasino = n.akurasinofeature(newline)
                    print 'hasil akurasi tanpa menggunakan feature expansion : ', akurasino

                else:
                    print 'Angka atau Pilihan yang dimasukkan tidak sesuai, terima kasih'
            elif pilihan == 2:
                print 'Terima Kasih'
            else :
                print 'Angka atau Pilihan yang dimasukkan tidak sesuai, terima kasih'
        else:
            print 'Angka atau Pilihan yang dimasukkan tidak sesuai, terima kasih'
        # piliha= input('gunakan kamus yang sudah tersedia? \n1.Ya \n2.Tidak \nMasukkan pilihan :')
        # if piliha==1:
        #     kamus = open('D:\SKRIPSI\Program\data\hasilkamus.csv')
        # pilihan = input('Menu : \n 1. data berita yang sudah di preprocessing \n 2. data berita baru \n Pilih menu yang diinginkan : ')
        # if pilihan==1:
        #     dokumen=[]
        #     dok = open('D:\SKRIPSI\Program\data\hasilpreproces.csv')
        #     csv_dok = csv.reader(dok, delimiter=',')
        #     for dada in csv_dok:
        #         dokumen.append(dada)
        #     print dokumen
        # elif pilihan==2:
        #     pilih=input('masukkan alamat dokumen yang akan di proses : ')
        #     dokumenlatih = open(pilih)
        #     datalatih = csv.reader(dokumenlatih,delimiter=';')
        #     hasil=p.buatlist(datalatih)
        #     akhir=p.proses(hasil)
        #     print akhir
        #     dok = open('D:\SKRIPSI\Program\data\hasilpreproces.csv', 'w')
        #     filecsv = csv.writer(dok)
        #     filecsv.writerows(akhir)
