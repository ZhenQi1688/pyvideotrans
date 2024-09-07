# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatgpt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets

from videotrans.configure import config


class Ui_chatgptform(object):
    def setupUi(self, chatgptform):
        self.has_done=False
        chatgptform.setObjectName("chatgptform")
        chatgptform.setWindowModality(QtCore.Qt.NonModal)
        chatgptform.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chatgptform.sizePolicy().hasHeightForWidth())
        chatgptform.setSizePolicy(sizePolicy)
        chatgptform.setMaximumSize(QtCore.QSize(600, 600))

        self.label_0 = QtWidgets.QLabel(chatgptform)
        self.label_0.setGeometry(QtCore.QRect(10, 10, 580, 35))
        self.label_0.setText(
            '兼容ChatGPT接口的AI也在此使用' if config.defaulelang == 'zh' else 'AIs compatible with the ChatGPT also used here')

        self.label = QtWidgets.QLabel(chatgptform)
        self.label.setGeometry(QtCore.QRect(10, 45, 130, 35))
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setObjectName("label")
        self.chatgpt_api = QtWidgets.QLineEdit(chatgptform)
        self.chatgpt_api.setGeometry(QtCore.QRect(150, 45, 431, 35))
        self.chatgpt_api.setMinimumSize(QtCore.QSize(0, 35))
        self.chatgpt_api.setObjectName("chatgpt_api")

        self.label_2 = QtWidgets.QLabel(chatgptform)
        self.label_2.setGeometry(QtCore.QRect(10, 95, 130, 35))
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.chatgpt_key = QtWidgets.QLineEdit(chatgptform)
        self.chatgpt_key.setGeometry(QtCore.QRect(150, 95, 431, 35))
        self.chatgpt_key.setMinimumSize(QtCore.QSize(0, 35))
        self.chatgpt_key.setObjectName("chatgpt_key")

        self.label_3 = QtWidgets.QLabel(chatgptform)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 121, 16))
        self.label_3.setObjectName("label_3")
        self.chatgpt_model = QtWidgets.QComboBox(chatgptform)
        self.chatgpt_model.setGeometry(QtCore.QRect(150, 145, 431, 35))
        self.chatgpt_model.setMinimumSize(QtCore.QSize(0, 35))
        self.chatgpt_model.setObjectName("chatgpt_model")

        self.label_allmodels = QtWidgets.QLabel(chatgptform)
        self.label_allmodels.setGeometry(QtCore.QRect(10, 180, 571, 21))
        self.label_allmodels.setObjectName("label_allmodels")
        self.label_allmodels.setText(
            '填写所有可用模型，以英文逗号分隔，填写后可在上方选择' if config.defaulelang == 'zh' else 'Fill in all available models, separated by commas. After filling in, you can select them above')

        self.edit_allmodels = QtWidgets.QPlainTextEdit(chatgptform)
        self.edit_allmodels.setGeometry(QtCore.QRect(10, 210, 571, 100))
        self.edit_allmodels.setObjectName("edit_allmodels")

        self.label_4 = QtWidgets.QLabel(chatgptform)
        self.label_4.setGeometry(QtCore.QRect(10, 315, 571, 21))
        self.label_4.setObjectName("label_4")

        self.chatgpt_template = QtWidgets.QPlainTextEdit(chatgptform)
        self.chatgpt_template.setGeometry(QtCore.QRect(10, 340, 571, 151))
        self.chatgpt_template.setObjectName("chatgpt_template")

        self.set_chatgpt = QtWidgets.QPushButton(chatgptform)
        self.set_chatgpt.setGeometry(QtCore.QRect(10, 520, 93, 35))
        self.set_chatgpt.setMinimumSize(QtCore.QSize(0, 35))
        self.set_chatgpt.setObjectName("set_chatgpt")

        self.test_chatgpt = QtWidgets.QPushButton(chatgptform)
        self.test_chatgpt.setGeometry(QtCore.QRect(130, 525, 93, 30))
        self.test_chatgpt.setMinimumSize(QtCore.QSize(0, 30))
        self.test_chatgpt.setObjectName("test_chatgpt")

        self.retranslateUi(chatgptform)
        QtCore.QMetaObject.connectSlotsByName(chatgptform)

    def retranslateUi(self, chatgptform):
        chatgptform.setWindowTitle("ChatGPT API")
        self.label_3.setText('选择模型' if config.defaulelang == 'zh' else "Model")
        self.chatgpt_template.setPlaceholderText("prompt")
        self.label_4.setText(
            "{lang}代表目标语言名称，不要删除。" if config.defaulelang == 'zh' else "{lang} represents the target language name, do not delete it.")
        self.set_chatgpt.setText('保存' if config.defaulelang == 'zh' else "Save")
        self.test_chatgpt.setText('测试..' if config.defaulelang == 'zh' else "Test..")
        self.chatgpt_api.setPlaceholderText(
            '若使用OpenAI官方接口，无需填写;第三方api在此填写' if config.defaulelang == 'zh' else 'If using the official OpenAI interface, there is no need to fill it out; Fill in the third-party API here')
        self.chatgpt_api.setToolTip(
            '若使用OpenAI官方接口，无需填写;第三方api在此填写' if config.defaulelang == 'zh' else 'If using the official OpenAI interface, there is no need to fill it out; Fill in the third-party API here')
        self.chatgpt_key.setPlaceholderText("Secret key")
        self.chatgpt_key.setToolTip(
            "必须是付费账号，免费账号频率受限无法使用" if config.defaulelang == 'zh' else 'Must be a paid account, free account frequency is limited and cannot be used')
        self.label.setText("API URL")
        self.label_2.setText("SK")
