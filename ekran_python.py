# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ekran.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1050, 650)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));border-radius: 30px;")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(50, 59, 1050, 960))
        self.frame.setStyleSheet("background-color: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_kapa = QtWidgets.QPushButton(Dialog)
        self.btn_kapa.setGeometry(QtCore.QRect(994, 20, 17, 17))
        self.btn_kapa.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_kapa.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_kapa.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {        \n"
"    background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.btn_kapa.setText("")
        self.btn_kapa.setObjectName("btn_kapa")
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setGeometry(QtCore.QRect(0, 10, 71, 51))
        self.logo.setStyleSheet("background-color:none;\n"
"image: url(:/logom/tubitak_logo.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(50, 60, 960, 570))
        self.stackedWidget.setStyleSheet("background-color: rgb(60, 231, 195,150);\n"
"border-radius: 12px;\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("background-color: rgb(60, 231, 195,150);\n"
"")
        self.page.setObjectName("page")
        self.tumor_i_t = QtWidgets.QLabel(self.page)
        self.tumor_i_t.setGeometry(QtCore.QRect(20, 440, 291, 21))
        self.tumor_i_t.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.tumor_i_t.setObjectName("tumor_i_t")
        self.Roket_Map = QtWidgets.QWidget(self.page)
        self.Roket_Map.setGeometry(QtCore.QRect(350, 10, 591, 411))
        self.Roket_Map.setObjectName("Roket_Map")
        self.bt_2 = QtWidgets.QLabel(self.Roket_Map)
        self.bt_2.setGeometry(QtCore.QRect(0, 0, 590, 410))
        self.bt_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"image:none;")
        self.bt_2.setText("")
        self.bt_2.setObjectName("bt_2")
        self.isle_onay = QtWidgets.QPushButton(self.page)
        self.isle_onay.setGeometry(QtCore.QRect(700, 500, 100, 30))
        self.isle_onay.setStyleSheet("QPushButton {\n"
"    color:rgb(250,250,250);\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: none;\n"
"    border-radius: 10px;        \n"
"    background-color:  rgb(0, 85, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(0, 85, 127, 100);\n"
"}")
        self.isle_onay.setObjectName("isle_onay")
        self.bt_sec = QtWidgets.QPushButton(self.page)
        self.bt_sec.setGeometry(QtCore.QRect(570, 500, 100, 30))
        self.bt_sec.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    color:rgb(250,250,250);\n"
"\n"
"    background-color: rgb(0, 85, 127);\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(0, 85, 127, 150);\n"
"}")
        self.bt_sec.setObjectName("bt_sec")
        self.kist_t = QtWidgets.QLabel(self.page)
        self.kist_t.setGeometry(QtCore.QRect(20, 470, 291, 21))
        self.kist_t.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.kist_t.setObjectName("kist_t")
        self.tas_t = QtWidgets.QLabel(self.page)
        self.tas_t.setGeometry(QtCore.QRect(20, 500, 291, 21))
        self.tas_t.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.tas_t.setObjectName("tas_t")
        self.normal_t = QtWidgets.QLabel(self.page)
        self.normal_t.setGeometry(QtCore.QRect(20, 530, 291, 21))
        self.normal_t.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.normal_t.setObjectName("normal_t")
        self.nii_katman = QtWidgets.QPushButton(self.page)
        self.nii_katman.setGeometry(QtCore.QRect(40, 60, 181, 41))
        self.nii_katman.setStyleSheet("QPushButton {\n"
"    color:rgb(250,250,250);\n"
"    border: none;\n"
"    border-radius: 10px;        \n"
"    background-color:  rgb(0, 85, 127);\n"
"    \n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(0, 85, 127, 100);\n"
"}")
        self.nii_katman.setObjectName("nii_katman")
        self.ni_kaydet = QtWidgets.QPushButton(self.page)
        self.ni_kaydet.setGeometry(QtCore.QRect(40, 120, 181, 41))
        self.ni_kaydet.setStyleSheet("QPushButton {\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"    color:rgb(250,250,250);\n"
"    border: none;\n"
"    border-radius: 10px;        \n"
"    background-color:  rgb(0, 85, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(0, 85, 127, 100);\n"
"}")
        self.ni_kaydet.setObjectName("ni_kaydet")
        self.ni_onayla = QtWidgets.QPushButton(self.page)
        self.ni_onayla.setGeometry(QtCore.QRect(250, 92, 75, 31))
        self.ni_onayla.setStyleSheet("QPushButton {\n"
"    color:rgb(250,250,250);\n"
"    border: none;\n"
"    border-radius: 10px;        \n"
"    background-color:  rgb(0, 85, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(0, 85, 127, 100);\n"
"}")
        self.ni_onayla.setObjectName("ni_onayla")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(30, 40, 301, 131))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(540, 480, 271, 71))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.t_ihtimal = QtWidgets.QLabel(self.page)
        self.t_ihtimal.setGeometry(QtCore.QRect(320, 440, 91, 21))
        self.t_ihtimal.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.t_ihtimal.setText("")
        self.t_ihtimal.setObjectName("t_ihtimal")
        self.kist_ihtimal = QtWidgets.QLabel(self.page)
        self.kist_ihtimal.setGeometry(QtCore.QRect(320, 470, 91, 21))
        self.kist_ihtimal.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.kist_ihtimal.setText("")
        self.kist_ihtimal.setObjectName("kist_ihtimal")
        self.tas_ihtimal = QtWidgets.QLabel(self.page)
        self.tas_ihtimal.setGeometry(QtCore.QRect(320, 500, 91, 21))
        self.tas_ihtimal.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.tas_ihtimal.setText("")
        self.tas_ihtimal.setObjectName("tas_ihtimal")
        self.normal_ihtimal = QtWidgets.QLabel(self.page)
        self.normal_ihtimal.setGeometry(QtCore.QRect(320, 530, 91, 21))
        self.normal_ihtimal.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.normal_ihtimal.setText("")
        self.normal_ihtimal.setObjectName("normal_ihtimal")
        self.d_yansi = QtWidgets.QPushButton(self.page)
        self.d_yansi.setGeometry(QtCore.QRect(850, 520, 100, 30))
        self.d_yansi.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color:rgb(250,250,250);\n"
