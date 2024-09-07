# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QObject, QEvent, QUrl, Qt
from PySide6.QtGui import QDesktopServices

from videotrans.configure import config


class LineEditClickFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            # 在这里处理点击事件
            if obj.text().strip():
                QDesktopServices.openUrl(QUrl.fromLocalFile(obj.text().strip()))
            # 可以在这里执行任何函数或方法
            return True  # 表示事件已处理，不再传递
        # 其他事件交给基类处理，保持默认行为
        return False


class Ui_separateform(object):
    def setupUi(self, separateform):
        self.has_done=False
        separateform.setObjectName("separateform")
        separateform.setWindowModality(QtCore.Qt.NonModal)
        separateform.resize(600, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(separateform.sizePolicy().hasHeightForWidth())
        separateform.setSizePolicy(sizePolicy)
        separateform.setMaximumSize(QtCore.QSize(600, 300))

        self.showtips = QtWidgets.QLabel(separateform)
        self.showtips.setGeometry(QtCore.QRect(10, 130, 500, 50))
        self.showtips.setStyleSheet("""color:#eeeeee""")
        # 开始分离
        self.showtips.setObjectName("showtips")
        self.showtips.setText(
            "如果文件过大，或频繁分离出错，建议选择独立分离工具，比如uvr5或vocal-separate\ngithub.com/Anjok07/ultimatevocalremovergui/releases\ngithub.com/jianchang512/vocal-separate/releases")

        self.set = QtWidgets.QPushButton(separateform)
        self.set.setGeometry(QtCore.QRect(170, 200, 141, 35))
        self.set.setMinimumSize(QtCore.QSize(0, 35))
        # 开始分离
        self.set.setObjectName("set")
        self.set.setCursor(Qt.PointingHandCursor)

        # 创建一个布局
        self.layoutWidget = QtWidgets.QWidget(separateform)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 16, 471, 80))
        self.layoutWidget.setObjectName("layoutWidget")
        # 创建表单布局
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        # 创建垂直布局
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # 选择文件按钮
        self.selectfile = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectfile.sizePolicy().hasHeightForWidth())
        self.selectfile.setSizePolicy(sizePolicy)
        self.selectfile.setMinimumSize(QtCore.QSize(100, 35))
        self.selectfile.setObjectName("selectfile")
        self.selectfile.setCursor(Qt.PointingHandCursor)
        # 垂直布局中添加一个选择文件按钮
        self.verticalLayout.addWidget(self.selectfile)

        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 35))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        # 加到表达中
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)

        # 垂直布局2中添加一个文本框用于显示选择的文件路径
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fromfile = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fromfile.sizePolicy().hasHeightForWidth())
        self.fromfile.setSizePolicy(sizePolicy)
        self.fromfile.setMinimumSize(QtCore.QSize(0, 35))
        self.fromfile.setReadOnly(True)
        self.fromfile.setObjectName("fromfile")
        self.fromfile.setPlaceholderText("显示选择的音视频文件" if config.defaulelang == 'zh' else "show file where you selected")
        self.verticalLayout_2.addWidget(self.fromfile)

        self.url = QtWidgets.QPushButton(self.layoutWidget)
        self.url.setMinimumSize(QtCore.QSize(0, 35))
        self.url.setObjectName("url")
        self.url.setStyleSheet("""background-color:transparent""")
        self.url.setCursor(Qt.PointingHandCursor)
        self.url.setToolTip('点击打开结果文件夹' if config.defaulelang == 'zh' else 'Open target dir')
        # self.url.setReadOnly(True)

        self.click_filter = LineEditClickFilter()
        self.url.installEventFilter(self.click_filter)
        self.verticalLayout_2.addWidget(self.url)

        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)

        self.logs = QtWidgets.QLabel(separateform)
        self.logs.setGeometry(QtCore.QRect(30, 250, 441, 16))
        self.logs.setText("")
        self.logs.setObjectName("logs")

        self.retranslateUi(separateform)
        QtCore.QMetaObject.connectSlotsByName(separateform)

    def retranslateUi(self, separateform):
        separateform.setWindowTitle('分离人声和背景音' if config.defaulelang == 'zh' else "Separte vocal and instrument")
        self.set.setText('立即开始' if config.defaulelang == 'zh' else "Start Separate")
        self.label_2.setText('分离结果保存到' if config.defaulelang == 'zh' else "Outdir click open")
        self.selectfile.setText('选择音视频文件' if config.defaulelang == 'zh' else "Select file")
