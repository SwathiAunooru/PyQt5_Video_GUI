# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:10:23 2019

@author: swathi
"""
from win32api import GetSystemMetrics
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QPixmap,QImage
from PyQt5.QtCore import QDir, Qt, QUrl,QThread,QRect,QSize
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QTableWidget,QVBoxLayout,
    QTableWidgetItem, QLabel, QHBoxLayout,QGridLayout)
import cv2
from collections import deque 
from PyQt5.QtCore import pyqtSlot

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Video Streaming & Alerts'
        self.left = 0
        self.top = 0
        self.width = GetSystemMetrics(0) #640
        self.height = GetSystemMetrics(1) #480
        self.initUI()        

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) 
#        self.resize(1200, 650) #1800,1200 width & height
        
        w = self.width
        print(w)
        w_frame = (w/100)*80
        h = self.height
        print(h)
        h_frame = (h/100)*90
        
        w_sub_frame = (w/100)*20
        h_sub_frame = (h/100)*25
        
        w_button = (h/100)*91
           
            
        layout = QWidget(self)
#        layout.setBackgroundRole()
        label = QLabel(self)
        label.setScaledContents(True)
        label_1 = QLabel(self)
        label_2 = QLabel(self)
        label_3 = QLabel(self)
        label_4 = QLabel(self)
#        button = QLabel(self)
        
        stack = deque(["0","1","2","3","4"])
        stack.append("new")
        stack.popleft()
        
        count = 0
        self.helmet = "helmet.png"
        self.handglove = "handglove.png"
        self.vest = "vest.png"
        self.shoe = "shoe.png"
        self.spill = "spill.png"
        
        label_img = QLabel(self)
        label_img1 = QLabel(self)
        label_img2 = QLabel(self)
        label_img3 = QLabel(self)
        label_img4 = QLabel(self)
        
        self.gif = QLabel(self)
        movie = QtGui.QMovie("gify_kid.gif")
        self.gif.setMovie(movie)
        self.gif.setGeometry(w_frame-150,w_button-100,100,100)
        movie.setScaledSize(QSize(100,100))  #Width , height
        movie.start()
        
        
        self.cb = QCheckBox('HELMET', self)
        self.cb.setChecked(True)
        
        self.cb.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: green;")
        self.cb.move(0,w_button)
        self.cb.stateChanged.connect(self.changeTitle)
        self.show
        
        self.cb1 = QCheckBox('HANDGLOVE', self)
        self.cb1.setChecked(True)
        self.cb1.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 100px;" "height: 30px;" "background-color: green;")
        self.cb1.move(100, w_button)
        self.cb1.stateChanged.connect(self.changeTitle1)
        self.show

        self.cb2 = QCheckBox('VEST', self)
        self.cb2.setChecked(True)
        self.cb2.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: green;")
        self.cb2.move(230, w_button)
        self.cb2.stateChanged.connect(self.changeTitle2)
        self.show
        
        self.cb3 = QCheckBox('SHOE', self)
        self.cb3.setChecked(True)
        self.cb3.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: green;")
        self.cb3.move(330, w_button)
        self.cb3.stateChanged.connect(self.changeTitle3)
        self.show
        
        self.cb4 = QCheckBox('SPILL', self)
        self.cb4.setChecked(True)
        self.cb4.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: green;")
        self.cb4.move(430, w_button)
        self.cb4.stateChanged.connect(self.changeTitle4)
        self.show
        
        font = cv2.FONT_HERSHEY_PLAIN
        cap = cv2.VideoCapture(0)
#        cap = cv2.VideoCapture("http://10.13.7.46:4747/video")
        self.color = cv2.COLOR_BGR2RGB
        while True:
            ret, frame = cap.read()
            cv2.putText(frame, "mobile alert", (10, 50), font, 1, (0, 255, 255
                        ), 2, cv2.LINE_AA)
            rgbImage = cv2.cvtColor(frame, self.color)
            convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                             QtGui.QImage.Format_RGB888)
            convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
            pixmap = QPixmap(convertToQtFormat)
            resizeImage = pixmap.scaled(w_frame, h_frame) #changing 640,480
            QApplication.processEvents()
            label.setPixmap(resizeImage)

            self.show()
            
            if count %30 == 0:
                cv2.imwrite("vid%d.jpg" % count, frame)     # save frame as JPEG file      
                picname = "vid%d.jpg" % count
#                ll.append(picname) 
                stack.append(picname)
                stack.popleft()
                print('Read a new frame')            
                
            count += 1
            
            label_1.setGeometry(QtCore.QRect(5+w_frame, 0, w_sub_frame, h_sub_frame)) #Here x,y,width,height
            img1 = stack[0]
            img1_0 = QtGui.QPixmap(img1)
#            print(img1)
            label_1.setPixmap(img1_0)
            label_1.setScaledContents(True)
            

            label_2.setGeometry(QtCore.QRect(5+w_frame, 1*h_sub_frame, w_sub_frame, h_sub_frame))
            img2 = stack[1]
            label_2.setPixmap(QtGui.QPixmap(img2))
            label_2.setScaledContents(True)
            
            label_3.setGeometry(QtCore.QRect(5+w_frame, 2*h_sub_frame, w_sub_frame, h_sub_frame))
            img3 = stack[2]
            label_3.setPixmap(QtGui.QPixmap(img3))
            label_3.setScaledContents(True)
            
            label_4.setGeometry(QtCore.QRect(5+w_frame, 3*h_sub_frame, w_sub_frame, h_sub_frame))
            img4 = stack[3]
            label_4.setPixmap(QtGui.QPixmap(img4))
            label_4.setScaledContents(True)
            
            pixmap0 = QPixmap(self.helmet)
            label_img.setPixmap(pixmap0)
            label_img.setScaledContents(True)
            label_img.setGeometry(QtCore.QRect(0, 0, 40, 40))   #Here x,y,width,height
            
            pixmap1 = QPixmap(self.handglove)
            label_img1.setPixmap(pixmap1)
            label_img1.setScaledContents(True)
            label_img1.setGeometry(QtCore.QRect(50, 0, 40, 40))
            
            pixmap2 = QPixmap(self.vest)
            label_img2.setPixmap(pixmap2)
            label_img2.setScaledContents(True)
            label_img2.setGeometry(QtCore.QRect(100,0, 40, 40))
            
            pixmap3 = QPixmap(self.shoe)
            label_img3.setPixmap(pixmap3)
            label_img3.setScaledContents(True)
            label_img3.setGeometry(QtCore.QRect(150,0, 40, 40))
            
            pixmap4 = QPixmap(self.spill)
            label_img4.setPixmap(pixmap4)
            label_img4.setScaledContents(True)
            label_img4.setGeometry(QtCore.QRect(200,0, 40, 40))


            
        
        layout = QWidget()
        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        
        layout.addWidget(self.gif)
        
        layout.addWidget(cb)
        layout.addWidget(cb1)
        layout.addWidget(cb2)
        layout.addWidget(cb3)
        layout.addWidget(cb4)
        
        layout.addWidget(label_img)
        layout.addWidget(label_img1)
        layout.addWidget(label_img2)
        layout.addWidget(label_img3)
        layout.addWidget(label_img4)
        
        
    def changeTitle(self, state):
        if state == Qt.Checked:
#            self.color = cv2.COLOR_BGR2HSV
            self.helmet = "helmet.png"
            self.cb.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: green;")
        else:
#            self.color = cv2.COLOR_BGR2RGB
            self.helmet = " "
            self.cb.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: blue;")
        
    def changeTitle1(self, state):
        if state == Qt.Checked:
#            self.color = cv2.COLOR_BGR2XYZ
            self.handglove = "handglove.png"
            self.cb1.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: green;")

        else:
            self.color = cv2.COLOR_BGR2RGB
            self.handglove = " "
            self.cb1.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: blue;")


    def changeTitle2(self, state):
        if state == Qt.Checked:
#            self.color = cv2.COLOR_BGR2HLS
            self.vest = "vest.png"
            self.cb2.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: green;")
        
        else:
            self.color = cv2.COLOR_BGR2RGB
            self.vest = " "
            self.cb2.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: blue;")
            
            
    def changeTitle3(self, state):
        if state == Qt.Checked:
#            self.color = cv2.COLOR_BGR2HSV
            self.shoe = "shoe.png"
            self.cb3.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: green;")

        else:
            self.color = cv2.COLOR_BGR2RGB
            self.shoe = " "
            self.cb3.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
                "width: 70px;" "height: 30px;" "background-color: blue;")
            
            
    def changeTitle4(self, state):
        if state == Qt.Checked:
#            self.color = cv2.COLOR_BGR2HSV
            self.spill = "spill.png"
            self.cb4.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: green;")
        else:
            self.color = cv2.COLOR_BGR2RGB
            self.spill = " "
            self.cb4.setStyleSheet("color: white;"" font: bold 14px;" "border-radius: 10px;"
            "width: 70px;" "height: 30px;" "background-color: blue;")
       
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
