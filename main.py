from ast import Index
import enum
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *  #Bu * işlemi hepsini al demek yani bütün kütüphane gibi düşünebiilşrsin
from panel import *

#Arayüz İşlemleri 
#----------------------------------
uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()

#VERİ TABANI İŞLEMLERİ
#-----------------------------------
import sqlite3
baglanti = sqlite3.connect('kayit.db')
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute('Create Table if not Exists Kayit(Ad text,Soyad text,Sirket text)')
baglanti.commit()


ui.tbl1.setHorizontalHeaderLabels(('Ad','Soyad','Şirket'))

def kayit_ekle():
    Ad = ui.ln1.text()
    Soyad = ui.ln2.text()
    Sirket = ui.cmb1.currentText()
    
    try:
        ekle = 'insert into Kayit(Ad,Soyad,Sirket) values (?,?,?)'
        islem.execute(ekle,(Ad,Soyad,Sirket))
        baglanti.commit()
        ui.statusbar.showMessage('Kayit Eklendi.',1000)
        kayit_listele()

    except: 
        ui.statusbar.showMessage('Kayit Eklenenemedi Hata.',1000)
        

def kayit_listele():
    ui.tbl1.clear()
    ui.tbl1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.tbl1.setHorizontalHeaderLabels(('Ad','Soyad','Şirket'))
    sorgu = 'Select * from Kayit'
    islem.execute(sorgu)
    
    for indexSatir,kayitNumarası in enumerate(islem):
        for IndexSutun,KayitSutun in enumerate(kayitNumarası):
            ui.tbl1.setItem(indexSatir,IndexSutun,QTableWidgetItem(str(KayitSutun)))


def kayit_silme():
    sil_mesaj = QMessageBox.question(pencere,'Silme Onayı','Silmek İstediğnize Eminmisiniz ?')
    QMessageBox.Yes | QMessageBox.No

    if sil_mesaj == QMessageBox.Yes:
        secilen_kayit = ui.tbl1.selectedItems()
        silinicek_kayit = secilen_kayit[0].text()
        
        sorgu = 'delete from Kayit where Ad = ?'
    
        try:
            islem.execute(sorgu,(silinicek_kayit,))
            baglanti.commit()
            ui.statusbar.showMessage('Kayit Silindi.',1000)
            kayit_listele()
        except:
            ui.statusbar.showMessage('Kayit Silinemedi Hata !',1000)

    else:
        ui.statusbar.showMessage('İşlem İptal Edildi.',1000)


def sirkete_göre_listele():
    listelenecek_sirket = ui.cmb2.currentText()
    sorgu = 'select * from Kayit where Sirket = ?'
    islem.execute(sorgu,(listelenecek_sirket,))
    ui.tbl1.clear()
    ui.tbl1.setHorizontalHeaderLabels(('Ad','Soyad','Şirket'))

    for indexSatir,kayitNumarası in enumerate(islem):
        for IndexSutun,KayitSutun in enumerate(kayitNumarası):
            ui.tbl1.setItem(indexSatir,IndexSutun,QTableWidgetItem(str(KayitSutun)))


#BUTONLAR

ui.btn1.clicked.connect(kayit_ekle)

ui.btn2.clicked.connect(kayit_silme)

ui.btn3.clicked.connect(sirkete_göre_listele)



kayit_listele()

sys.exit(uygulama.exec_())