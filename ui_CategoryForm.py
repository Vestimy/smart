# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CategoryForm.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_CategoryForm(object):
    def setupUi(self, CategoryForm):
        if not CategoryForm.objectName():
            CategoryForm.setObjectName(u"CategoryForm")
        CategoryForm.resize(1043, 660)
        self.verticalLayout = QVBoxLayout(CategoryForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_category = QTableView(CategoryForm)
        self.table_category.setObjectName(u"table_category")
        self.table_category.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout.addWidget(self.table_category)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(CategoryForm)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_title_category = QLineEdit(CategoryForm)
        self.lineEdit_title_category.setObjectName(u"lineEdit_title_category")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_title_category)

        self.label_2 = QLabel(CategoryForm)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_desc_category = QLineEdit(CategoryForm)
        self.lineEdit_desc_category.setObjectName(u"lineEdit_desc_category")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_desc_category)


        self.verticalLayout.addLayout(self.formLayout)

        self.pushButton_save_category = QPushButton(CategoryForm)
        self.pushButton_save_category.setObjectName(u"pushButton_save_category")

        self.verticalLayout.addWidget(self.pushButton_save_category)


        self.retranslateUi(CategoryForm)

        QMetaObject.connectSlotsByName(CategoryForm)
    # setupUi

    def retranslateUi(self, CategoryForm):
        CategoryForm.setWindowTitle(QCoreApplication.translate("CategoryForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("CategoryForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_2.setText(QCoreApplication.translate("CategoryForm", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.pushButton_save_category.setText(QCoreApplication.translate("CategoryForm", u"Save", None))
    # retranslateUi

