#-*- coding: UTF-8 -*-

import sys
from PyQt4 import QtCore, QtGui, uic , Qt
import  sqlite3
qtCreatorFile = "windo_home.ui"  # Enter file here.
qtCreatorFile2 = "windi_2.ui"  # Enter file here.
qtCreatorFile3 = "add_new_etidient.ui"  # Enter file here.
qtCreatorFile4 = "add_new_classe.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile )
Ui_MainWindow2, QtBaseClass2 = uic.loadUiType(qtCreatorFile2)
Ui_MainWindow3, QtBaseClass2 = uic.loadUiType(qtCreatorFile3)
Ui_MainWindow4, QtBaseClass2 = uic.loadUiType(qtCreatorFile4)





class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.betton()
        self.combobox_classe()






    def betton(self):
         self.pushButton_3.clicked.connect(self.etidient)
         self.pushButton.clicked.connect(self.foneetrn_add_new_etidient)
         self.pushButton_8.clicked.connect(self.add_new_classe)




    def etidient(self):
        self.window2 = fonetr_etidient()
        self.window2.show()




    def foneetrn_add_new_etidient(self):
        self.window3 = add_etidient()
        self.window3.show()

    def add_new_classe(self):
        self.window4 = add_new_classe()
        self.window4.show()



    def combobox_classe(self):
        file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT classe FROM etidient " )
        s = self.cur.fetchall()
        for  i  in  s  :
            if i[0] != None :
                self.comboBox.addItem(i[0])

# هذا الكلاس تاع الطلبة يمركي الابسنس
class fonetr_etidient(QtGui.QMainWindow, Ui_MainWindow2):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.combobox_classe()
        self.bottun()


    def bottun(self):
        self.pushButton_3.clicked.connect(self.pass_nome_etidient)
        #self.pushButton.clicked.connect(self.pass_nome_etidient)



    # تشغيل كومبو بوكس
    def combobox_classe(self):
        file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT classe FROM etidient " )
        s = self.cur.fetchall()
        for  i  in  s  :
            if i[0] != None :
                self.comboBox.addItem(i[0])

    # هذي  الدالة ترجع كامل اسماء الي في القسم في قائمة

    def get_nom_etidient(self):
        classe_combo = self.comboBox.currentText()
        file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()


        self.cur.execute("SELECT * FROM etidient")
        car = self.cur.fetchall()

        list_class = []

        #strr = u' '.join(classe).encode('utf-8')



        for i  in  car :
            if  classe_combo in  i  :
                list_class.append(i[1])
        return   list_class


    #  هذي الدالة تدمج بين قائمة مكونة من 73 صفر و القائمة التي  تحتوي اسماء الطلبة للاستخدام فيما بعد
    def liste_total(self):
        liste = self.get_nom_etidient()
        list__ =  [0] * 36
        i = 0
        while len(liste) > i :
            list__[i] = liste[i]
            i  = i+1
        return  list__



    def pass_nome_etidient(self):
        liste = self.liste_total()
        if liste[0] != 0 and liste[0] != None :
            self.lineEdit_1.setText(liste[0])
        if liste[1] != 0 and liste[1] != None :
            self.lineEdit_2.setText(liste[1])
        if liste[2] != 0  and liste[2] != None :
            self.lineEdit_3.setText(liste[2])
        if liste[3] != 0 and liste[3] != None :
            self.lineEdit_4.setText(liste[3])
        if liste[4] != 0 and liste[4] != None :
            self.lineEdit_5.setText(liste[4])
        if liste[5] != 0 and liste[5] != None :
            self.lineEdit_6.setText(liste[5])
        if liste[6] != 0 and liste[6] != None :
            self.lineEdit_7.setText(liste[6])
        if liste[7] != 0 and liste[7] != None :
            self.lineEdit_8.setText(liste[7])
        if liste[8] != 0 and liste[8] != None :
            self.lineEdit_9.setText(liste[8])
        if liste[9] != 0 and liste[9] != None :
            self.lineEdit_10.setText(liste[9])
        if liste[10] != 0 and liste[10] != None :
            self.lineEdit_11.setText(liste[10])
        if liste[11] != 0 and liste[11] != None :
            self.lineEdit_12.setText(liste[11])
        if liste[12] != 0 and liste[12] != None :
            self.lineEdit_13.setText(liste[12])
        if liste[13] != 0 and liste[13] != None :
            self.lineEdit_14.setText(liste[13])
        if liste[14] != 0 and liste[14] != None :
            self.lineEdit_15.setText(liste[14])
        if liste[15] != 0 and liste[15] != None :
            self.lineEdit_16.setText(liste[15])
        if liste[16] != 0 and liste[16] != None :
            self.lineEdit_17.setText(liste[16])
        if liste[17] != 0 and liste[17] != None :
            self.lineEdit_18.setText(liste[17])
        if liste[18] != 0 and liste[18] != None :
            self.lineEdit_19.setText(liste[18])
        if liste[19] != 0 and liste[19] != None :
            self.lineEdit_20.setText(liste[19])
        if liste[20] != 0 and liste[20] != None  :
            self.lineEdit_21.setText(liste[20])
        if liste[21] != 0 and liste[21] != None :
            self.lineEdit_22.setText(liste[21])
        if liste[22] != 0 and liste[22] != None :
            self.lineEdit_23.setText(liste[22])
        if liste[23] != 0 and liste[23] != None :
            self.lineEdit_24.setText(liste[23])
        if liste[24] != 0 and liste[24] != None :
            self.lineEdit_25.setText(liste[24])
        if liste[25] != 0 and liste[25] != None :
            self.lineEdit_26.setText(liste[25])
        if liste[26] != 0 and liste[26] != None :
            self.lineEdit_27.setText(liste[26])
        if liste[27] != 0 and liste[27] != None :
            self.lineEdit_28.setText(liste[27])
        if liste[28] != 0 and liste[28] != None :
            self.lineEdit_29.setText(liste[28])
        if liste[29] != 0 and liste[29] != None :
            self.lineEdit_30.setText(liste[29])
        if liste[30] != 0 and liste[30] != None :
            self.lineEdit_31.setText(liste[30])
        if liste[31] != 0 and liste[31] != None :
            self.lineEdit_32.setText(liste[31])
        if liste[32] != 0 and liste[32] != None :
            self.lineEdit_33.setText(liste[32])
        if liste[33] != 0 and liste[33] != None :
            self.lineEdit_34.setText(liste[33])
        if liste[34] != 0 and liste[34] != None :
            self.lineEdit_35.setText(liste[34])
        if liste[35] != 0 and liste[35] != None :
            self.lineEdit_36.setText(liste[35])























