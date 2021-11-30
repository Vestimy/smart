import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLineEdit, QPushButton, QTableWidgetItem, \
    QErrorMessage, QTableWidget, QCheckBox, QTableView, QMessageBox
from PySide6.QtCore import QFile, Qt, QRegularExpression, Slot
from PySide6.QtGui import QRegularExpressionValidator, QIntValidator, QDoubleValidator, QKeySequence
from ui_mainwindow import Ui_MainWindow
from PySide6 import QtCore, QtWidgets
from base import *


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        print(f"Hello {self.edit.text()}")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Menu Bar
        self.create_menubar()

        self.ui.btn_save.clicked.connect(self.newwindow)

        self.ui.table__new_new.setColumnCount(6)
        self.ui.table__new_new.setRowCount(6)
        self.ui.table__new_new.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])
        self.ui.table__new_new.setItem(4, 4, QTableWidgetItem('hewq'))
        self.ui.table__new_new.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)

        self.ui.pushButton_save.clicked.connect(self.push_save)

        # ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"  # Часть регулярного выржение
        # ipRegex = QRegularExpression("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
        self.num = QDoubleValidator()
        self.ui.lineEdit_pcs.setValidator(self.num)
        self.ui.lineEdit_price.setValidator(self.num)

        # Категория
        self.load_category()

        # Список добавления категории в субкатегорию
        self.load_subcategory()

        # Оборудование
        self.load_equipment()

        self.ui.pushButton_subcategory.clicked.connect(self.save_subcategory)
        self.error_dialog = QErrorMessage()

    # --------------------------------------------------------------------------
    # Подкатегория----------------------------------------------------------------

    def load_subcategory(self, check=False):
        if check:
            self.ui.comboBox_subcategory.clear()
        result = CategoryEquipment.load_subcategory()
        for i in result:
            self.ui.comboBox_subcategory.addItem(i.title)

    def save_subcategory(self):
        nnn = CategoryEquipment.search_id(self.ui.comboBox_subcategory.currentText())
        print(nnn)

    def newwindow(self):
        self.form = Form()
        self.form.show()

    def push_save(self):
        title = self.ui.lineEdit_title.text()
        pcs = self.ui.lineEdit_pcs.text()
        price = self.ui.lineEdit_price.text()
        eq = Equipment()
        eq.save(title, pcs, price)
        self.rest_qline()

    # --------------------------------------------------------------------------
    # Категория----------------------------------------------------------------
    def load_category(self):
        self.ui.table_category.setAlternatingRowColors(True)
        self.ui.table_category.setSelectionBehavior(QTableView.SelectRows)
        self.ui.pushButton_delete_category_2.clicked.connect(self.delete_category)
        self.ui.pushButton_save_category.clicked.connect(self.save_category)
        self.ui.table_category.hideColumn(0)
        self.ui.table_category.hideColumn(3)
        self.ui.table_category.hideColumn(4)
        self.show_list_category()
        self.ui.table_category.cellChanged.connect(self.save_cell)

    def save_category(self):
        title = self.ui.lineEdit_title_category.text()
        description = self.ui.textEdit_descr_category.toPlainText()
        if title != '':
            new = CategoryEquipment()
            error, msg = new.save_category(title, description)
            if error == False:
                self.error_dialog.showMessage(f'Такое название уже существует {msg}')
            self.load_subcategory(True)
            self.ui.lineEdit_title_category.setText('')
            self.show_list_category()

    def delete_category(self):
        for i in range(self.ui.table_category.rowCount()):
            res = self.ui.table_category.cellWidget(i, 5).checkState()
            if res == Qt.Checked:
                delete = CategoryEquipment()
                delete.delete_category(self.ui.table_category.item(i, 0).text())
        self.load_category()

    def show_list_category(self):
        category, count = CategoryEquipment.load_all_category()
        self.ui.table_category.setRowCount(count)
        for i in range(count):
            timeupdate = category[i].time_updated
            if timeupdate is None:
                timeupdate = ""
            self.ui.table_category.setItem(i, 0, QTableWidgetItem(str(category[i].id)))
            self.ui.table_category.setItem(i, 1, QTableWidgetItem(str(category[i].title)))
            self.ui.table_category.setItem(i, 2, QTableWidgetItem(str(category[i].description)))
            self.ui.table_category.setItem(i, 3, QTableWidgetItem(str(timeupdate)))
            self.ui.table_category.setItem(i, 4, QTableWidgetItem(str(category[i].time_created)))
            self.ui.table_category.setCellWidget(i, 5, QCheckBox())

    def save_cell(self, col, row):
        checked = [1, 2]
        object = True
        if row in checked:
            print(f"col {col} row {row}")
            id = int(self.ui.table_category.item(col, 0).text())
            cell = self.ui.table_category.item(col, row).text()
            cells = CategoryEquipment()
            if row == 1:
                object, error, result = cells.update_title(id, title=cell)
            if row == 2:
                object, error, result = cells.update_title(id, description=cell)
            if object is False:
                self.ui.table_category.setItem(col, 1, QTableWidgetItem(str(result.title)))
            else:
                self.ui.table_category.setItem(col, 0, QTableWidgetItem(str(result.id)))
                self.ui.table_category.setItem(col, 3, QTableWidgetItem(str(result.time_updated)))
                self.ui.table_category.setItem(col, 4, QTableWidgetItem(str(result.time_created)))

    # ------------------------------------------------------------------------
    # Списко оборудования-----------------------------------------------------

    def load_equipment(self):
        pass


    def load_all_equipment(self):
        equip = Equipment.load_all()
        print(equip)


    def rest_qline(self):
        self.ui.lineEdit_title.setText('')
        self.ui.lineEdit_pcs.setText('')
        self.ui.lineEdit_price.setText('')

    def create_menubar(self):
        # file_menu = self.ui.menuBar().addMenu(self.tr("&File"))

        self.ui.quit_action = self.ui.menuFile.addAction(self.tr("&Quit"))
        self.ui.quit_action.triggered.connect(qApp.quit)
        #
        self.ui.about_action = self.ui.menuHelp.addAction(self.tr("&About"))
        self.ui.about_action.setShortcut(QKeySequence.HelpContents)
        self.ui.about_action.triggered.connect(self.about)
        self.ui.aboutQt_action = self.ui.menuHelp.addAction("&About Qt")
        self.ui.aboutQt_action.triggered.connect(qApp.aboutQt)
# ------------------------------------------------------------------------------
# -----Иницилизация приложения--------------------------------------------------

    @Slot()
    def about(self):
        QMessageBox.about(self, self.tr("About Books"),
            self.tr("<p>The <b>Books</b> example shows how to use Qt SQL classes "
                "with a model/view framework."))


def application():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    application()