"    border: none;\n"
"    border-radius: 10px;        \n"
"    background-color:  rgb(0, 85, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(0, 85, 127, 100);\n"
"}")
        self.d_yansi.setObjectName("d_yansi")
        self.bt_semantic = QtWidgets.QLabel(self.page)
        self.bt_semantic.setGeometry(QtCore.QRect(20, 390, 311, 41))
        self.bt_semantic.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.bt_semantic.setAlignment(QtCore.Qt.AlignCenter)
        self.bt_semantic.setObjectName("bt_semantic")
        self.t_tani = QtWidgets.QLabel(self.page)
        self.t_tani.setGeometry(QtCore.QRect(700, 440, 141, 21))
        self.t_tani.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.t_tani.setText("")
        self.t_tani.setObjectName("t_tani")
        self.muhtemel_text = QtWidgets.QLabel(self.page)
        self.muhtemel_text.setGeometry(QtCore.QRect(430, 440, 261, 21))
        self.muhtemel_text.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.muhtemel_text.setObjectName("muhtemel_text")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 261, 171))
        self.label_5.setStyleSheet("background-color:none;\n"
"image: url(:/logo_meb/meb_logo.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.tumor_i_t.raise_()
        self.Roket_Map.raise_()
        self.kist_t.raise_()
        self.tas_t.raise_()
        self.normal_t.raise_()
        self.label.raise_()
        self.nii_katman.raise_()
        self.ni_kaydet.raise_()
        self.ni_onayla.raise_()
        self.label_2.raise_()
        self.bt_sec.raise_()
        self.isle_onay.raise_()
        self.t_ihtimal.raise_()
        self.kist_ihtimal.raise_()
        self.tas_ihtimal.raise_()
        self.normal_ihtimal.raise_()
        self.d_yansi.raise_()
        self.bt_semantic.raise_()
        self.t_tani.raise_()
        self.muhtemel_text.raise_()
        self.label_5.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("")
        self.page_2.setObjectName("page_2")
        self.h_oyku = QtWidgets.QTextEdit(self.page_2)
        self.h_oyku.setGeometry(QtCore.QRect(460, 300, 481, 211))
        self.h_oyku.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.h_oyku.setObjectName("h_oyku")
        self.h_yas_t = QtWidgets.QLabel(self.page_2)
        self.h_yas_t.setGeometry(QtCore.QRect(20, 60, 271, 31))
        self.h_yas_t.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.h_yas_t.setAlignment(QtCore.Qt.AlignCenter)
        self.h_yas_t.setObjectName("h_yas_t")
        self.h_isim = QtWidgets.QLineEdit(self.page_2)
        self.h_isim.setGeometry(QtCore.QRect(320, 20, 291, 31))
        self.h_isim.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.h_isim.setText("")
        self.h_isim.setObjectName("h_isim")
        self.h_cinsiyet_t = QtWidgets.QLabel(self.page_2)
        self.h_cinsiyet_t.setGeometry(QtCore.QRect(20, 100, 271, 31))
        self.h_cinsiyet_t.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.h_cinsiyet_t.setAlignment(QtCore.Qt.AlignCenter)
        self.h_cinsiyet_t.setObjectName("h_cinsiyet_t")
        self.h_cinsiyet = QtWidgets.QLineEdit(self.page_2)
        self.h_cinsiyet.setGeometry(QtCore.QRect(320, 100, 291, 31))
        self.h_cinsiyet.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.h_cinsiyet.setText("")
        self.h_cinsiyet.setObjectName("h_cinsiyet")
        self.h_yas = QtWidgets.QLineEdit(self.page_2)
        self.h_yas.setGeometry(QtCore.QRect(320, 60, 291, 31))
        self.h_yas.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.h_yas.setText("")
        self.h_yas.setObjectName("h_yas")
        self.h_iletisim_t = QtWidgets.QLabel(self.page_2)
        self.h_iletisim_t.setGeometry(QtCore.QRect(20, 140, 271, 31))
        self.h_iletisim_t.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.h_iletisim_t.setAlignment(QtCore.Qt.AlignCenter)
        self.h_iletisim_t.setObjectName("h_iletisim_t")
        self.h_isim_t = QtWidgets.QLabel(self.page_2)
        self.h_isim_t.setGeometry(QtCore.QRect(20, 20, 271, 31))
        self.h_isim_t.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.h_isim_t.setAlignment(QtCore.Qt.AlignCenter)
        self.h_isim_t.setObjectName("h_isim_t")
        self.h_email = QtWidgets.QLineEdit(self.page_2)
        self.h_email.setGeometry(QtCore.QRect(320, 140, 291, 31))
        self.h_email.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.h_email.setText("")
        self.h_email.setObjectName("h_email")
        self.h_tani_oyku = QtWidgets.QLabel(self.page_2)
        self.h_tani_oyku.setGeometry(QtCore.QRect(660, 270, 271, 21))
        self.h_tani_oyku.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.h_tani_oyku.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.h_tani_oyku.setAlignment(QtCore.Qt.AlignCenter)
        self.h_tani_oyku.setObjectName("h_tani_oyku")
        self.u_dil = QtWidgets.QLabel(self.page_2)
        self.u_dil.setGeometry(QtCore.QRect(10, 490, 151, 31))
        self.u_dil.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.u_dil.setAlignment(QtCore.Qt.AlignCenter)
        self.u_dil.setObjectName("u_dil")
        self.turkce = QtWidgets.QPushButton(self.page_2)
        self.turkce.setGeometry(QtCore.QRect(10, 530, 75, 23))
        self.turkce.setStyleSheet("QPushButton {\n"
"    color:rgb(250,250,250);\n"
"    border: none;\n"
"    border-radius: 10px;        \n"
"    background-color:  rgb(0, 85, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(0, 85, 127, 100);\n"
"}")
        self.turkce.setObjectName("turkce")
        self.english = QtWidgets.QPushButton(self.page_2)
        self.english.setGeometry(QtCore.QRect(90, 530, 75, 23))
        self.english.setStyleSheet("QPushButton {\n"
"    color:rgb(250,250,250);\n"
"    border: none;\n"
"    border-radius: 10px;        \n"
"    background-color:  rgb(0, 85, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(0, 85, 127, 100);\n"
"}")
        self.english.setObjectName("english")
        self.y_tahlil_t = QtWidgets.QLabel(self.page_2)
        self.y_tahlil_t.setGeometry(QtCore.QRect(20, 280, 361, 31))
        self.y_tahlil_t.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 100 14pt \"MS Shell Dlg 2\";")
        self.y_tahlil_t.setAlignment(QtCore.Qt.AlignCenter)
        self.y_tahlil_t.setObjectName("y_tahlil_t")
        self.y_islem = QtWidgets.QTextEdit(self.page_2)
        self.y_islem.setGeometry(QtCore.QRect(20, 320, 371, 151))
        self.y_islem.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.y_islem.setObjectName("y_islem")
        self.h_kaydet = QtWidgets.QPushButton(self.page_2)
        self.h_kaydet.setGeometry(QtCore.QRect(330, 530, 171, 23))
        self.h_kaydet.setStyleSheet("QPushButton {\n"
"    color:rgb(250,250,250);\n"
"    border: none;\n"
"    border-radius: 10px;        \n"
"    background-color:  rgb(0, 85, 127);\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(0, 85, 127, 100);\n"
"}")
        self.h_kaydet.setObjectName("h_kaydet")
        self.d_yansi_2 = QtWidgets.QPushButton(self.page_2)
        self.d_yansi_2.setGeometry(QtCore.QRect(850, 520, 100, 30))
        self.d_yansi_2.setStyleSheet("QPushButton {\n"
"    color:rgb(250,250,250);\n"
"    border: none;\n"
"    border-radius: 10px;        \n"
"    background-color:  rgb(0, 85, 127);\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(0, 85, 127, 100);\n"
"}")
        self.d_yansi_2.setObjectName("d_yansi_2")
        self.hasta_bilgi_kaydet = QtWidgets.QPushButton(self.page_2)
        self.hasta_bilgi_kaydet.setGeometry(QtCore.QRect(640, 130, 101, 31))
        self.hasta_bilgi_kaydet.setStyleSheet("QPushButton {\n"
"    color:rgb(250,250,250);\n"
"    border: none;\n"
"    border-radius: 10px;        \n"
"    background-color:  rgb(0, 85, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(0, 85, 127, 100);\n"
"}")
        self.hasta_bilgi_kaydet.setObjectName("hasta_bilgi_kaydet")
        self.id_no = QtWidgets.QLineEdit(self.page_2)
        self.id_no.setGeometry(QtCore.QRect(680, 20, 101, 31))
        self.id_no.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.id_no.setText("")
        self.id_no.setObjectName("id_no")
        self.h_cinsiyet_t_2 = QtWidgets.QLabel(self.page_2)
        self.h_cinsiyet_t_2.setGeometry(QtCore.QRect(630, 20, 41, 31))
        self.h_cinsiyet_t_2.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.h_cinsiyet_t_2.setAlignment(QtCore.Qt.AlignCenter)
        self.h_cinsiyet_t_2.setObjectName("h_cinsiyet_t_2")
        self.tc_hasta = QtWidgets.QLabel(self.page_2)
        self.tc_hasta.setGeometry(QtCore.QRect(20, 180, 271, 31))
        self.tc_hasta.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.tc_hasta.setAlignment(QtCore.Qt.AlignCenter)
        self.tc_hasta.setObjectName("tc_hasta")
        self.h_tc_yaz = QtWidgets.QLineEdit(self.page_2)
        self.h_tc_yaz.setGeometry(QtCore.QRect(320, 180, 291, 31))
        self.h_tc_yaz.setStyleSheet("border-radius: 5px;image:none;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.h_tc_yaz.setText("")
        self.h_tc_yaz.setObjectName("h_tc_yaz")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(780, 80, 151, 151))
        self.label_4.setStyleSheet("background-color:none;\n"
"image:url(:/logo_meb/meb_logo.png)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_2)
        self.btn_indir = QtWidgets.QPushButton(Dialog)
        self.btn_indir.setGeometry(QtCore.QRect(943, 20, 17, 17))
        self.btn_indir.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_indir.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_indir.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;    \n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(85, 255, 127, 150);\n"
"}")
        self.btn_indir.setText("")
        self.btn_indir.setObjectName("btn_indir")
        self.btn_cerceve = QtWidgets.QPushButton(Dialog)
        self.btn_cerceve.setGeometry(QtCore.QRect(970, 20, 17, 17))
        self.btn_cerceve.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_cerceve.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_cerceve.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(255, 170, 0, 150);\n"