# هذا الكلاس تاع فوناتر تاع اضافة طالب جديد

class add_etidient(QtGui.QMainWindow, Ui_MainWindow3):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.betton()
        self.data_add()





    def betton(self):
        self.pushButton.clicked.connect(self.add_new_etidient)


    def data_add(self):
        file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT classe FROM etidient ")
        s = self.cur.fetchall()
        for i in s:
            if i[0] != None :
                self.comboBox.addItem(i[0])


    def add_new_etidient(self):
        #connect avec data base

        file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
        self.conn  =  sqlite3.connect(file)
        self.cur = self.conn.cursor()




        #get le information que fonetre
        nome_ = self.lineEdit.text()
        prenome_ =  self.lineEdit_2.text()
        age_ = self.lineEdit_3.text()
        classe = self.comboBox.currentText()
        numbre_ = self.lineEdit_5.text()


        # اولا نقوم بحذف  الفراغات الزائدة في كل نص بستعمال الدالة في الكلاس تاع اضافة قسم جديد

        delet_text  =  add_new_classe()
        nome = delet_text.delet_text(nome_)
        prenome = delet_text.delet_text(prenome_)
        age = delet_text.delet_text(age_)
        numbre = delet_text.delet_text(numbre_)


        # التاكد ان الطالب غير موجود في قاعدة البانات

        self.cur.execute("SELECT * FROM etidient")
        car =  self.cur.fetchall()
        flag2 = 0
        for i in car  :
            if age == i[0] and  nome == i[1] and prenome == i[2]  :
                Qt.QMessageBox.critical(self , u'موجود بالفعل ' , u'تم اظافة هذا الطالب في هذا القسم سابقا')
                flag2 = 1
                break


        flag3 = 0
        if age == '' or nome == '' or prenome == ''  :
            flag3 = 1
            Qt.QMessageBox.critical(self, u'خطأ ', u'لم يتم ادخال كافة المعلومات')


        if flag2 + flag3 == 0  :



                #Qt.QMessageBox.critical(self, u'خطأ ', u'لم يتم ادخال كافة المعلومات')




                #ajeuté les information sur data base

                #cur.execute("CREATE TABLE etidient (age TEXT , nome TEXT , prenom TEXT , numbre INTEGER , classe TEXT)")
            self.cur.execute('''INSERT INTO etidient(age , nome , prenom , numbre , classe ) VALUES('%s' , '%s' , '%s' , '%s' , '%s' )''' %(age , nome , prenome , numbre , classe))

            self.conn.commit()


                #self.cur.execute("SELECT * FROM etidient ")
                #Is  = self.cur.fetchall()
                #for i  in Is  :
                #    print i



            Qt.QMessageBox.information(self , u'تم الحفظ'  , u'تم حفظ معلومات الطالب'  )


#  اضافة قسم جديد
class add_new_classe(QtGui.QMainWindow, Ui_MainWindow4):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.betton()


    def betton(self):
        self.pushButton.clicked.connect(self.classe)


    # هذه الدالة تحذف الفراغات الموجودة في اخر  النص

    def delet_text(self , text):

        f  = text
        i = 0
        if len(f)> 0 :
            while True:
                if f[-1] == ' ':
                    f = f[:-1]
                else:
                    break
                i = i + 1
        else :
            f = ''
        return  f

    def classe(self):
        file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()

        classes_ = self.lineEdit.text()


        # هذه الدالة تحذف الفراغات في اخر  النص

        classes =  self.delet_text(classes_)


        # سحب جميع الاقسام و اذا كان القسم موجود في قاعدة البانات اضف واحد للفلاق

        self.cur.execute("SELECT classe FROM etidient")
        car  =  self.cur.fetchall()
        flag  =  0
        for i in car  :
            if classes == i[0] :
                flag  =  1
                break
        #  اذا كان الكلاس فارغ اظهر خطأ تنبيه
        if  classes == ''   :
            Qt.QMessageBox.critical(self, u'خطأ', u'لم تقم باضافة اي شيئ ')


        # اذا كان الفلاق يساوي واحد معناه القسم موجود بالفغل
        elif flag == 1 :

            Qt.QMessageBox.critical(self, u'خطأ', u'هذا القسم موجود بالفعل ')

        #     احفظ القسم في قاعدة البانات و اظهر رسالة تاكيد الحفظ

        else :


            self.cur.execute(
                '''INSERT INTO etidient(classe) VALUES('%s')''' % (
                    classes))

            self.conn.commit()

            Qt.QMessageBox.information(self, u'تنبيه', u'تم اضافة القسم بنجاح ')




        #   هذي الحكاية بش كي ندخل قسم جديد يتحدث مباشرة في نافذة الكومبوبكس
        get_class_myapp = MyApp()
        get_class_myapp.combobox_classe()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())