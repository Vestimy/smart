import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLineEdit, QPushButton, QTableWidgetItem, \
    QErrorMessage, QTableWidget, QCheckBox, QTableView, QMessageBox, QToolBar, QAbstractItemView, QHeaderView, \
    QDataWidgetMapper
from PySide6.QtCore import QFile, Qt, QRegularExpression, Slot
from PySide6.QtGui import QRegularExpressionValidator, QIntValidator, QDoubleValidator, QKeySequence
from ui_mainwindow import Ui_MainWindow
from PySide6 import QtCore, QtWidgets
from PySide6.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRelationalDelegate, QSqlQuery
import createddb

from smart.design.ui_main_wisget import Ui_Form
from smart.design.ui_CategoryForm import Ui_CategoryForm
from smart.design.ui_SubCategoryForm import Ui_SubCategoryForm
from smart.design.ui_EquipmentForm import Ui_EquipmentForm
import config


class CategoryWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CategoryWidget, self).__init__(parent)
        self.ui_category = Ui_CategoryForm()
        self.ui_category.setupUi(self)
        self.setWindowTitle('Категория')
        self.init_model()

        self.ui_category.table_category.setModel(self.model)

        self.setHeader()

        self.setColumnHidden()

        self.settings_table()

    def init_model(self):
        self.model = QSqlTableModel(self)
        self.model.setTable("categoryequipment")
        self.model.select()

    def setHeader(self):
        self.model.setHeaderData(self.model.fieldIndex("id"), Qt.Horizontal, self.tr("ID"))
        self.model.setHeaderData(self.model.fieldIndex("title"), Qt.Horizontal, self.tr("Название"))
        self.model.setHeaderData(self.model.fieldIndex("description"), Qt.Horizontal, self.tr("Описание"))
        self.model.setHeaderData(self.model.fieldIndex("time_created"), Qt.Horizontal, self.tr("Дата создания"))
        self.model.setHeaderData(self.model.fieldIndex("time_updated"), Qt.Horizontal, self.tr("Дата обновления"))

    def setColumnHidden(self):
        self.ui_category.table_category.setColumnHidden(self.model.fieldIndex("id"), True)
        self.ui_category.table_category.setColumnHidden(self.model.fieldIndex("time_created"), True)
        self.ui_category.table_category.setColumnHidden(self.model.fieldIndex("time_updated"), True)

    def settings_table(self):
        self.ui_category.table_category.setColumnHidden(self.model.fieldIndex("id"), True)
        self.ui_category.table_category.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui_category.table_category.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui_category.table_category.resizeColumnsToContents()
        self.ui_category.table_category.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


class SubCategoryWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SubCategoryWidget, self).__init__(parent)
        self.ui_sub_category = Ui_SubCategoryForm()
        self.ui_sub_category.setupUi(self)

        self.setWindowTitle('Подкатегория')

        self.init_model()

        self.ui_sub_category.table_sub_category.setModel(self.model)

    def init_model(self):
        self.model = QSqlTableModel(self)
        self.model.setTable("subcategoryequipment")
        self.model.select()


class EquipmentWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(EquipmentWidget, self).__init__(parent)
        self.ui_equipment = Ui_EquipmentForm()
        self.ui_equipment.setupUi(self)
        self.setWindowTitle('Список оборудования')


class MainQwidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainQwidget, self).__init__(parent)
        self.qqq = Ui_Form()
        self.qqq.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.config = config.Config()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Иницилизация базы данных
        createddb.init_db()
        # Окно в окне
        self.mdiArea = QtWidgets.QMdiArea()
        self.setCentralWidget(self.mdiArea)
        # Menu Bar
        self.create_menubar()

    def show_equipment(self):
        self.sub_equipment = QtWidgets.QMdiSubWindow()
        self.sub_equipment.setWidget(EquipmentWidget())
        self.mdiArea.addSubWindow(self.sub_equipment)
        self.size()
        self.sub_equipment.resize(self.sizeHint())
        self.sub_equipment.show()

    def show_sub_category(self):
        self.sub_category = QtWidgets.QMdiSubWindow()
        self.sub_category.setWidget(SubCategoryWidget())
        self.mdiArea.addSubWindow(self.sub_category)
        self.size()
        self.sub_category.resize(self.sizeHint())
        self.sub_category.show()

    def show_category(self):
        self.category = QtWidgets.QMdiSubWindow()
        self.category.setWidget(CategoryWidget())
        self.mdiArea.addSubWindow(self.category)
        self.category.resize(self.size() / 2)
        self.category.show()

    def create_menubar(self):
        self.ui.category = self.ui.menuFile.addAction(self.tr("&Категория"))
        self.ui.category = self.ui.menubar.addAction(self.tr("&Категория"))
        self.ui.category.triggered.connect(self.show_category)

        self.ui.subcategory = self.ui.menuFile.addAction(self.tr("Sub Категория"))
        self.ui.subcategory = self.ui.menubar.addAction(self.tr("Sub Категория"))
        self.ui.subcategory.triggered.connect(self.show_sub_category)

        self.ui.equipment = self.ui.menuFile.addAction(self.tr("Таблица"))
        self.ui.equipment = self.ui.menubar.addAction(self.tr("Таблица"))
        self.ui.equipment.triggered.connect(self.show_equipment)

        self.ui.new = self.ui.menuFile.addAction(self.tr("&New"))

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

    def closeEvent(self, event):
        if not self.isMaximized():
            self.config.set_windowsize(self.width(), self.height())
        self.config.set_Maximized(self.isMaximized())


def application():
    app = QApplication(sys.argv)

    window = MainWindow()
    a, b = window.config.get_windowsize()
    window.resize(a, b)
    if window.config.get_Maximized():
        window.showMaximized()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    application()
