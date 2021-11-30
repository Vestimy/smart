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

from ui_main_wisget import Ui_Form
from ui_CategoryForm import Ui_CatalogForm


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


class CatalogEquipment(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CatalogEquipment, self).__init__(parent)
        self.lay = QtWidgets.QVBoxLayout(self)
        # self.lay.addWidget(self.table_category)
        self.model = QSqlTableModel(self)
        self.model.setTable('categoryequipment')
        self.model.select()
        self.table_category.setModel(self.model)
        self.push = QPushButton('Save')
        self.lay.addWidget(self.push)
        self.table_category.setColumnHidden(self.model.fieldIndex("id"), True)
        self.table_category.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_category.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_category.resizeColumnsToContents()
        self.table_category.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.model.setHeaderData(self.model.fieldIndex("id"), Qt.Horizontal, self.tr("ID"))
        self.model.setHeaderData(self.model.fieldIndex("title"), Qt.Horizontal, self.tr("Название"))
        self.model.setHeaderData(self.model.fieldIndex("description"), Qt.Horizontal, self.tr("Описание"))
        self.model.setHeaderData(self.model.fieldIndex("time_created"), Qt.Horizontal, self.tr("Дата создания"))
        self.model.setHeaderData(self.model.fieldIndex("time_updated"), Qt.Horizontal, self.tr("Дата обновления"))

        self.table_category.setColumnHidden(self.model.fieldIndex("id"), True)
        self.table_category.setColumnHidden(self.model.fieldIndex("time_created"), True)
        self.table_category.setColumnHidden(self.model.fieldIndex("time_updated"), True)

        self.push.clicked.connect(self.load_save)
        # self.load_save()

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.model)
        # self.mapper.setItemDelegate(BookDelegate(self))
        self.mapper.addMapping(self.titleEdit, self.model.fieldIndex("title"))
        self.mapper.addMapping(self.yearEdit, self.model.fieldIndex("year"))
        self.mapper.addMapping(self.authorEdit, self.author_idx)
        self.mapper.addMapping(self.genreEdit, self.genre_idx)
        self.mapper.addMapping(self.ratingEdit, self.model.fieldIndex("rating"))

    def load_save(self):
        print('new!')
        title = "New1"
        description = "Description"
        insertDataQuery = QSqlQuery()
        insertDataQuery.addBindValue(title)
        insertDataQuery.addBindValue(description)
        insertDataQuery.exec()


class SubcategoryEquipment(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SubcategoryEquipment, self).__init__(parent)
        self.lay = QtWidgets.QVBoxLayout(self)
        self.table_category = QtWidgets.QTableView()
        self.lay.addWidget(self.table_category)
        self.model = QSqlRelationalTableModel(self)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.setTable('subcategoryequipment')

        categoryequipmentid = self.model.fieldIndex("categoryequipmentid")

        self.model.setRelation(categoryequipmentid, QSqlRelation("categoryequipment", "id", "title"))

        self.model.setHeaderData(self.model.fieldIndex("id"), Qt.Horizontal, self.tr("Id"))
        self.model.setHeaderData(self.model.fieldIndex("title"), Qt.Horizontal, self.tr("Название"))
        self.model.setHeaderData(self.model.fieldIndex("description"), Qt.Horizontal, self.tr("Описание"))
        self.model.setHeaderData(categoryequipmentid, Qt.Horizontal, self.tr("Подкатегория"))

        self.model.select()

        self.table_category.setModel(self.model)

        self.table_category.setItemDelegate(QSqlRelationalDelegate(self.table_category))
        self.table_category.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.AnyKeyPressed)

        self.table_category.setColumnHidden(self.model.fieldIndex("id"), True)
        self.table_category.setColumnHidden(self.model.fieldIndex("time_created"), True)
        self.table_category.setColumnHidden(self.model.fieldIndex("time_updated"), True)
        self.table_category.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_category.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_category.resizeColumnsToContents()
        self.table_category.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Remember the indexes of the columns:


class MainQwidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainQwidget, self).__init__(parent)
        self.qqq = Ui_Form()
        self.qqq.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        createddb.init_db()
        # Menu Bar
        self.create_menubar()
        self.mdiArea = QtWidgets.QMdiArea()

        self.setCentralWidget(self.mdiArea)

    def show_sub4(self):
        self.sub4 = QtWidgets.QMdiSubWindow()
        self.sub4.setWidget(SubcategoryEquipment())
        self.mdiArea.addSubWindow(self.sub4)
        size = self.size() / 2
        self.sub4.resize(size)
        self.sub4.show()

    def show_sub3(self):
        self.sub3 = QtWidgets.QMdiSubWindow()
        self.sub3.setWidget(MainQwidget())
        self.mdiArea.addSubWindow(self.sub3)

        size = self.size() / 2
        self.sub3.resize(size)
        self.sub3.show()

    def show_sub1(self):
        self.sub1 = QtWidgets.QMdiSubWindow()
        self.sub1.setWidget(CatalogEquipment())
        self.mdiArea.addSubWindow(self.sub1)
        self.sub1.show()

    def create_menubar(self):
        # file_menu = self.ui.menuBar().addMenu(self.tr("&File"))

        self.ui.category = self.ui.menuFile.addAction(self.tr("&Категория"))
        self.ui.category.triggered.connect(self.show_sub1)
        self.ui.subcategory = self.ui.menuFile.addAction(self.tr("&Sub Категория"))
        self.ui.subcategory.triggered.connect(self.show_sub4)
        self.ui.new = self.ui.menuFile.addAction(self.tr("&New"))
        self.ui.new.triggered.connect(self.show_sub3)
        self.ui.quit_action = self.ui.menuFile.addAction(self.tr("&Quit"))
        self.ui.quit_action.triggered.connect(qApp.quit)
        #
        self.ui.about_action = self.ui.menuHelp.addAction(self.tr("&About"))
        self.ui.about_action.setShortcut(QKeySequence.HelpContents)
        self.ui.about_action.triggered.connect(self.about)
        self.ui.aboutQt_action = self.ui.menuHelp.addAction("&About Qt")
        self.ui.aboutQt_action.triggered.connect(qApp.aboutQt)

    def create_toolbar(self):
        self.too = QToolBar()

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
    window.resize(window.sizeHint())
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    application()
