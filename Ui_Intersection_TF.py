# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Intersection_TF\Intersection_TF.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(743, 719)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(743, 719))
        Form.setMaximumSize(QtCore.QSize(743, 719))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Intersection_TF\\tjad.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 210, 721, 311))
        self.groupBox.setObjectName("groupBox")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 321, 281))
        self.graphicsView.setObjectName("graphicsView")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(340, 20, 371, 151))
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(340, 190, 371, 111))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_load_data = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_load_data.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.pushButton_load_data.setObjectName("pushButton_load_data")
        self.pushButton_clear_data = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_clear_data.setGeometry(QtCore.QRect(260, 30, 75, 23))
        self.pushButton_clear_data.setObjectName("pushButton_clear_data")
        self.pushButton_save_data = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_save_data.setGeometry(QtCore.QRect(150, 30, 75, 23))
        self.pushButton_save_data.setObjectName("pushButton_save_data")
        self.pushButton_draw_p = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_draw_p.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButton_draw_p.setObjectName("pushButton_draw_p")
        self.pushButton_ouput_p = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_ouput_p.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.pushButton_ouput_p.setObjectName("pushButton_ouput_p")
        self.pushButton_zhanwei = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_zhanwei.setGeometry(QtCore.QRect(260, 70, 75, 23))
        self.pushButton_zhanwei.setObjectName("pushButton_zhanwei")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 721, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 321, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_8.setObjectName("label_8")
        self.radioButton_X = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_X.setGeometry(QtCore.QRect(90, 20, 61, 16))
        self.radioButton_X.setObjectName("radioButton_X")
        self.radioButton_T = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_T.setGeometry(QtCore.QRect(180, 20, 51, 16))
        self.radioButton_T.setObjectName("radioButton_T")
        self.radioButton_Others = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_Others.setGeometry(QtCore.QRect(250, 20, 51, 16))
        self.radioButton_Others.setObjectName("radioButton_Others")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 61, 24))
        self.label_9.setObjectName("label_9")
        self.textEdit_NBLK = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_NBLK.setGeometry(QtCore.QRect(80, 50, 71, 24))
        self.textEdit_NBLK.setObjectName("textEdit_NBLK")
        self.textEdit_DXLK = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_DXLK.setGeometry(QtCore.QRect(230, 50, 71, 24))
        self.textEdit_DXLK.setObjectName("textEdit_DXLK")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(160, 50, 61, 24))
        self.label_10.setObjectName("label_10")
        self.pushButton_Para_Reset = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_Para_Reset.setGeometry(QtCore.QRect(180, 130, 101, 22))
        self.pushButton_Para_Reset.setObjectName("pushButton_Para_Reset")
        self.textEdit_INAME_NB = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_INAME_NB.setGeometry(QtCore.QRect(80, 90, 71, 24))
        self.textEdit_INAME_NB.setObjectName("textEdit_INAME_NB")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 90, 71, 24))
        self.label_11.setObjectName("label_11")
        self.pushButton_clear_input = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_clear_input.setGeometry(QtCore.QRect(40, 130, 101, 22))
        self.pushButton_clear_input.setObjectName("pushButton_clear_input")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(160, 90, 71, 24))
        self.label_12.setObjectName("label_12")
        self.textEdit_INAME_DX = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_INAME_DX.setGeometry(QtCore.QRect(230, 90, 71, 24))
        self.textEdit_INAME_DX.setObjectName("textEdit_INAME_DX")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(340, 20, 371, 161))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 71, 20))
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.groupBox_4)
        self.frame.setGeometry(QtCore.QRect(260, 30, 41, 20))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_changeC1 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_changeC1.setGeometry(QtCore.QRect(310, 30, 51, 23))
        self.pushButton_changeC1.setObjectName("pushButton_changeC1")
        self.pushButton_changeC2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_changeC2.setGeometry(QtCore.QRect(130, 30, 51, 23))
        self.pushButton_changeC2.setObjectName("pushButton_changeC2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 71, 20))
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_2.setGeometry(QtCore.QRect(80, 30, 41, 20))
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_changeC4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_changeC4.setGeometry(QtCore.QRect(310, 60, 51, 23))
        self.pushButton_changeC4.setObjectName("pushButton_changeC4")
        self.pushButton_changeC3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_changeC3.setGeometry(QtCore.QRect(130, 60, 51, 23))
        self.pushButton_changeC3.setObjectName("pushButton_changeC3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 71, 20))
        self.label_4.setObjectName("label_4")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_3.setGeometry(QtCore.QRect(80, 60, 41, 20))
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(190, 60, 71, 20))
        self.label_5.setObjectName("label_5")
        self.frame_4 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_4.setGeometry(QtCore.QRect(260, 60, 41, 20))
        self.frame_4.setAutoFillBackground(True)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 54, 12))
        self.label_6.setObjectName("label_6")
        self.radioButton_aidaroe = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_aidaroe.setGeometry(QtCore.QRect(90, 100, 89, 16))
        self.radioButton_aidaroe.setObjectName("radioButton_aidaroe")
        self.radioButton_cad = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_cad.setGeometry(QtCore.QRect(180, 100, 89, 16))
        self.radioButton_cad.setObjectName("radioButton_cad")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 71, 22))
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox.setGeometry(QtCore.QRect(90, 130, 161, 22))
        self.spinBox.setMinimum(20)
        self.spinBox.setMaximum(200)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setObjectName("spinBox")
        self.pushButton_para_reset2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_para_reset2.setGeometry(QtCore.QRect(260, 130, 101, 22))
        self.pushButton_para_reset2.setObjectName("pushButton_para_reset2")
        self.radioButton_zdk = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_zdk.setGeometry(QtCore.QRect(270, 100, 89, 16))
        self.radioButton_zdk.setObjectName("radioButton_zdk")
        self.groupBox_6 = QtWidgets.QGroupBox(Form)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 530, 721, 181))
        self.groupBox_6.setObjectName("groupBox_6")
        self.textEdit_save_path = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit_save_path.setGeometry(QtCore.QRect(84, 30, 531, 25))
        self.textEdit_save_path.setObjectName("textEdit_save_path")
        self.pushButton_choose_path = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_choose_path.setGeometry(QtCore.QRect(630, 30, 75, 25))
        self.pushButton_choose_path.setObjectName("pushButton_choose_path")
        self.pushButton_load_datas = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_load_datas.setGeometry(QtCore.QRect(220, 70, 75, 23))
        self.pushButton_load_datas.setObjectName("pushButton_load_datas")
        self.pushButton_draw_ps = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_draw_ps.setGeometry(QtCore.QRect(314, 70, 81, 23))
        self.pushButton_draw_ps.setObjectName("pushButton_draw_ps")
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setGeometry(QtCore.QRect(20, 30, 54, 25))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar.setGeometry(QtCore.QRect(20, 110, 681, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_help = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_help.setGeometry(QtCore.QRect(420, 150, 75, 23))
        self.pushButton_help.setObjectName("pushButton_help")
        self.pushButton_close_form = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_close_form.setGeometry(QtCore.QRect(220, 150, 75, 23))
        self.pushButton_close_form.setObjectName("pushButton_close_form")
        self.pushButton_restart_form = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_restart_form.setGeometry(QtCore.QRect(320, 150, 75, 23))
        self.pushButton_restart_form.setObjectName("pushButton_restart_form")
        self.pushButton_open_folder = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_open_folder.setGeometry(QtCore.QRect(420, 70, 75, 23))
        self.pushButton_open_folder.setObjectName("pushButton_open_folder")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "交叉口流量流向图Demo(Designed by zoudaokou)"))
        self.groupBox.setTitle(_translate("Form", "交叉口流量流向图"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "南进口道"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "北进口道"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "东进口道"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "西进口道"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "左转（pcu/h)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "直行（pcu/h)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "右转（pcu/h)"))
        self.groupBox_5.setTitle(_translate("Form", "单个绘制"))
        self.pushButton_load_data.setText(_translate("Form", "导入数据"))
        self.pushButton_clear_data.setText(_translate("Form", "清空数据"))
        self.pushButton_save_data.setText(_translate("Form", "保存数据"))
        self.pushButton_draw_p.setText(_translate("Form", "绘制图形"))
        self.pushButton_ouput_p.setText(_translate("Form", "导出图形"))
        self.pushButton_zhanwei.setText(_translate("Form", "Fireworks"))
        self.groupBox_2.setTitle(_translate("Form", "参数设置"))
        self.groupBox_3.setTitle(_translate("Form", "交叉口参数"))
        self.label_8.setText(_translate("Form", "交叉口形式："))
        self.radioButton_X.setText(_translate("Form", "十字型"))
        self.radioButton_T.setText(_translate("Form", "T型"))
        self.radioButton_Others.setText(_translate("Form", "其他"))
        self.label_9.setText(_translate("Form", "南北路宽："))
        self.label_10.setText(_translate("Form", "东西路宽："))
        self.pushButton_Para_Reset.setText(_translate("Form", "恢复默认设置"))
        self.label_11.setText(_translate("Form", "南北向路名："))
        self.pushButton_clear_input.setText(_translate("Form", "清空输入"))
        self.label_12.setText(_translate("Form", "东西向路名："))
        self.groupBox_4.setTitle(_translate("Form", "图形参数"))
        self.label_2.setText(_translate("Form", "北进口颜色："))
        self.pushButton_changeC1.setText(_translate("Form", "更改"))
        self.pushButton_changeC2.setText(_translate("Form", "更改"))
        self.label_3.setText(_translate("Form", "南进口颜色："))
        self.pushButton_changeC4.setText(_translate("Form", "更改"))
        self.pushButton_changeC3.setText(_translate("Form", "更改"))
        self.label_4.setText(_translate("Form", "东进口颜色："))
        self.label_5.setText(_translate("Form", "西进口颜色："))
        self.label_6.setText(_translate("Form", "图形风格："))
        self.radioButton_aidaroe.setText(_translate("Form", "aidaroee"))
        self.radioButton_cad.setText(_translate("Form", "cadstyle"))
        self.label_7.setText(_translate("Form", "流量线宽比："))
        self.pushButton_para_reset2.setText(_translate("Form", "恢复默认设置"))
        self.radioButton_zdk.setText(_translate("Form", "JAstyle"))
        self.groupBox_6.setTitle(_translate("Form", "批量绘制"))
        self.pushButton_choose_path.setText(_translate("Form", "选择路径"))
        self.pushButton_load_datas.setText(_translate("Form", "打开数据集"))
        self.pushButton_draw_ps.setText(_translate("Form", "批量绘制图形"))
        self.label.setText(_translate("Form", "存储路径："))
        self.pushButton_help.setText(_translate("Form", "帮助"))
        self.pushButton_close_form.setText(_translate("Form", "关闭"))
        self.pushButton_restart_form.setText(_translate("Form", "重启"))
        self.pushButton_open_folder.setText(_translate("Form", "打开文件夹"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
