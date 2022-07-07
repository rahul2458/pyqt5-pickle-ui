import pickle
import shutil
import tkinter
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox
from window1 import Ui_MainWindow
from PyQt5.QtCore import Qt
import datetime
import os
import socket

try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = os.open(os.devnull, os.O_RDWR)

now = ''


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # hide function
        self.ui.comboBox.setHidden(True)
        self.ui.comboBox_2.setHidden(True)
        self.ui.label.setHidden(True)
        self.ui.Save_btn_3.setHidden(True)
        self.ui.Save_btn.setHidden(True)

    
        self.ui.pushButton_2.clicked.connect(lambda: self.showMinimized())
        self.ui.Save_btn.clicked.connect(self.check_Operator_id)
        self.ui.Save_btn_2.clicked.connect(self.Login_fun)
        self.ui.Save_btn_3.clicked.connect(self.Logout_function)

        # main prog load
        try:
            Prog = pickle.load(open("Line_file", "rb"))
            for item in Prog:
                print(item)
                self.ui.comboBox.addItem(item)

            Prog1 = pickle.load(open("Model_file", "rb"))
            for item in Prog1:
                print(item)
                self.ui.comboBox_2.addItem(item)

        except Exception as e:
            self.ui.error_log.setText(str(e))

        # get ip address
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            self.ui.ip_ad_label.setText(f"Machine ip address is: {ip_address}")
        except Exception as e:
            self.ui.error_log.setText(str(e))

    def check_Operator_id(self):
        space = len(self.ui.lineEdit_3.text())
        print(space)
        if self.ui.lineEdit_3.text() =="":
            self.ui.error_log.setText("Error: Operator ID can't be empty")
            self.ui.lineEdit_3.setFocus()
        elif space ==8:
            self.main_fun()

        else:
            self.ui.error_log.setText("Error: The operator's ID must be 8 digits.")

    def main_fun(self):
        now = datetime.datetime.now()
        self.ui.error_log.setText("")
        try:
            if os.path.exists("D:\气密性测试程序1021更新\气密性测试治具程序_V1.31.70_P400\气密性测试治具程序_V1.31.70_P400\气密性测试治具程序_V1.31.70_P400_执行元件\para\Line_details"):
                shutil.rmtree(r"D:\气密性测试程序1021更新\气密性测试治具程序_V1.31.70_P400\气密性测试治具程序_V1.31.70_P400\气密性测试治具程序_V1.31.70_P400_执行元件\para\Line_details")
        except:
            self.ui.error_log.setText("Error: folder&file already open need to close")
            print('  folder&file already open need to close it')

        comb1 = self.ui.comboBox.currentText()
        comb2 = self.ui.comboBox_2.currentText()
        comb3 = self.ui.lineEdit_3.text()
        try:
            if not os.path.exists('D:\气密性测试程序1021更新\气密性测试治具程序_V1.31.70_P400\气密性测试治具程序_V1.31.70_P400\气密性测试治具程序_V1.31.70_P400_执行元件\para\Line_details'):
                os.makedirs('D:\气密性测试程序1021更新\气密性测试治具程序_V1.31.70_P400\气密性测试治具程序_V1.31.70_P400\气密性测试治具程序_V1.31.70_P400_执行元件\para\Line_details')
                f = open(r'D:\气密性测试程序1021更新\气密性测试治具程序_V1.31.70_P400\气密性测试治具程序_V1.31.70_P400\气密性测试治具程序_V1.31.70_P400_执行元件\para\Line_details\details.ini', 'a')
                f.write( f'{comb1 }\n{comb2}\n{comb3}' )
                self.ui.error_log.setText('Line details updated'+ now.strftime(" %H:%M:%S"))
                f.close()
                self.os_open()
        except Exception as e:
            self.ui.error_log.setText(str(e))
            print(e)
        else:
            self.ui.error_log.setText('Error: File path error')
        

    def os_open(self):

        try:
            os.startfile("Tracking data")
            # tmp = os.popen("tasklist").read()  # it would return a str type
            # if "Tracking data.exe" in tmp:
            #     print(tmp)
            # # s = subprocess.check_output('tasklist', shell=True).decode('utf-8').split('=')
            # # if "Details_editor.exe" in s:
            #     print('checked')
                
            # else:
            #     print('not esi')
            #     os.startfile("Tracking data")
                #os.startfile("C:\\Users\\user\\Desktop\\air_tightness\\output\\Details_editor.exe")
        except Exception as e:
            print("file")
            self.ui.error_log.setText(f'Error: {e}')


    def Login_fun(self):
        
        if 'air_master' in self.ui.lineEdit.text() and '052621443186' in self.ui.lineEdit_2.text():
            self.Animat_lode()
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.error_log.setText("")
            print('Access')
        elif 'air' in self.ui.lineEdit.text() and '21443186' in self.ui.lineEdit_2.text():
            self.Animat_lode()
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.error_log.setText("")
            print('Access')


        else:
            
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.error_log.setText("Error: Access denied please input right password")
            print('Access denied')


    def Logout_function(self):
        self.ui.lineEdit.setHidden(False)
        self.ui.lineEdit_2.setHidden(False)
        self.ui.Save_btn_2.setHidden(False)
        self.ui.comboBox.setHidden(True)
        self.ui.comboBox_2.setHidden(True)
        self.ui.label.setHidden(True)
        
        self.ui.Save_btn_3.setHidden(True)
        self.ui.Save_btn.setHidden(True)
        


    def Animat_lode(self):
        self.ui.lineEdit.setHidden(True)
        self.ui.lineEdit_2.setHidden(True)
        self.ui.Save_btn_2.setHidden(True)
        self.ui.comboBox.setHidden(False)
        self.ui.comboBox_2.setHidden(False)
        self.ui.label.setHidden(False)
        self.ui.Save_btn_3.setHidden(False)
        self.ui.Save_btn.setHidden(False)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowFlags(Qt.FramelessWindowHint
                                | Qt.WindowStaysOnTopHint)
    window.show()
    sys.exit(app.exec_())
