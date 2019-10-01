# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:09:38 2019

@author: swathi
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QPixmap,QImage,QPainter,QColor
from PyQt5.QtCore import QDir, Qt, QUrl,QThread,QRect,QPoint
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QTableWidget,QVBoxLayout,
    QTableWidgetItem, QLabel, QHBoxLayout,QGridLayout)
import cv2
from collections import deque 

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Video Streaming & Alerts'
        self.left = 0
        self.top = 0
        self.width = 1900 #640
        self.height = 1000 #480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
#        self.resize(1200, 800) #1800,1200 width & height  #this will resize the  whole GUI layout so better
#                                                                to keep it commented
        layout = QWidget(self)
        label = QLabel(self)
        label.setScaledContents(True)

        label_1 = QLabel(self)
        label_2 = QLabel(self)
        label_3 = QLabel(self)
        label_4 = QLabel(self)
        label_5 = QLabel(self)
        
#        pos = QPoint(50, 50)
#        painter = QPainter(self)
#        painter.drawText(pos, 'text here')
#        painter.setPen(QColor(255, 255, 255))
#        painter.show()
        
        
        stack = deque(["0","1","2","3","4"])
        stack.append("new")
        stack.popleft()
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        count = 0
        
#        cap = cv2.VideoCapture(0)
        cap = cv2.VideoCapture("videoplayback.mp4")
        while True:
            ret, frame = cap.read()
            cv2.putText(frame, "Swathi!", (10, 50), font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                             QtGui.QImage.Format_RGB888)
            convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
            pixmap = QPixmap(convertToQtFormat)
            resizeImage = pixmap.scaled(900, 900) #changing 640,480
            QApplication.processEvents()
            label.setPixmap(resizeImage)
            self.show()
            
#            font = cv2.FONT_HERSHEY_SIMPLEX
#            bottomLeftCornerOfText = (10,500)
#            fontScale              = 1
#            fontColor              = (255,255,255)
#            lineType               = 2
#            
#            cv2.putText(frame,'Hello World!',bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
#            cv2.putText(frame, "This one!", (50, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)


            if count %30 == 0:
                cv2.imwrite("vid%d.jpg" % count, frame)     # save frame as JPEG file      
                picname = "vid%d.jpg" % count
                stack.append(picname)
                stack.popleft()
                print('Read a new frame')
                print(stack)
                
                
            count += 1
            
            label_1.setGeometry(QtCore.QRect(1430, 0, 480, 200)) #Here x,y,width,height
            img1 = stack[0]
            img1_0 = QtGui.QPixmap(img1)
            print(img1)
            label_1.setPixmap(img1_0)
            label_1.setScaledContents(True)
            
            label_2.setGeometry(QtCore.QRect(1430, 205, 480, 200))
            img2 = stack[1]
            print("img22222222222")
            label_2.setPixmap(QtGui.QPixmap(img2))
            label_2.setScaledContents(True)
            
            label_3.setGeometry(QtCore.QRect(1430, 410, 480, 200))
            img3 = stack[2]
            label_3.setPixmap(QtGui.QPixmap(img3))
            label_3.setScaledContents(True)
            
            label_4.setGeometry(QtCore.QRect(1430, 615, 480, 200))
            img4 = stack[3]
            label_4.setPixmap(QtGui.QPixmap(img4))
            label_4.setScaledContents(True)

            label_5.setGeometry(QtCore.QRect(1430, 820, 480, 200))
            img5 = stack[4]
            label_5.setPixmap(QtGui.QPixmap(img5))
            label_5.setScaledContents(True)
            
            label.setGeometry(QtCore.QRect(0, 0, 1420, 1000))
            
        layout = QWidget()
        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())