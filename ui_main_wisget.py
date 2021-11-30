# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableView, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1003, 654)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tab_estimate = QTabWidget(Form)
        self.tab_estimate.setObjectName(u"tab_estimate")
        self.tab_estimate.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_2 = QHBoxLayout(self.tab)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table__new_new = QTableWidget(self.tab)
        if (self.table__new_new.columnCount() < 5):
            self.table__new_new.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table__new_new.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table__new_new.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table__new_new.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table__new_new.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table__new_new.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.table__new_new.rowCount() < 5):
            self.table__new_new.setRowCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table__new_new.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table__new_new.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table__new_new.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table__new_new.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table__new_new.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table__new_new.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table__new_new.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table__new_new.setItem(0, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table__new_new.setItem(3, 2, __qtablewidgetitem13)
        self.table__new_new.setObjectName(u"table__new_new")
        self.table__new_new.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout.addWidget(self.table__new_new)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 20, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.tab)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setMinimumSize(QSize(0, 0))
        self.btn_cancel.setBaseSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(self.tab)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_3.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.tab_estimate.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_title = QLineEdit(self.tab_2)
        self.lineEdit_title.setObjectName(u"lineEdit_title")

        self.horizontalLayout_7.addWidget(self.lineEdit_title)

        self.lineEdit_pcs = QLineEdit(self.tab_2)
        self.lineEdit_pcs.setObjectName(u"lineEdit_pcs")
        self.lineEdit_pcs.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.lineEdit_pcs)

        self.lineEdit_price = QLineEdit(self.tab_2)
        self.lineEdit_price.setObjectName(u"lineEdit_price")

        self.horizontalLayout_7.addWidget(self.lineEdit_price)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.pushButton_save = QPushButton(self.tab_2)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.477387, y1:0, x2:0.487437, y2:1, stop:0 rgba(255, 178, 102, 255), stop:0.316583 rgba(201, 117, 32, 255), stop:1 rgba(127, 78, 72, 255));\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.pushButton_save)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.tableWidget_Equipment = QTableWidget(self.tab_2)
        if (self.tableWidget_Equipment.columnCount() < 6):
            self.tableWidget_Equipment.setColumnCount(6)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_Equipment.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_Equipment.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_Equipment.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_Equipment.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_Equipment.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_Equipment.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        if (self.tableWidget_Equipment.rowCount() < 6):
            self.tableWidget_Equipment.setRowCount(6)
        self.tableWidget_Equipment.setObjectName(u"tableWidget_Equipment")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget_Equipment.sizePolicy().hasHeightForWidth())
        self.tableWidget_Equipment.setSizePolicy(sizePolicy1)
        self.tableWidget_Equipment.setShowGrid(True)
        self.tableWidget_Equipment.setRowCount(6)
        self.tableWidget_Equipment.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Equipment.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_Equipment.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.tableWidget_Equipment)

        self.tab_estimate.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalGroupBox = QGroupBox(self.tab_3)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.verticalGroupBox.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox.setSizePolicy(sizePolicy2)
        self.verticalGroupBox.setMinimumSize(QSize(500, 200))
        self.verticalLayout_7 = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.verticalGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_title_category = QLineEdit(self.verticalGroupBox)
        self.lineEdit_title_category.setObjectName(u"lineEdit_title_category")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_title_category)

        self.label_5 = QLabel(self.verticalGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.textEdit_descr_category = QTextEdit(self.verticalGroupBox)
        self.textEdit_descr_category.setObjectName(u"textEdit_descr_category")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textEdit_descr_category)


        self.verticalLayout_7.addLayout(self.formLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_save_category = QPushButton(self.verticalGroupBox)
        self.pushButton_save_category.setObjectName(u"pushButton_save_category")
        self.pushButton_save_category.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_4.addWidget(self.pushButton_save_category)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.table_category = QTableView(self.verticalGroupBox)
        self.table_category.setObjectName(u"table_category")

        self.verticalLayout_7.addWidget(self.table_category)


        self.verticalLayout_5.addWidget(self.verticalGroupBox)

        self.pushButton_delete_category_2 = QPushButton(self.tab_3)
        self.pushButton_delete_category_2.setObjectName(u"pushButton_delete_category_2")

        self.verticalLayout_5.addWidget(self.pushButton_delete_category_2)

        self.line = QFrame(self.tab_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.tab_estimate.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_6 = QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(self.tab_4)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_title_subcategory = QLineEdit(self.groupBox)
        self.lineEdit_title_subcategory.setObjectName(u"lineEdit_title_subcategory")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_title_subcategory)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.textEdit_descr_subcategory = QTextEdit(self.groupBox)
        self.textEdit_descr_subcategory.setObjectName(u"textEdit_descr_subcategory")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.textEdit_descr_subcategory)

        self.comboBox_subcategory = QComboBox(self.groupBox)
        self.comboBox_subcategory.setObjectName(u"comboBox_subcategory")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.comboBox_subcategory)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_8)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.pushButton_subcategory = QPushButton(self.tab_4)
        self.pushButton_subcategory.setObjectName(u"pushButton_subcategory")
        self.pushButton_subcategory.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_6.addWidget(self.pushButton_subcategory)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.tab_estimate.addTab(self.tab_4, "")

        self.verticalLayout_2.addWidget(self.tab_estimate)


        self.retranslateUi(Form)

        self.tab_estimate.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.table__new_new.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem1 = self.table__new_new.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem2 = self.table__new_new.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem3 = self.table__new_new.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem4 = self.table__new_new.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem5 = self.table__new_new.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem6 = self.table__new_new.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem7 = self.table__new_new.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem8 = self.table__new_new.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem9 = self.table__new_new.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));

        __sortingEnabled = self.table__new_new.isSortingEnabled()
        self.table__new_new.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.table__new_new.item(0, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"4", None));
        ___qtablewidgetitem11 = self.table__new_new.item(0, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"5", None));
        ___qtablewidgetitem12 = self.table__new_new.item(0, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"vfdv", None));
        ___qtablewidgetitem13 = self.table__new_new.item(3, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"dfv", None));
        self.table__new_new.setSortingEnabled(__sortingEnabled)

        self.btn_cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.tab_estimate.setTabText(self.tab_estimate.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0412\u043e", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430", None))
        self.pushButton_save.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        ___qtablewidgetitem14 = self.tableWidget_Equipment.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"Id", None));
        ___qtablewidgetitem15 = self.tableWidget_Equipment.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem16 = self.tableWidget_Equipment.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e", None));
        ___qtablewidgetitem17 = self.tableWidget_Equipment.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430 \u0437\u0430 \u0435\u0434", None));
        ___qtablewidgetitem18 = self.tableWidget_Equipment.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u043b\u0435\u043d\u0435\u0435 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem19 = self.tableWidget_Equipment.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u043d\u0430\u0438\u044f", None));
        self.tab_estimate.setTabText(self.tab_estimate.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.pushButton_save_category.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_delete_category_2.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.tab_estimate.setTabText(self.tab_estimate.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.pushButton_subcategory.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tab_estimate.setTabText(self.tab_estimate.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
    # retranslateUi