"}")
        self.btn_cerceve.setText("")
        self.btn_cerceve.setObjectName("btn_cerceve")

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_kapa.setToolTip(_translate("Dialog", "Close"))
        self.tumor_i_t.setText(_translate("Dialog", "Tümör bulunma ihtimali:"))
        self.isle_onay.setText(_translate("Dialog", "İşle"))
        self.bt_sec.setText(_translate("Dialog", "BT Seç"))
        self.kist_t.setText(_translate("Dialog", "Kist bulunma ihtimali:"))
        self.tas_t.setText(_translate("Dialog", "Taş bulunma ihtimali:"))
        self.normal_t.setText(_translate("Dialog", "Sağlıklı olma ihtimali:"))
        self.nii_katman.setText(_translate("Dialog", ".nii dosya katmanlara ayir"))
        self.ni_kaydet.setText(_translate("Dialog", "kaydedilecek yeri seç"))
        self.ni_onayla.setText(_translate("Dialog", "Onayla"))
        self.d_yansi.setText(_translate("Dialog", "Diğer yansı"))
        self.bt_semantic.setText(_translate("Dialog", "BT ile anlamsal bölütleme"))
        self.muhtemel_text.setText(_translate("Dialog", "Muhtemel Tanı:"))
        self.h_yas_t.setText(_translate("Dialog", "Yaşı"))
        self.h_cinsiyet_t.setText(_translate("Dialog", "Cinsiyeti"))
        self.h_iletisim_t.setText(_translate("Dialog", "İletişim Bilgisi (Email)"))
        self.h_isim_t.setText(_translate("Dialog", "Hasta İsim Soy İsim"))
        self.h_tani_oyku.setText(_translate("Dialog", "Tanı ve Hastanın Öyküsü"))
        self.u_dil.setText(_translate("Dialog", "Uygulama Dili"))
        self.turkce.setText(_translate("Dialog", "Türkçe"))
        self.english.setText(_translate("Dialog", "English"))
        self.y_tahlil_t.setText(_translate("Dialog", "Yapılacak Tahliller ve İşlemler"))
        self.h_kaydet.setText(_translate("Dialog", "İŞLE"))
        self.d_yansi_2.setText(_translate("Dialog", "Diğer yansı"))
        self.hasta_bilgi_kaydet.setText(_translate("Dialog", "Tüm bilgileri Kaydet"))
        self.h_cinsiyet_t_2.setText(_translate("Dialog", "ID:"))
        self.tc_hasta.setText(_translate("Dialog", "Hasta TCKN"))
        self.btn_indir.setToolTip(_translate("Dialog", "Maximize"))
        self.btn_cerceve.setToolTip(_translate("Dialog", "Minimize"))
import logo_meb_rc
import logo_rc