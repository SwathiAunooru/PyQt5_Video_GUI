# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:23:01 2019

@author: swathi
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QPixmap,QImage
from PyQt5.QtCore import QDir, Qt, QUrl,QThread,QRect
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QTableWidget,QVBoxLayout,
    QTableWidgetItem, QLabel, QHBoxLayout,QGridLayout)
import cv2
from collections import deque 

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Video Streaming & Alerts'
        self.left = 100
        self.top = 100
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
        
        stack = deque(["0","1","2","3","4"])
        stack.append("new")
        stack.popleft()
        
        count = 0
        
#        cap = cv2.VideoCapture(0)
        cap = cv2.VideoCapture("videoplayback2.mov")
        while True:
            ret, frame = cap.read()
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                             QtGui.QImage.Format_RGB888)
            convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
            pixmap = QPixmap(convertToQtFormat)
            resizeImage = pixmap.scaled(900, 900) #changing 640,480
            QApplication.processEvents()
            label.setPixmap(resizeImage)
            self.show()

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