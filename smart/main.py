import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLineEdit, QPushButton, QTableWidgetItem, \
    QErrorMessage, QTableWidget, QCheckBox, QTableView, QMessageBox, QToolBar, QAbstractItemView, QHeaderView, \
    QDataWidgetMapper, QStyledItemDelegate
from PySide6.QtCore import QFile, Qt, QRegularExpression, Slot
from PySide6.QtGui import QRegularExpressionValidator, QIntValidator, QDoubleValidator, QKeySequence, QStandardItemModel
from ui_mainwindow import Ui_MainWindow
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRelationalDelegate, QSqlQuery
import createddb

from smart.design.ui_main_wisget import Ui_Form
from smart.design.ui_CategoryForm import Ui_CategoryForm
from smart.design.ui_SubCategoryForm import Ui_SubCategoryForm
from smart.design.ui_EquipmentForm import Ui_EquipmentForm
import config
from decimal import Decimal


class CategoryWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CategoryWidget, self).__init__(parent)
        self.ui_category = Ui_CategoryForm()
        self.ui_category.setupUi(self)
        self.setWindowTitle('Категория')
        self.init_model()
        self.q = QSqlQuery()
        self.ui_category.table_category.setModel(self.model)

        self.ui_category.table_category.setSortingEnabled(True)

        self.setHeader()

        self.setColumnHidden()

        self.settings_table()

        self.ui_category.pushButton_save_category.clicked.connect(self.setCategory)

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

    def setCategory(self):
        title = self.ui_category.lineEdit_title_category.text()
        description = self.ui_category.lineEdit_desc_category.text()
        self.q.prepare("INSERT INTO categoryequipment (title, description) "
                       "VALUES (?, ?)")
        self.q.addBindValue(title)
        self.q.addBindValue(description)
        if self.q.exec():
            self.ui_category.lineEdit_title_category.setText('')
            self.ui_category.lineEdit_desc_category.setText('')
        self.model.select()


class SubCategoryWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SubCategoryWidget, self).__init__(parent)
        self.ui_sub_category = Ui_SubCategoryForm()
        self.ui_sub_category.setupUi(self)

        self.setWindowTitle('Подкатегория')
        self.ui_sub_category.table_sub_category.setSortingEnabled(True)

        self.init_model()

        self.q = QSqlQuery()

        self.ui_sub_category.table_sub_category.setModel(self.model)
        self.ui_sub_category.table_sub_category.setItemDelegate(
            QSqlRelationalDelegate(self.ui_sub_category.table_sub_category))

        self.setHeader()
        self.settings_table()
        self.ui_sub_category.pushButton_sub_category.clicked.connect(self.setSubCategory)

        self.qwer()

    def init_model(self):
        self.model = QSqlRelationalTableModel(self.ui_sub_category.table_sub_category)
        self.model.setTable("subcategoryequipment")

        self.category_idx = self.model.fieldIndex("categoryequipmentid")
        self.model.setRelation(self.category_idx, QSqlRelation('categoryequipment', 'id', 'title'))

        self.model.setSort(self.category_idx, QtCore.Qt.SortOrder.AscendingOrder)
        self.model.select()

    def setHeader(self):
        self.model.setHeaderData(self.model.fieldIndex("id"), Qt.Horizontal, self.tr("ID"))
        self.model.setHeaderData(self.model.fieldIndex("title"), Qt.Horizontal, self.tr("Название"))
        self.model.setHeaderData(self.model.fieldIndex("description"), Qt.Horizontal, self.tr("Описание"))
        self.model.setHeaderData(self.model.fieldIndex("time_created"), Qt.Horizontal, self.tr("Дата создания"))
        self.model.setHeaderData(self.model.fieldIndex("time_updated"), Qt.Horizontal, self.tr("Дата обновления"))
        self.model.setHeaderData(self.category_idx, Qt.Horizontal, self.tr("Категория"))

    def settings_table(self):
        self.ui_sub_category.table_sub_category.setColumnHidden(self.model.fieldIndex("id"), True)
        self.ui_sub_category.table_sub_category.setColumnHidden(self.model.fieldIndex("time_created"), True)
        self.ui_sub_category.table_sub_category.setColumnHidden(self.model.fieldIndex("time_updated"), True)
        self.ui_sub_category.table_sub_category.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui_sub_category.table_sub_category.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui_sub_category.table_sub_category.resizeColumnsToContents()
        self.ui_sub_category.table_sub_category.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def qwer(self):
        self.model_combo = QSqlTableModel()
        self.model_combo.setTable('categoryequipment')

        column = self.model_combo.fieldIndex('title')

        self.model_combo.setSort(column, QtCore.Qt.SortOrder.AscendingOrder)
        self.model_combo.select()

        self.ui_sub_category.lineEdit_categoryid_sub_category.setModel(self.model_combo)
        self.ui_sub_category.lineEdit_categoryid_sub_category.setModelColumn(column)

    def setSubCategory(self):
        title = self.ui_sub_category.lineEdit_title_sub_category.text()
        description = self.ui_sub_category.lineEdit_desc_sub_category.text()
        categoryequipmentid = self.model_combo.index(
            self.ui_sub_category.lineEdit_categoryid_sub_category.currentIndex(),
            self.model_combo.fieldIndex('id')).data()
        self.q.prepare("INSERT INTO subcategoryequipment (title, description, categoryequipmentid) "
                       "VALUES (?, ?, ?)")
        self.q.addBindValue(title)
        self.q.addBindValue(description)
        self.q.addBindValue(categoryequipmentid)
        if self.q.exec():
            self.ui_sub_category.lineEdit_title_sub_category.setText('')
            self.ui_sub_category.lineEdit_desc_sub_category.setText('')
        self.model.select()


class EquipmentWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(EquipmentWidget, self).__init__(parent)
        self.ui_equipment = Ui_EquipmentForm()
        self.ui_equipment.setupUi(self)
        self.setWindowTitle('Список оборудования')

        self.init_model()
        self.ui_equipment.table_equipment.setSortingEnabled(True)
        self.ui_equipment.table_equipment.setModel(self.model)
        self.ui_equipment.table_equipment.setItemDelegate(
            QSqlRelationalDelegate(self.ui_equipment.table_equipment)
        )
        self.q = QSqlQuery()
        self.setHeader()
        self.settings_table()

        self.ui_equipment.pushButton_save_equipment.clicked.connect(self.setEquipment)

        self.qwer()

    def init_model(self):
        self.model = QSqlRelationalTableModel(self.ui_equipment.table_equipment)
        self.model.setTable('equipment')

        self.subcategory_idx = self.model.fieldIndex('subcategoryequipmentid')

        self.model.setRelation(self.subcategory_idx, QSqlRelation('subcategoryequipment', 'id', 'title'))
        self.model.select()

    def setHeader(self):
        self.model.setHeaderData(self.model.fieldIndex("id"), Qt.Horizontal, self.tr("ID"))
        self.model.setHeaderData(self.model.fieldIndex("title"), Qt.Horizontal, self.tr("Название"))
        self.model.setHeaderData(self.model.fieldIndex("pcs"), Qt.Horizontal, self.tr("Кол-во"))
        self.model.setHeaderData(self.model.fieldIndex("price"), Qt.Horizontal, self.tr("Цена"))
        self.model.setHeaderData(self.model.fieldIndex("time_created"), Qt.Horizontal, self.tr("Дата создания"))
        self.model.setHeaderData(self.model.fieldIndex("time_updated"), Qt.Horizontal, self.tr("Дата обновления"))
        self.model.setHeaderData(self.subcategory_idx, Qt.Horizontal, self.tr("Категория"))

    def settings_table(self):
        self.ui_equipment.table_equipment.setColumnHidden(self.model.fieldIndex("id"), True)
        self.ui_equipment.table_equipment.setColumnHidden(self.model.fieldIndex("time_created"), True)
        self.ui_equipment.table_equipment.setColumnHidden(self.model.fieldIndex("time_updated"), True)
        self.ui_equipment.table_equipment.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui_equipment.table_equipment.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui_equipment.table_equipment.resizeColumnsToContents()
        self.ui_equipment.table_equipment.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def qwer(self):
        self.model_combo = QSqlTableModel()
        self.model_combo.setTable('subcategoryequipment')

        column = self.model_combo.fieldIndex('title')
        self.model_combo.setSort(column, QtCore.Qt.SortOrder.AscendingOrder)
        self.model_combo.select()

        self.ui_equipment.comboBox_subcategory_equipment.setModel(self.model_combo)
        self.ui_equipment.comboBox_subcategory_equipment.setModelColumn(column)

    def setEquipment(self):
        title = self.ui_equipment.lineEdit_title_equipment.text()
        pcs = self.ui_equipment.lineEdit_pcs_equipment.text()
        price = self.ui_equipment.lineEdit_price_equipment.text()
        subcategoryequipmentid = self.model_combo.index(
            self.ui_equipment.comboBox_subcategory_equipment.currentIndex(),
            self.model_combo.fieldIndex('id')).data()
        self.q.prepare("INSERT INTO equipment (title, pcs, price, subcategoryequipmentid) "
                       "VALUES (?, ?, ?, ?)")
        self.q.addBindValue(title)
        self.q.addBindValue(pcs)
        self.q.addBindValue(price)
        self.q.addBindValue(subcategoryequipmentid)
        if self.q.exec():
            self.ui_equipment.lineEdit_title_equipment.setText('')
            self.ui_equipment.lineEdit_pcs_equipment.setText('')
            self.ui_equipment.lineEdit_price_equipment.setText('')
            self.model.select()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.config = config.Config()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Иницилизация базы данных
        db = createddb.init_db()
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
        self.sub_equipment.resize(self.size() / 2)
        self.sub_equipment.show()

    def show_sub_category(self):
        self.sub_category = QtWidgets.QMdiSubWindow()
        self.sub_category.setWidget(SubCategoryWidget())
        self.mdiArea.addSubWindow(self.sub_category)
        self.size()
        self.sub_category.resize(self.size() / 2)
        self.sub_category.show()

    def show_category(self):
        self.category = QtWidgets.QMdiSubWindow()
        self.category.setWidget(CategoryWidget())
        self.mdiArea.addSubWindow(self.category)
        self.category.resize(self.size() / 2)
        self.category.show()

    def create_menubar(self):
        self.ui.categorys = self.ui.menuFile.addAction(self.tr("&Категория"))
        self.ui.category = self.ui.menubar.addAction(self.tr("&Категория"))
        self.ui.category.triggered.connect(self.show_category)
        self.ui.categorys.triggered.connect(self.show_category)

        self.ui.subcategory = self.ui.menuFile.addAction(self.tr("Sub Категория"))
        self.ui.subcategory = self.ui.menubar.addAction(self.tr("Sub Категория"))
        self.ui.subcategory.triggered.connect(self.show_sub_category)

        self.ui.equipment = self.ui.menuFile.addAction(self.tr("Список оборудования"))
        self.ui.equipment = self.ui.menubar.addAction(self.tr("Список оборудования"))
        self.ui.equipment.triggered.connect(self.show_equipment)

        # self.ui.new = self.ui.menuFile.addAction(self.tr("&New"))

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
