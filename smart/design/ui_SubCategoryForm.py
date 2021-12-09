# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SubCategoryForm.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFormLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_SubCategoryForm(object):
    def setupUi(self, SubCategoryForm):
        if not SubCategoryForm.objectName():
            SubCategoryForm.setObjectName(u"SubCategoryForm")
        SubCategoryForm.setWindowModality(Qt.ApplicationModal)
        SubCategoryForm.resize(1043, 660)
        self.verticalLayout = QVBoxLayout(SubCategoryForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_sub_category = QTableView(SubCategoryForm)
        self.table_sub_category.setObjectName(u"table_sub_category")
        self.table_sub_category.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout.addWidget(self.table_sub_category)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(SubCategoryForm)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_title_sub_category = QLineEdit(SubCategoryForm)
        self.lineEdit_title_sub_category.setObjectName(u"lineEdit_title_sub_category")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_title_sub_category)

        self.label_2 = QLabel(SubCategoryForm)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_desc_sub_category = QLineEdit(SubCategoryForm)
        self.lineEdit_desc_sub_category.setObjectName(u"lineEdit_desc_sub_category")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_desc_sub_category)

        self.label_3 = QLabel(SubCategoryForm)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_categoryid_sub_category = QComboBox(SubCategoryForm)
        self.lineEdit_categoryid_sub_category.setObjectName(u"lineEdit_categoryid_sub_category")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_categoryid_sub_category)


        self.verticalLayout.addLayout(self.formLayout)

        self.pushButton_sub_category = QPushButton(SubCategoryForm)
        self.pushButton_sub_category.setObjectName(u"pushButton_sub_category")

        self.verticalLayout.addWidget(self.pushButton_sub_category)


        self.retranslateUi(SubCategoryForm)

        QMetaObject.connectSlotsByName(SubCategoryForm)
    # setupUi

    def retranslateUi(self, SubCategoryForm):
        SubCategoryForm.setWindowTitle(QCoreApplication.translate("SubCategoryForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("SubCategoryForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_2.setText(QCoreApplication.translate("SubCategoryForm", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.label_3.setText(QCoreApplication.translate("SubCategoryForm", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.pushButton_sub_category.setText(QCoreApplication.translate("SubCategoryForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

