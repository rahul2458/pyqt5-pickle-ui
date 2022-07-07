import pickle
import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QListWidgetItem, QInputDialog, qApp
from Line_details_fo import Ui_MainWindow
import socket

class MainWindow2(QMainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Main function run
        self.load_line_Prog()
        self.load_model_prog()

        # buttons function call
        self.ui.inser_bt.clicked.connect(self.fun_insert_Line)
        self.ui.delete_bt.clicked.connect(self.deleteitem_from_line)
        self.ui.modified_bt.clicked.connect(self.fun_modify)
        #self.ui.actionExit.setShortcut('Ctrl+Q')
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.Aboutit)

        self.ui.line_list.itemClicked.connect(self.selection_line_list)
        self.ui.model_list.itemClicked.connect(self.selection_model_list)

        # get ip address
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            self.ui.ip_label.setText(f"Machine ip address is: {ip_address}")
        except Exception as e:
            self.ui.log_text.append(str(e))

        # function load program
    def load_line_Prog(self):
        self.ui.line_list.clear()
        try:
            Prog = pickle.load(open("Line_file", "rb"))
            self.ui.log_text.append("Line_file load successfully!")

        except:
            try:
                Prog = ['A1201          ', 'A1202          ', 'A1203          ']
                pickle.dump(Prog, open("Line_file", "wb"))
                self.ui.log_text.append("Line_file not found!")
            except:
                Prog = ['A1201          ', 'A1202          ', 'A1203          ']
                pickle.dump(Prog, open("Line_file", "wb"))
                self.ui.log_text.append("Line_file not found!")
        time.sleep(.2)
        try:
            for item in Prog:
                self.ui.line_list.addItem(item)

        except:
            try:
                for item in Prog:
                    self.ui.line_list.addItem(item)
            except:
                pass

    def load_model_prog(self):
        self.ui.model_list.clear()
        try:
            Prog = pickle.load(open("Model_file", "rb"))
            self.ui.log_text.append("Model_file load successfully!")
        except:
            try:
                Prog = ['AD1818_BF      ', 'AD1818_CF      ', 'AD1818_HF      ']
                pickle.dump(Prog, open("Model_file", "wb"))
                self.ui.log_text.append("Model_file not found!")
            except:
                Prog = ['AD1818_BF      ', 'AD1818_CF      ', 'AD1818_HF      ']
                pickle.dump(Prog, open("Model_file", "wb"))
                self.ui.log_text.append("Model_file not found!")
        time.sleep(.2)
        try:
            for item in Prog:
                self.ui.model_list.addItem(item)

        except:
            try:
                for item in Prog:
                    self.ui.model_list.addItem(item)
            except:
                pass

    # insert line & model number
    def fun_insert_Line(self):
        self.fun_insert_Model()
        listItems = self.ui.line_list.selectedItems()
        if not listItems: return
        selRow = self.ui.line_list.currentRow()
        selRow += 1
        line_details = self.ui.line_edit.text()
        self.ui.model_edit.clear()
        if line_details[:1] == "A" and len(line_details) == 15:
            self.ui.log_text.append(f"Line edit successfully: {self.ui.line_edit.text()}")
            self.ui.line_list.insertItem(selRow, line_details)
            self.ui.line_list.setCurrentRow(selRow)
            try:
                items = []
                for index in range(self.ui.line_list.count()):
                    data_val = self.ui.line_list.item(index)
                    h = data_val.text()
                    items.append(h)
                pickle.dump(tuple(items), open("Line_file", "wb"))
            except:
                print("err")
        else:
            self.ui.log_text.append("Line no must be start F.. / Character length should be 15")


    # insert line & model number
    def fun_insert_Model(self):
        listItems = self.ui.model_list.selectedItems()
        if not listItems: return
        selRow = self.ui.model_list.currentRow()
        selRow += 1
        line_details = self.ui.model_edit.text()
        self.ui.line_edit.clear()
        if line_details[:2] == "AD" and len(line_details) == 15:
            self.ui.log_text.append(f"Line edit successfully: {self.ui.model_edit.text()}")
            self.ui.model_list.insertItem(selRow, line_details)
            self.ui.model_list.setCurrentRow(selRow)
            try:
                items = []
                for index in range(self.ui.model_list.count()):
                    data_val = self.ui.model_list.item(index)
                    h = data_val.text()
                    items.append(h)
                pickle.dump(tuple(items), open("Model_file", "wb"))
            except:
                print("err")
        else:
            self.ui.log_text.append("Model no must be start AD.. / Character length should be 15 ")


    # select event list box on line list details
    def selection_line_list(self):
        line = self.ui.line_list.currentItem()
        line1 = line.text()
        self.ui.log_text.append(f"You have selected line no: {str(line1)}length is: {len(line1)}")
        self.ui.model_list.clearSelection()

    # select event Model box on line model details
    def selection_model_list(self):
        model = self.ui.model_list.currentItem()
        model1 = model.text()
        self.ui.log_text.append(f"You have selected Model no: {str(model1)}length is: {len(model1)}")
        self.ui.line_list.clearSelection()

    # delete line items
    def deleteitem_from_line(self):
        self.deleteitem_from_model()
        listItems = self.ui.line_list.selectedItems()
        selRow = self.ui.line_list.currentRow()
        if selRow == 0: return
        if not listItems: return
        try:
            for item in listItems:
                self.ui.line_list.takeItem(self.ui.line_list.row(item))
                items = []
                for index in range(self.ui.line_list.count()):
                    data_val = self.ui.line_list.item(index)
                    h = data_val.text()
                    items.append(h)
                pickle.dump(tuple(items), open("Line_file", "wb"))
                self.ui.log_text.append(f"Line deleted successfully!")
        except Exception as e:
            self.ui.log_text.append(str(e))

    # delete model items
    def deleteitem_from_model(self):
        listItems = self.ui.model_list.selectedItems()
        selRow = self.ui.model_list.currentRow()
        if selRow == 0: return
        if not listItems: return
        try:
            for item in listItems:
                self.ui.model_list.takeItem(self.ui.model_list.row(item))
                items = []
                for index in range(self.ui.model_list.count()):
                    data_val = self.ui.model_list.item(index)
                    h = data_val.text()
                    items.append(h)
                pickle.dump(tuple(items), open("Model_file", "wb"))
                self.ui.log_text.append(f"Model deleted successfully!")
        except Exception as e:
            self.ui.log_text.append(str(e))

    def fun_modify(self):
        listItems1 = self.ui.model_list.selectedItems()
        listItems = self.ui.line_list.selectedItems()
        if not listItems1:
            selt = self.ui.line_list.selectedItems()
            if not selt: return
            # self.ui.model_list.clearSelection()
            line = self.ui.line_list.currentItem()
            line1 = line.text()
            self.ui.modified_edit.setText(line1)
            self.ui.log_text.append(f"For line modify selected: {str(line1)}")
            print(line1)
        if not listItems:
            try:
                model = self.ui.model_list.currentItem()
                model1 = model.text()
                self.ui.modified_edit.setText(model1)
                self.ui.log_text.append(f"For model modify selected: {str(model1)}")
                #self.ui.model_list.clearSelection()
                print(model1)
            except Exception as e:
                self.ui.log_text.append(str(e))


    def keyPressEvent(self, e):
        if e.key()  == Qt.Key_Return :
            self.fun_enter_modify()

    def fun_enter_modify(self):
        line_details = self.ui.modified_edit.text()
        if line_details[:2] == "AD":
            listItems = self.ui.model_list.selectedItems()
            if not listItems: return
            listItems = self.ui.model_list.selectedItems()
            selRow = self.ui.model_list.currentRow()
            line_details = self.ui.modified_edit.text()
            selRow += 0
            self.ui.line_edit.clear()
            self.ui.model_edit.clear()
            if line_details[:2] == "AD" and len(line_details) == 15:
                self.ui.log_text.append(f"Model modify successfully!: {self.ui.modified_edit.text()}")
                self.ui.model_list.takeItem(int(selRow))
                self.ui.model_list.insertItem(selRow, line_details)
                try:
                    for item in listItems:
                        self.ui.model_list.takeItem(self.ui.model_list.row(item))
                        items = []
                        for index in range(self.ui.model_list.count()):
                            data_val = self.ui.model_list.item(index)
                            h = data_val.text()
                            items.append(h)
                        pickle.dump(tuple(items), open("Model_file", "wb"))
                        self.ui.model_list.clearSelection()

                except Exception as e:
                    self.ui.log_text.append(str(e))



        else:
            listItems = self.ui.line_list.selectedItems()
            if not listItems: return
            selRow = self.ui.line_list.currentRow()
            line_details = self.ui.modified_edit.text()
            selRow += 0
            self.ui.line_edit.clear()
            if line_details[:1] == "A" and len(line_details) == 15:
                self.ui.log_text.append(f"Line modify successfully!: {self.ui.modified_edit.text()}")
                self.ui.line_list.setCurrentRow(selRow)
                self.ui.line_list.takeItem(int(selRow))
                self.ui.line_list.insertItem(selRow, line_details)
                try:
                    for item in listItems:
                        self.ui.line_list.takeItem(self.ui.line_list.row(item))
                        items = []
                        for index in range(self.ui.line_list.count()):
                            data_val = self.ui.line_list.item(index)
                            h = data_val.text()
                            items.append(h)
                        pickle.dump(tuple(items), open("Line_file", "wb"))
                        self.ui.line_list.clearSelection()
                except Exception as e:
                    self.ui.log_text.append(str(e))

    def Aboutit(self):
        QMessageBox.about(self, "About It",
                          "This software is only designed to provide details of the <b>Data tracking software </b>"
                          "of <b>Air-tightness</b> machine such as for line details and model details. "
                          " The help of this software will create two files which will contain "
                          " <b>Line details & Model details.</b> "
                          " \n<b>Note: </b> Without this software, these file can't be edited and modified.")





if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    windows = MainWindow2()
    windows.show()
    sys.exit(app.exec_())