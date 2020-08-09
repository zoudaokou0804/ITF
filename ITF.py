#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:ITF.py
@Time:2020/07/28 22:56:16
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:交叉口流量流向图自动化绘制
'''

import shutil
import time
import math
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from Ui_Intersection_TF import Ui_Form
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import webbrowser
import win32api
import platform

# 重写graphicsview双击事件
class gpv(QGraphicsView):
    def __init__(self,parent=None):
        super(gpv,self).__init__(parent)
        self.setGeometry(10, 230, 331, 281)
        self.bpg=r'交叉口流量流向示意图.png'
    def mouseDoubleClickEvent(self,e):
        userPlatform=platform.system()						# 获取操作系统
        if userPlatform == 'Darwin':								# Mac
            subprocess.call(['open', fileDir])
        elif userPlatform == 'Linux':								# Linux
            subprocess.call(['xdg-open', fileDir])
        else:																# Windows
            os.startfile(self.bpg)
class InnerHTML(QMainWindow):

    def __init__(self):
        super(InnerHTML, self).__init__()
        self.setWindowTitle('Welcome to TJAD-QL-4')
        self.setGeometry(400, 250, 1000, 500)

    def open(self):
        self.show()
        self.browser = QWebEngineView()
        self.browser.load(QUrl(QFileInfo(r"烟花特效\index .html").absoluteFilePath()))
        self.setCentralWidget(self.browser)


class ITF(QWidget, Ui_Form):
    def __init__(self):
        super(ITF, self).__init__()
        self.setupUi(self)
        self.datas_dict_list=[]
        # 交叉口默认参数设置
        self.radioButton_X.setChecked(True)
        self.textEdit_NBLK.setPlainText('30')
        self.textEdit_DXLK.setPlainText('30')
        self.textEdit_INAME_NB.setPlainText('南林路')
        self.textEdit_INAME_DX.setPlainText('G318')
        self.pushButton_clear_input.clicked.connect(self.clear_input)
        self.pushButton_Para_Reset.clicked.connect(self.reset_para1)
        # 绘制图形参数设置
        self.frame.setAutoFillBackground(True)
        self.frame.setPalette(QPalette(Qt.red))
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setPalette(QPalette(Qt.green))
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setPalette(QPalette(Qt.cyan))
        self.frame_4.setAutoFillBackground(True)
        self.frame_4.setPalette(QPalette(Qt.yellow))
        self.radioButton_aidaroe.setChecked(True)
        self.radioButton_zdk.clicked.connect(self.get_JA_process)
        self.spinBox.setRange(20, 100)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(100)
        self.pushButton_para_reset2.clicked.connect(self.reset_para2)
        self.pushButton_changeC1.clicked.connect(self.choose_c1)
        self.pushButton_changeC2.clicked.connect(self.choose_c2)
        self.pushButton_changeC3.clicked.connect(self.choose_c3)
        self.pushButton_changeC4.clicked.connect(self.choose_c4)
        # 设置默认示意图
        self.graphicsView=gpv(self)
        self.graphicsView.scene_img = QGraphicsScene()
        self.imgShow = QPixmap()
        self.imgShow.load(self.graphicsView.bpg)
        self.imgShowItem = QGraphicsPixmapItem()
        self.imgShowItem.setPixmap(QPixmap(self.imgShow))
        self.imgShowItem.setPixmap(
            QPixmap(self.imgShow).scaled(1700,  5500))  # 自己设定尺寸
        self.graphicsView.scene_img.addItem(self.imgShowItem)
        self.graphicsView.setScene(self.graphicsView.scene_img)
        self.graphicsView.fitInView(
            QGraphicsPixmapItem(QPixmap(self.imgShow)))  # 图像自适应大小
        # 设置表格格式及默认值
        # 第一行
        self.tableWidget.setShowGrid(True)
        newItem = QTableWidgetItem('789')
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置单元格居中
        self.tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('2011')
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置单元格居中
        self.tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('562')
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置单元格居中
        self.tableWidget.setItem(0, 2, newItem)
        # 第二行
        newItem = QTableWidgetItem('812')
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置单元格居中
        self.tableWidget.setItem(1, 0, newItem)
        newItem = QTableWidgetItem('2415')
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置单元格居中
        self.tableWidget.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('680')
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置单元格居中
        self.tableWidget.setItem(1, 2, newItem)
        # 第三行
        newItem = QTableWidgetItem('297')
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置单元格居中
        self.tableWidget.setItem(2, 0, newItem)
        newItem = QTableWidgetItem('350')
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置单元格居中
        self.tableWidget.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('787')
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置单元格居中
        self.tableWidget.setItem(2, 2, newItem)
        # 第四行
        newItem = QTableWidgetItem('770')
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置单元格居中
        self.tableWidget.setItem(3, 0, newItem)
        newItem = QTableWidgetItem('560')
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置单元格居中
        self.tableWidget.setItem(3, 1, newItem)
        newItem = QTableWidgetItem('280')
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置单元格居中
        self.tableWidget.setItem(3, 2, newItem)
        # 设置单个绘制区域按钮功能
        self.pushButton_load_data.clicked.connect(self.load_data)
        self.pushButton_save_data.clicked.connect(self.save_data)
        self.pushButton_clear_data.clicked.connect(self.clear_data)
        self.pushButton_ouput_p.clicked.connect(self.output_pic)
        self.pushButton_draw_p.clicked.connect(self.draw_p)
        # 批量绘图区域按钮
        self.textEdit_save_path.setPlainText(r'C:\ITF_DT')
        self.pushButton_choose_path.clicked.connect(self.choose_path)
        self.pushButton_open_folder.clicked.connect(self.open_folder)
        self.pushButton_load_datas.clicked.connect(self.load_datas)
        self.pushButton_draw_ps.clicked.connect(self.drawpics_batch)
        self.color_N=Qt.red
        self.color_S=Qt.green
        self.color_W=Qt.yellow
        self.color_E=Qt.cyan
        # 整个窗口操作之关闭窗口
        self.pushButton_close_form.clicked.connect(
            QCoreApplication.instance().quit)
       # 重新启动窗口
        self.pushButton_restart_form.clicked.connect(self.restart_form)
        # 打开帮助文档
        self.pushButton_help.clicked.connect(self.open_help_word)

        # self.graphicsView.mouseDoubleClickEvent(QMouseEvent)
    #     """
    #     设置控件透明度
    #     """
        self.path=os.path.abspath('.')
    #     op = QtWidgets.QGraphicsOpacityEffect()
    #     op.setOpacity(0)
    #     self.pushButton_tc.setGraphicsEffect(op)
    #     self.pushButton_tc.setAutoFillBackground(True)
    #     self.pushButton_tc.mouseDoubleClickEvent(self.show_son_window)
    # def show_son_window(self):
    #     QMessageBox.information(self,'消息','！', QMessageBox.Yes,QMessageBox.Yes)
        # self.graphicsView.mouseDoubleClickEvent(self.graphicsView,QMouseEvent)

    def get_JA_process(self): 
        QMessageBox.information(self,'消息','请先点击济安程序~“重置”~按钮！', QMessageBox.Yes,QMessageBox.Yes)
        # time.sleep(1)
        win32api.ShellExecute(0, 'open', '济安交叉口流量流向图.exe', '', '', 1)
    # 绘制单个交叉口流量流向图
    def draw_p(self):
        self.data={}
        data={}
        if self.radioButton_X.isChecked():
            data['TYPE']='1'
        elif self.radioButton_T.isChecked():
            data['TYPE']='2'
        else:
            data['TYPE']='3'
        data['SNRW']=self.textEdit_NBLK.toPlainText()
        data['EWRL']=self.textEdit_DXLK.toPlainText()
        data['SNRN']=self.textEdit_INAME_NB.toPlainText()
        data['EWRN']=self.textEdit_INAME_DX.toPlainText()
        data['S']=[self.tableWidget.item(0,0).text(),self.tableWidget.item(0,1).text(),self.tableWidget.item(0,2).text()]
        data['N']=[self.tableWidget.item(1,0).text(),self.tableWidget.item(1,1).text(),self.tableWidget.item(1,2).text()]
        data['E']=[self.tableWidget.item(2,0).text(),self.tableWidget.item(2,1).text(),self.tableWidget.item(2,2).text()]
        data['W']=[self.tableWidget.item(3,0).text(),self.tableWidget.item(3,1).text(),self.tableWidget.item(3,2).text()]
        # print(data) 
        self.data=data
        self.draw_p_p()
        self.graphicsView.bpg=self.path+'\\%s交叉口流量流向图.jpg'%(self.data['SNRN']+'&'+self.data['EWRN'])
        self.show_in_graphview(self.graphicsView.bpg)
    # 进口道路颜色设置
        
    def choose_c1(self):
        self.color_N = QColorDialog.getColor(Qt.blue)
        self.frame.setPalette(QPalette(self.color_N))
        # return color_N

    def choose_c2(self):
        self.color_S = QColorDialog.getColor(Qt.green)
        self.frame_2.setPalette(QPalette(self.color_S))
        # return color_S
    def choose_c4(self):
        self.color_W = QColorDialog.getColor(Qt.yellow)
        self.frame_4.setPalette(QPalette(self.color_W))
    def choose_c3(self):
        self.color_E = QColorDialog.getColor(Qt.cyan)
        self.frame_3.setPalette(QPalette(self.color_E))
        # return color_E
    # 将图像花在pixmap上，再保存为图片
    def draw_p_p(self):
        # 基准点坐标
        base_x,base_y=0,0
        # 将交通量转化为笔宽的除数
        ratio_div=self.spinBox.value()
        """
        以下为东西南北进口道
        """
        # 北进口道    
        NI_L_width=int(self.data['N'][0])/ratio_div
        NI_Z_width=int(self.data['N'][1])/ratio_div
        NI_R_width=int(self.data['N'][2])/ratio_div
        NI_total_width=NI_L_width+NI_Z_width+NI_R_width 
        NI_XZ,NI_YZ=base_x+375,base_y+275
        NPI_Z=QPoint(NI_XZ,NI_YZ)
        NI_XL,NI_YL=base_x+375+(NI_L_width+NI_Z_width)/2,base_y+275 
        NPI_L=QPoint(NI_XL,NI_YL)
        NI_XR,NI_YR=base_x+375-(NI_Z_width+NI_R_width)/2,base_y+275 
        NPI_R=QPoint(NI_XR,NI_YR)
        # 南进口道     
        SI_L_width=int(self.data['S'][0])/ratio_div
        SI_Z_width=int(self.data['S'][1])/ratio_div
        SI_R_width=int(self.data['S'][2])/ratio_div
        SI_total_width=SI_L_width+SI_Z_width+SI_R_width 
        SI_XZ,SI_YZ=base_x+525,base_y+725
        SPI_Z=QPoint(SI_XZ,SI_YZ)
        SI_XL,SI_YL=base_x+525-(SI_L_width+SI_Z_width)/2,base_y+725
        SPI_L=QPoint(SI_XL,SI_YL)
        SI_XR,SI_YR=base_x+525+(SI_Z_width+SI_R_width)/2,base_y+725
        SPI_R=QPoint(SI_XR,SI_YR)
        # 西进口道  
        WI_L_width=int(self.data['W'][0])/ratio_div
        WI_Z_width=int(self.data['W'][1])/ratio_div
        WI_R_width=int(self.data['W'][2])/ratio_div
        WI_total_width=WI_L_width+WI_Z_width+WI_R_width 
        WI_XZ,WI_YZ=base_x+225,base_y+575
        WPI_Z=QPoint(WI_XZ,WI_YZ)
        WI_XL,WI_YL=base_x+225,base_y+575-(WI_L_width+WI_Z_width)/2
        WPI_L=QPoint(WI_XL,WI_YL)
        WI_XR,WI_YR=base_x+225,base_y+575+(WI_Z_width+WI_R_width)/2    
        WPI_R=QPoint(WI_XR,WI_YR)
        # 东进口道
        EI_L_width=int(self.data['E'][0])/ratio_div
        EI_Z_width=int(self.data['E'][1])/ratio_div
        EI_R_width=int(self.data['E'][2])/ratio_div
        EI_total_width=EI_L_width+EI_Z_width+EI_R_width 
        EI_XZ,EI_YZ=base_x+675,base_y+425
        EPI_Z=QPoint(EI_XZ,EI_YZ)
        EI_XL,EI_YL=base_x+675,base_y+425+(EI_L_width+EI_Z_width)/2
        EPI_L=QPoint(EI_XL,EI_YL)
        EI_XR,EI_YR=base_x+675,base_y+425-(EI_Z_width+EI_R_width)/2
        EPI_R=QPoint(EI_XR,EI_YR)
        """
        以下为东西南北出口道
        """
        # 北出口道
        NO_L_width=WI_L_width # 等于西进口道左转
        NO_Z_width=SI_Z_width # 等于南进口道直行
        NO_R_width=EI_R_width #等于东进口道右转
        NO_total_width=NO_L_width+NO_Z_width+NO_R_width # 北出口道总线宽
        NO_XZ,NO_YZ=base_x+525,base_y+275
        NPO_Z=QPoint(NO_XZ,NO_YZ)
        NO_XL,NO_YL=base_x+525-(NO_L_width+NO_Z_width)/2,base_y+275
        NPO_L=QPoint(NO_XL,NO_YL)
        NO_XR,NO_YR=base_x+525+(NO_Z_width+NO_R_width)/2,base_y+275
        NPO_R=QPoint(NO_XR,NO_YR)
        
        # 南出口道
        SO_L_width=EI_L_width #等于东进口道左转
        SO_Z_width=NI_Z_width #等于北进口到直行
        SO_R_width=WI_R_width #等于西进口道右转
        SO_total_width=SO_L_width+SO_Z_width+SO_R_width # 南出口道总线宽
        SO_XZ,SO_YZ=base_x+375,base_y+725
        SPO_Z=QPoint(SO_XZ,SO_YZ)
        SO_XL,SO_YL=base_x+375+(NO_L_width+NO_Z_width)/2,base_y+725
        SPO_L=QPoint(SO_XL,SO_YL)
        SO_XR,SO_YR=base_x+375-(NO_Z_width+NO_R_width)/2,base_y+725
        SPO_R=QPoint(SO_XR,SO_YR)
        # 西出口道
        WO_L_width=SI_L_width #等于南进口道左转
        WO_Z_width=EI_Z_width # 等于东进口道直行
        WO_R_width=NI_R_width #等于北进口到右转
        WO_total_width=WO_L_width+WO_Z_width+WO_R_width # 西出口道总线宽
        WO_XZ,WO_YZ=base_x+225,base_y+425
        WPO_Z=QPoint(WO_XZ,WO_YZ)
        WO_XZ,WO_YZ=base_x+225,base_y+425+(WO_L_width+WO_Z_width)/2
        WPO_L=QPoint(WO_XZ,WO_YZ)
        WO_XZ,WO_YZ=base_x+225,base_y+425-(WO_Z_width+WO_R_width)/2
        WPO_R=QPoint(WO_XZ,WO_YZ)
         # 东出口道
        EO_L_width=NI_L_width #等于北进口到左转
        EO_Z_width=WI_Z_width #等于西进口道直行
        EO_R_width=SI_R_width #等于南进口道右转
        EO_total_width=EO_L_width+EO_Z_width+EO_R_width # 东出口道总线宽
        EO_XZ,EO_YZ=base_x+675,base_y+575
        EPO_Z=QPoint(EO_XZ,EO_YZ)
        EO_XL,EO_YL=base_x+675,base_y+575-(EO_L_width+EO_Z_width)/2
        EPO_L=QPoint(EO_XL,EO_YL)
        EO_XR,EO_YR=base_x+675,base_y+575+(EO_Z_width+EO_R_width)/2
        EPO_R=QPoint(EO_XR,EO_YR)
        
#################以下为具体的绘图操作#######################以下为具体的绘图操作############################## 以下为具体的绘图操作#################################################################################################################
        self.image = QPixmap(900, 1000)
        self.image.fill(Qt.white)# 填充透明色
        # self.setWindowTitle("简单的画板")
        painter = QPainter(self.image)   
        painter.setRenderHint(True)
        # 画直行车流
        # 北进口道直行
        if NI_Z_width>0:
            pen1 = QPen(self.color_N,NI_Z_width,Qt.SolidLine)
            painter.setPen(pen1)
            NS_Z=QLine(NPI_Z,SPO_Z) # 北向南直行直线
            painter.drawLine(NS_Z) # 抗锯齿，去除绘图锯齿
        # 北进口道右转
        if NI_R_width>0:
            pen1 = QPen(self.color_N,NI_R_width,Qt.SolidLine)
            painter.setPen(pen1)
            rect = QRect(NPI_R.x()-2*abs(NPI_R.x()-WPO_R.x()),NPI_R.y()-abs(NPI_R.y()-WPO_R.y()),2*abs(NPI_R.x()-WPO_R.x()),2*abs(NPI_R.y()-WPO_R.y()))
            painter.drawArc(rect,270*16, 90*16)
        # 北进口道左转
        if NI_L_width>0:
            pen1 = QPen(self.color_N,NI_L_width,Qt.SolidLine)
            painter.setPen(pen1)
            rect = QRect(NPI_L.x(),NPI_L.y()-abs(NPI_L.y()-EPO_L.y()),2*abs(NPI_L.x()-EPO_L.x()),2*abs(NPI_L.y()-EPO_L.y()))
            painter.drawArc(rect,180*16, 90*16)
        # # 画进口道尾部
        # pen1 = QPen(self.color_N,NI_Z_width,Qt.SolidLine)
        # painter.setPen(pen1)
        # NS_Z=QLine(QPoint(NPI_Z.x(),NPI_Z.y()),QPoint(NPI_Z.x(),NPI_Z.y()-100+NI_Z_width/2))
        # painter.drawLine(NS_Z)
        # pen1 = QPen(self.color_N,NI_R_width,Qt.SolidLine)
        # painter.setPen(pen1)
        # NW_R=QLine(QPoint(NPI_R.x(),NPI_R.y()),QPoint(NPI_R.x(),NPI_R.y()-100+NI_R_width/2))
        # painter.drawLine(NW_R)
        # pen1 = QPen(self.color_N,NI_L_width,Qt.SolidLine)
        # painter.setPen(pen1)
        # NE_L=QLine(QPoint(NPI_L.x(),NPI_L.y()),QPoint(NPI_L.x(),NPI_L.y()-100+NI_L_width/2))
        # painter.drawLine(NE_L)

        # # 画进口道尾部——————方法2
        if NI_total_width>0:
            pen1 = QPen(self.color_N,NI_total_width,Qt.SolidLine)
            painter.setPen(pen1)
            NPI1=QPoint((NPI_L.x()+NPI_R.x())/2,(NPI_L.y()+NPI_R.y())/2)
            NPI2=QPoint((NPI_L.x()+NPI_R.x())/2,(NPI_L.y()+NPI_R.y())/2-100)
            NI_L=QLine(NPI1,NPI2)
            painter.drawLine(NI_L)
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 南进口道直行
        if SI_Z_width>0:
            pen1 = QPen(self.color_S,SI_Z_width,Qt.SolidLine)
            painter.setPen(pen1)
            # painter.drawLine(SPI_Z,NPO_Z) # 第一种方法
            SN_Z=QLine(SPI_Z,NPO_Z)  # 南向北直行直线
            painter.drawLine(SN_Z)
        # 南进口道右转
        if SI_R_width>0:
            pen1 = QPen(self.color_S,SI_R_width,Qt.SolidLine)
            painter.setPen(pen1)
            rect = QRect(SPI_R.x(),SPI_R.y()-abs(SPI_R.y()-EPO_R.y()),2*abs(SPI_R.x()-EPO_R.x()),2*abs(SPI_R.y()-EPO_R.y()))
            painter.drawArc(rect,90*16, 90*16)
        # 南进口道左转
        if SI_L_width>0:
            pen1 = QPen(self.color_S,SI_L_width,Qt.SolidLine)
            painter.setPen(pen1)
            rect = QRect(SPI_L.x()-2*abs(SPI_L.x()-WPO_L.x()),SPI_L.y()-abs(SPI_L.y()-WPO_L.y()),2*abs(SPI_L.x()-WPO_L.x()),2*abs(SPI_L.y()-WPO_L.y()))
            painter.drawArc(rect,0, 90*16)

        # # 画进口道尾部
        # pen1 = QPen(self.color_S,SI_Z_width,Qt.SolidLine)
        # painter.setPen(pen1)
        # SN_Z=QLine(QPoint(SPI_Z.x(),SPI_Z.y()),QPoint(SPI_Z.x(),SPI_Z.y()+100-SI_Z_width/2))
        # painter.drawLine(SN_Z)
        # pen1 = QPen(self.color_S,SI_R_width,Qt.SolidLine)
        # painter.setPen(pen1)
        # SE_R=QLine(QPoint(SPI_R.x(),SPI_R.y()),QPoint(SPI_R.x(),SPI_R.y()+100-SI_R_width/2))
        # painter.drawLine(SE_R)
        # pen1 = QPen(self.color_S,SI_L_width,Qt.SolidLine)
        # painter.setPen(pen1)
        # SW_L=QLine(QPoint(SPI_L.x(),SPI_L.y()),QPoint(SPI_L.x(),SPI_L.y()+100-SI_L_width/2))
        # painter.drawLine(SW_L)
        # # 画进口道尾部——————方法2
        if SI_total_width>0:
            pen1 = QPen(self.color_S,SI_total_width,Qt.SolidLine)
            painter.setPen(pen1)
            SPI1=QPoint((SPI_L.x()+SPI_R.x())/2,(SPI_L.y()+SPI_R.y())/2)
            SPI2=QPoint((SPI_L.x()+SPI_R.x())/2,(SPI_L.y()+SPI_R.y())/2+100)
            SI_L=QLine(SPI1,SPI2)
            painter.drawLine(SI_L)

        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 西进口道直行
        if WI_Z_width>0:
            pen1 = QPen(self.color_W,WI_Z_width,Qt.SolidLine)
            painter.setPen(pen1)
            # painter.drawLine(WPI_Z,EPO_Z)
            WE_Z=QLine(WPI_Z,EPO_Z)  # 西向东直行直线
            painter.drawLine(WE_Z)
        # 西进口道右转
        if WI_R_width>0:
            pen1 = QPen(self.color_W,WI_R_width,Qt.SolidLine)
            painter.setPen(pen1)
            rect = QRect(WPI_R.x()-abs(WPI_R.x()-SPO_R.x()),WPI_R.y(),2*abs(WPI_R.x()-SPO_R.x()),2*abs(WPI_R.y()-SPO_R.y()))
            painter.drawArc(rect,0, 90*16)
        # 西进口道左转
        if WI_L_width>0:
            pen1 = QPen(self.color_W,WI_L_width,Qt.SolidLine)
            painter.setPen(pen1)
            rect = QRect(WPI_L.x()-abs(WPI_L.x()-NPO_L.x()),WPI_L.y()-2*abs(WPI_L.y()-NPO_L.y()),2*abs(WPI_L.x()-NPO_L.x()),2*abs(WPI_L.y()-NPO_L.y()))
            painter.drawArc(rect,270*16, 90*16)
        # 画进口道尾部
        # pen1 = QPen(self.color_W,WI_Z_width,Qt.SolidLine)
        # painter.setPen(pen1)
        # WE_Z=QLine(QPoint(WPI_Z.x(),WPI_Z.y()),QPoint(WPI_Z.x()-100+WI_Z_width/2,WPI_Z.y()))
        # painter.drawLine(WE_Z)
        # pen1 = QPen(self.color_W,WI_R_width,Qt.SolidLine)
        # painter.setPen(pen1)
        # WS_R=QLine(QPoint(WPI_R.x(),WPI_R.y()),QPoint(WPI_R.x()-100+WI_R_width/2,WPI_R.y()))
        # painter.drawLine(WS_R)
        # pen1 = QPen(self.color_W,WI_L_width,Qt.SolidLine)
        # painter.setPen(pen1)
        # WN_L=QLine(QPoint(WPI_L.x(),WPI_L.y()),QPoint(WPI_L.x()-100+WI_L_width/2,WPI_L.y()))
        # painter.drawLine(WN_L)
        # 画进口道尾部——————方法2
        if WI_total_width>0:
            pen1 = QPen(self.color_W,WI_total_width,Qt.SolidLine)
            painter.setPen(pen1)
            WPI1=QPoint((WPI_L.x()+WPI_R.x())/2,(WPI_L.y()+WPI_R.y())/2)
            WPI2=QPoint((WPI_L.x()+WPI_R.x())/2-100,(WPI_L.y()+WPI_R.y())/2)
            WI_L=QLine(WPI1,WPI2)
            painter.drawLine(WI_L)
        
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 东进口道直行
        if EI_Z_width>0:
            pen1 = QPen(self.color_E,EI_Z_width,Qt.SolidLine)
            painter.setPen(pen1)
            # painter.drawLine(EPI_Z,WPO_Z)
            EW_Z=QLine(EPI_Z,WPO_Z)  # 东向西直行直线
            painter.drawLine(EW_Z)
        # 东进口道右转
        if EI_R_width>0:
            pen1 = QPen(self.color_E,EI_R_width,Qt.SolidLine)
            painter.setPen(pen1)
            rect = QRect(EPI_R.x()-abs(EPI_R.x()-NPO_R.x()),EPI_R.y()-2*abs(EPI_R.y()-NPO_R.y()),2*abs(EPI_R.x()-NPO_R.x()),2*abs(EPI_R.y()-NPO_R.y()))
            painter.drawArc(rect,180*16, 90*16)
        # 东进口道左转
        if EI_L_width>0:
            pen1 = QPen(self.color_E,EI_L_width,Qt.SolidLine)
            painter.setPen(pen1)
            rect = QRect(EPI_L.x()-abs(EPI_L.x()-SPO_L.x()),EPI_L.y(),2*abs(EPI_L.x()-SPO_L.x()),2*abs(EPI_L.y()-SPO_L.y()))
            painter.drawArc(rect,90*16, 90*16)

        # # 画进口道尾部
        # pen1 = QPen(self.color_E,EI_Z_width,Qt.SolidLine)
        # painter.setPen(pen1)
        # EW_Z=QLine(QPoint(EPI_Z.x(),EPI_Z.y()),QPoint(EPI_Z.x()+100-EI_Z_width/2,EPI_Z.y()))
        # painter.drawLine(EW_Z)
        # pen1 = QPen(self.color_E,EI_R_width,Qt.SolidLine)
        # painter.setPen(pen1)
        # EN_R=QLine(QPoint(EPI_R.x(),EPI_R.y()),QPoint(EPI_R.x()+100-EI_R_width/2,EPI_R.y()))
        # painter.drawLine(EN_R)
        # pen1 = QPen(self.color_E,EI_L_width,Qt.SolidLine)
        # painter.setPen(pen1)
        # ES_L=QLine(QPoint(EPI_L.x(),EPI_L.y()),QPoint(EPI_L.x()+100-EI_L_width/2,EPI_L.y()))
        # painter.drawLine(ES_L)

        # # 画进口道尾部——————方法2
        if EI_total_width>0:
            pen1 = QPen(self.color_E,EI_total_width,Qt.SolidLine)
            painter.setPen(pen1)
            EPI1=QPoint((EPI_L.x()+EPI_R.x())/2,(EPI_L.y()+EPI_R.y())/2)
            EPI2=QPoint((EPI_L.x()+EPI_R.x())/2+100,(EPI_L.y()+EPI_R.y())/2)
            EI_L=QLine(EPI1,EPI2)
            painter.drawLine(EI_L)
        
####################################################################################################################################################################################################  
# 画四个出口道的
        # 北出口道
        # 画出口道尾部
        if NO_total_width>0:
            pen1 = QPen(self.color_N,NO_total_width,Qt.SolidLine)
            painter.setPen(pen1)
            NPO1=QPoint((NPO_L.x()+NPO_R.x())/2,(NPO_L.y()+NPO_R.y())/2)
            NPO2=QPoint((NPO_L.x()+NPO_R.x())/2,(NPO_L.y()+NPO_R.y())/2-60)
            NO_L=QLine(NPO1,NPO2)
            painter.drawLine(NO_L)
            # # 画出口道箭头
            N_arrowPoints=[QPoint(NPO1.x()-1.3*NO_total_width,NPO1.y()-60),QPoint(NPO1.x()+1.3*NO_total_width,NPO1.y()-60),QPoint(NPO1.x(),NPO1.y()-125)] # 出口道箭头的点集合
            pen1 = QPen(self.color_N,0,Qt.SolidLine)
            painter.setPen(pen1)
            brush = QBrush(self.color_N)
            painter.setBrush(brush)
            painter.drawPolygon(QPolygon(N_arrowPoints))
        
        # 南出口道
        # 画出口道尾部
        if SO_total_width>0:
            pen1 = QPen(self.color_S,SO_total_width,Qt.SolidLine)
            painter.setPen(pen1)
            SPO1=QPoint((SPO_L.x()+SPO_R.x())/2,(SPO_L.y()+SPO_R.y())/2)
            SPO2=QPoint((SPO_L.x()+SPO_R.x())/2,(SPO_L.y()+SPO_R.y())/2+60)
            SO_L=QLine(SPO1,SPO2)
            painter.drawLine(SO_L)

            # # 画箭头
            S_arrowPoints=[QPoint(SPO1.x()-1.3*SO_total_width,SPO1.y()+60),QPoint(SPO1.x()+1.3*SO_total_width,SPO1.y()+60),QPoint(SPO1.x(),SPO1.y()+125)] # 出口道箭头的点集合
            pen1 = QPen(self.color_S,0,Qt.SolidLine)
            painter.setPen(pen1)
            brush = QBrush(self.color_S)
            painter.setBrush(brush)
            painter.drawPolygon(QPolygon(S_arrowPoints))

        # 西出口道
        # 画出口道尾部
        if WO_total_width>0:
            pen1 = QPen(self.color_W,WO_total_width,Qt.SolidLine)
            painter.setPen(pen1)
            WPO1=QPoint((WPO_R.x()+WPI_R.x())/2,(WPO_L.y()+WPO_R.y())/2)
            WPO2=QPoint((WPO_R.x()+WPI_R.x())/2-60,(WPO_L.y()+WPO_R.y())/2)
            WO_L=QLine(WPO1,WPO2)
            painter.drawLine(WO_L)
            # # 画箭头
            W_arrowPoints=[QPoint(WPO1.x()-60,WPO1.y()-1.3*WO_total_width),QPoint(WPO1.x()-60,WPO1.y()+1.3*WO_total_width),QPoint(WPO1.x()-125,WPO1.y())] # 出口道箭头的点集合
            pen1 = QPen(self.color_W,0,Qt.SolidLine)
            painter.setPen(pen1)
            brush = QBrush(self.color_W)
            painter.setBrush(brush)
            painter.drawPolygon(QPolygon(W_arrowPoints))

        # 东出口道
        # 画出口道尾部
        if EO_total_width>0:
            pen1 = QPen(self.color_E,EO_total_width,Qt.SolidLine)
            painter.setPen(pen1)
            EPO1=QPoint((EPO_L.x()+EPO_R.x())/2,(EPO_L.y()+EPO_R.y())/2)
            EPO2=QPoint((EPO_L.x()+EPO_R.x())/2+60,(EPO_L.y()+EPO_R.y())/2)
            EO_L=QLine(EPO1,EPO2)
            painter.drawLine(EO_L)
            # # 画箭头
            E_arrowPoints=[QPoint(EPO1.x()+60,EPO1.y()-1.3*EO_total_width),QPoint(EPO1.x()+60,EPO1.y()+1.3*EO_total_width),QPoint(EPO1.x()+125,EPO1.y())] # 出口道箭头的点集合
            pen1 = QPen(self.color_E,0,Qt.SolidLine)
            painter.setPen(pen1)
            brush = QBrush(self.color_E)
            painter.setBrush(brush)
            painter.drawPolygon(QPolygon(E_arrowPoints))

        #################################以下为配文字##############################################
        # 设置字体和颜色
        font=QFont()
        font.setPointSize(20)
        font.setFamily("Microsoft YaHei")
        # font.setLetterSpacing(AbsoluteSpacing,0)
        pen1 = QPen(Qt.black,0,Qt.SolidLine)
        painter.setPen(pen1)
        painter.setFont(font)
        painter.drawText(QRect(250,20,400,40),Qt.AlignCenter,self.data['SNRN']+'&'+self.data['EWRN'])
        painter.drawText(QRect(250,70,400,40),Qt.AlignCenter,'交叉口流量流向图')
        
        pen1 = QPen(self.color_N,0,Qt.SolidLine)
        painter.setPen(pen1)
        painter.drawText(QRect(250,140,400,40),Qt.AlignCenter,'北')
        pen1 = QPen(self.color_S,0,Qt.SolidLine)
        painter.setPen(pen1)
        painter.drawText(QRect(250,820,400,40),Qt.AlignCenter,'南')
        pen1 = QPen(self.color_W,0,Qt.SolidLine)
        painter.setPen(pen1)
        painter.drawText(QRect(80,250,40,500),Qt.AlignCenter,'西')
        pen1 = QPen(self.color_E,0,Qt.SolidLine)
        painter.setPen(pen1)
        painter.drawText(QRect(770,250,40,500),Qt.AlignCenter,'东')

        # 设置字体和颜色
        font=QFont()
        font.setPointSize(15)
        font.setFamily("Microsoft YaHei")
        # font.setLetterSpacing(AbsoluteSpacing,0)
        pen1 = QPen(Qt.black,0,Qt.SolidLine)
        painter.setPen(pen1)
        painter.setFont(font)
        painter.drawText(QRect(250,900,400,40),Qt.AlignLeft,'注：')
        painter.drawText(QRect(270,930,400,40),Qt.AlignLeft,'1、交通量单位为pcu/h；')
        painter.drawText(QRect(270,960,400,40),Qt.AlignLeft,'2、南北向为%s，东西向为%s；'%(self.data['SNRN'],self.data['EWRN']))
        


        #################################以下为标注流量值##############################################
        # 设置字体和颜色
        font=QFont()
        font.setPointSize(15)
        font.setFamily("Microsoft YaHei")
        # font.setLetterSpacing(AbsoluteSpacing,0)
        pen1 = QPen(Qt.black,0,Qt.SolidLine)
        painter.setPen(pen1)
        painter.setFont(font)
        # 西出口道及进口道流量值标注
        if WO_total_width>0:
            painter.drawText(QRect(WPO_L.x()-60,WPO_L.y()+WO_L_width/2,100,100),Qt.AlignLeft,str(int(self.data['N'][2])+int(self.data['E'][1])+int(self.data['S'][0]))) #西出口
        if WI_total_width>0:
            painter.drawText(QRect(WPI_R.x()-60,WPI_R.y()+WI_R_width/2,100,100),Qt.AlignLeft,str(int(self.data['W'][0])+int(self.data['W'][1])+int(self.data['W'][2]))) #西进口
        if WI_L_width>0:
            painter.drawText(QRect(WPI_Z.x()+60,WPI_Z.y()-50,100,100),Qt.AlignLeft,self.data['W'][0]) #西进口左转
        if WI_Z_width>0:
            painter.drawText(QRect(WPI_Z.x()+60,WPI_Z.y()-10,100,100),Qt.AlignLeft,self.data['W'][1]) #西进口直行
        if WI_R_width>0:
            painter.drawText(QRect(WPI_Z.x()+60,WPI_Z.y()+45,100,100),Qt.AlignLeft,self.data['W'][2]) #西进口右转
        # 东出口道及进口道流量值标注
        if EO_total_width>0:
            painter.drawText(QRect(EPO_R.x(),EPO_R.y()+EO_R_width/2,100,100),Qt.AlignLeft,str(int(self.data['N'][0])+int(self.data['W'][1])+int(self.data['S'][2]))) #东出口
        if EI_total_width>0:
            painter.drawText(QRect(EPI_L.x(),EPI_L.y()+EI_L_width/2,100,100),Qt.AlignLeft,str(int(self.data['E'][0])+int(self.data['E'][1])+int(self.data['E'][2]))) #东进口
        if EI_R_width>0:
            painter.drawText(QRect(EPI_Z.x()-120,EPI_Z.y()-100,100,100),Qt.AlignLeft,str(int(self.data['E'][2]))) #东进口右转
        if EI_Z_width>0:
            painter.drawText(QRect(EPI_Z.x()-120,EPI_Z.y()-10,100,100),Qt.AlignLeft,str(int(self.data['E'][1]))) #东进口直行
        if EI_L_width>0:
            painter.drawText(QRect(EPI_Z.x()-120,EPI_Z.y()+25,100,100),Qt.AlignLeft,str(int(self.data['E'][0]))) #东进口左转
        # 北出口道及进口道流量值标注
        painter.rotate(90) # 旋转坐标系改变字体方向
        if NO_total_width>0:
            painter.drawText(QRect(NPO_L.y()+NO_L_width/2-60,-NPO_L.x(),100,100),Qt.AlignLeft,str(int(self.data['W'][0])+int(self.data['S'][1])+int(self.data['E'][2]))) #北出口
        if NI_total_width>0:
            painter.drawText(QRect(NPI_R.y()+NI_R_width/2-60,-NPI_R.x(),100,100),Qt.AlignLeft,str(int(self.data['N'][0])+int(self.data['N'][1])+int(self.data['N'][2]))) #北进口
        if NI_R_width>0:
            painter.drawText(QRect(NPI_Z.y()+60,-(NPI_Z.x()-50),100,100),Qt.AlignLeft,str(int(self.data['N'][2]))) #北进口右转
        if NI_Z_width>0:
            painter.drawText(QRect(NPI_Z.y()+60,-(NPI_Z.x()+10),100,100),Qt.AlignLeft,str(int(self.data['N'][1]))) #北进口直行
        if NI_L_width>0:
            painter.drawText(QRect(NPI_Z.y()+60,-(NPI_Z.x()+60),100,100),Qt.AlignLeft,str(int(self.data['N'][0]))) #北进口左转
        # 南出口道及进口道流量值标注
        if SO_total_width>0:
            painter.drawText(QRect(SPO_R.y()+SO_R_width/2,-SPO_R.x(),100,100),Qt.AlignLeft,str(int(self.data['E'][0])+int(self.data['N'][1])+int(self.data['W'][2]))) #南出口
        if SI_total_width>0:
            painter.drawText(QRect(SPI_L.y()+SI_L_width/2,-SPI_L.x(),100,100),Qt.AlignLeft,str(int(self.data['S'][0])+int(self.data['S'][1])+int(self.data['S'][2]))) #南进口
        if SI_R_width>0:
            painter.drawText(QRect(SPI_Z.y()-120,-(SPI_Z.x()+100),100,100),Qt.AlignLeft,str(int(self.data['S'][2]))) #南进口右转
        if SI_Z_width>0:
            painter.drawText(QRect(SPI_Z.y()-120,-(SPI_Z.x()+10),100,100),Qt.AlignLeft,str(int(self.data['S'][1]))) #南进口直行
        if SI_L_width>0:
            painter.drawText(QRect(SPI_Z.y()-120,-(SPI_Z.x()-40),100,100),Qt.AlignLeft,str(int(self.data['S'][0]))) #南进口左转
        # path=self.path
        # 保存为图片
        self.image.save(self.path+'\\%s交叉口流量流向图.jpg'%(self.data['SNRN']+'&'+self.data['EWRN']))
        # path=r'%s交叉口流量流向图.jpg'%(self.data['SNRN']+'&'+self.data['EWRN'])
        
#############################################################################################################################################################################################
    def show_in_graphview(self,fullpath):
        # 设置画板显示图片
        # self.graphicsView=gpv(self)
        self.graphicsView.scene_img = QGraphicsScene()
        self.imgShow = QPixmap()
        self.imgShow.load(fullpath)
        self.imgShowItem = QGraphicsPixmapItem()
        self.imgShowItem.setPixmap(QPixmap(self.imgShow))
        self.imgShowItem.setPixmap(
            QPixmap(self.imgShow).scaled(900,  1000))  # 自己设定尺寸
        self.graphicsView.scene_img.addItem(self.imgShowItem)
        self.graphicsView.setScene(self.graphicsView.scene_img)
        self.graphicsView.fitInView(
            QGraphicsPixmapItem(QPixmap(self.imgShow)))  # 图像自适应大小
    # 打开帮助文档
    def open_help_word(self):
        webbrowser.open(r'帮助文档.docx')
    # 重新启动程序

    def restart_form(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)
    # 导出单个交叉口流量流向图

    def output_pic(self):
        try:
            filename='%s交叉口流量流向图.jpg'%(self.data['SNRN']+'&'+self.data['EWRN'])
            dialog = QFileDialog.getSaveFileName(
                self, '保存数据文件', filename, '图像文件(*.jpg)')
            shutil.copy(filename,dialog[0] )
            reply = QMessageBox.information(self,'消息','文件保存成功', QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        except:
            QMessageBox.warning(self,'警告','请先绘制图像',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
    # 打开文件夹

    def open_folder(self):
        os.startfile(self.textEdit_save_path.toPlainText())
    # 选择批量绘图图形的保存路径

    def choose_path(self):
        dir = QFileDialog.getExistingDirectory(
            self, '请选择文件夹', r'C:\Users\user\Desktop')
        self.textEdit_save_path.setPlainText(dir)
    # 读取批量交叉口流量流向数据，以excel文件形式
    def load_datas(self):
        dialog = QFileDialog.getOpenFileName(self, '打开数据文件', '.', '*.dats')
        # print(dialog)
        if dialog[0]=='':
            reply=QMessageBox.warning(self,'警告','请选择数据集',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            
        # else:
        #     try:
        #         win32api.ShellExecute(0, 'open', 'notepad++.exe', dialog[0], '', 1)
        #     except expression as identifier:
        #         win32api.ShellExecute(0, 'open', 'notepad.exe', dialog[0], '', 1)
        with open(dialog[0], 'r', encoding='utf-8') as f:
            datas = f.read().split('--------------------\n')
            # print(datas)
        datas_dict_list=[]
        for i in range(0,len(datas)):
            data=datas[i].splitlines()
            # print(data)
            data_dict={}
            for j in range(0,len(data)):
                data_dict[data[j].split(':')[0]]=data[j].split(':')[1]
            data_dict['S']=data_dict['S'].split(' ')
            data_dict['N']=data_dict['N'].split(' ')
            data_dict['E']=data_dict['E'].split(' ')
            data_dict['W']=data_dict['W'].split(' ')
            datas_dict_list.append(data_dict)   
        self.datas_dict_list=datas_dict_list
        # print(self.datas_dict_list)
    # 定义批量绘图方法，类似单个绘图
    def drawpics_batch(self):
        dts=self.datas_dict_list
        if len(dts)>0:
            self.path=self.textEdit_save_path.toPlainText()
            if not os.path.exists(self.path):
                os.mkdir(self.path)
            self.progressBar.setMaximum(len(dts))
            self.progressBar.reset()
            for i in range(0,len(dts)):
                self.data=dts[i]
                self.progressBar.setValue((i+1)/len(dts)*100)
                self.draw_p_p()
            QMessageBox.information(self,'消息','文件保存成功', QMessageBox.Yes,QMessageBox.Yes)
        else:
            QMessageBox.critical(self,'错误','请先选择数据集',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
    # 清空tablewiget中所有的数据
    def clear_data(self):
        self.tableWidget.clearContents()

    # 保存单个交叉口流量流向数据文件
    def save_data(self):
        dialog = QFileDialog.getSaveFileName(self, '保存数据文件', '.', '*.dat')
        # 写入文件
        with open(dialog[0], 'w', encoding='utf-8') as f:
            if self.radioButton_X.isChecked():
                tp = '1'
                f.write('TYPE:'+tp+'\n')
            if self.radioButton_T.isChecked():
                tp = '2'
                f.write('TYPE:'+tp+'\n')
            if self.radioButton_Others.isChecked():
                tp = '3'
                f.write('TYPE:'+tp+'\n')
            # 写入南北路宽
            SNRW = self.textEdit_NBLK.toPlainText()
            f.write('SNRW:'+SNRW+'\n')
            # 写入东西路宽
            ESRW = self.textEdit_DXLK.toPlainText()
            f.write('EWRW:'+ESRW+'\n')
            # 写入南北路名
            INAME_NB = self.textEdit_INAME_NB.toPlainText()
            f.write('SNRN:'+INAME_NB+'\n')
            # 写入东西路名
            INAME_DX = self.textEdit_INAME_DX.toPlainText()
            f.write('EWRN:'+INAME_DX+'\n')
            # 南进口道流量
            S_tf = f.write('S:'+self.tableWidget.item(0, 0).text()+' '+self.tableWidget.item(
                0, 1).text()+' '+self.tableWidget.item(0, 2).text()+'\n')
            N_tf = f.write('N:'+self.tableWidget.item(1, 0).text()+' '+self.tableWidget.item(
                1, 1).text()+' '+self.tableWidget.item(1, 2).text()+'\n')
            E_tf = f.write('E:'+self.tableWidget.item(2, 0).text()+' '+self.tableWidget.item(
                2, 1).text()+' '+self.tableWidget.item(2, 2).text()+'\n')
            W_tf = f.write('W:'+self.tableWidget.item(3, 0).text()+' ' +
                           self.tableWidget.item(3, 1).text()+' '+self.tableWidget.item(3, 2).text())

    # 读取单个交叉口流量流向文件，以自定义的.dat文件格式
    def load_data(self):
        dialog = QFileDialog.getOpenFileName(self, '打开数据文件', '.', '*.dat')
        # 读取数据文件，存入到一个dataframe中
        with open(dialog[0], 'r', encoding='utf-8') as f:
            datas = f.read().splitlines()
            
            print(datas)
        if datas[0].split(':')[1] == '1':
            self.radioButton_X.setChecked(True)
        if datas[0].split(':')[1] == '2':
            self.radioButton_T.setChecked(True)
        if datas[0].split(':')[1] == '3':
            self.radioButton_Others.setChecked(True)
        self.textEdit_NBLK.setPlainText(datas[1].split(':')[1])
        self.textEdit_DXLK.setPlainText(datas[2].split(':')[1])
        self.textEdit_INAME_NB.setPlainText(datas[3].split(':')[1])
        self.textEdit_INAME_DX.setPlainText(datas[4].split(':')[1])
        self.tableWidget.setItem(0, 0, QTableWidgetItem(
            datas[5].split(':')[1].split(' ')[0]))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(
            datas[5].split(':')[1].split(' ')[1]))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(
            datas[5].split(':')[1].split(' ')[2]))
        self.tableWidget.setItem(1, 0, QTableWidgetItem(
            datas[6].split(':')[1].split(' ')[0]))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(
            datas[6].split(':')[1].split(' ')[1]))
        self.tableWidget.setItem(1, 2, QTableWidgetItem(
            datas[6].split(':')[1].split(' ')[2]))
        self.tableWidget.setItem(2, 0, QTableWidgetItem(
            datas[7].split(':')[1].split(' ')[0]))
        self.tableWidget.setItem(2, 1, QTableWidgetItem(
            datas[7].split(':')[1].split(' ')[1]))
        self.tableWidget.setItem(2, 2, QTableWidgetItem(
            datas[7].split(':')[1].split(' ')[2]))
        self.tableWidget.setItem(3, 0, QTableWidgetItem(
            datas[8].split(':')[1].split(' ')[0]))
        self.tableWidget.setItem(3, 1, QTableWidgetItem(
            datas[8].split(':')[1].split(' ')[1]))
        self.tableWidget.setItem(3, 2, QTableWidgetItem(
            datas[8].split(':')[1].split(' ')[2]))
        # 设置表格单元格居中显示
        for i in range(4):
            for j in range(3):
                self.tableWidget.item(i, j).setTextAlignment(
                    (Qt.AlignHCenter | Qt.AlignVCenter))

    def clear_input(self):
        self.textEdit_NBLK.setPlainText('')
        self.textEdit_DXLK.setPlainText('')
        self.textEdit_INAME_NB.setPlainText('')
        self.textEdit_INAME_DX.setPlainText('')
    # 交叉口恢复默认参数按钮

    def reset_para1(self):
        self.radioButton_X.setChecked(True)
        self.textEdit_NBLK.setPlainText('30')
        self.textEdit_DXLK.setPlainText('30')
        self.textEdit_INAME_NB.setPlainText('南林路')
        self.textEdit_INAME_DX.setPlainText('G318')
    # 图形参数恢复默认参数按钮

    def reset_para2(self):
        self.frame.setPalette(QPalette(self.color_N))
        self.frame_2.setPalette(QPalette(self.color_S))
        self.frame_3.setPalette(QPalette(self.color_E))
        self.frame_4.setPalette(QPalette(self.color_E))
        self.radioButton_aidaroe.setChecked(True)
        self.spinBox.setValue(5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    itf = ITF()
    inner_form = InnerHTML()
    itf.show()
    itf.pushButton_zhanwei.clicked.connect(inner_form.open)
    sys.exit(app.exec_())
