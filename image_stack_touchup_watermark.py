# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:20:43 2019

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
        self.left = 10
        self.top = 10
        self.width = 1930 #640
        self.height = 1000 #480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        layout = QWidget(self)
        label = QLabel(self)
        label.setScaledContents(True)
        label1 = QLabel(self)
        label1.setScaledContents(True)
        label2 = QLabel(self)
        label2.setScaledContents(True)
        label_1 = QLabel(self)
        label_2 = QLabel(self)
        label_3 = QLabel(self)
        label_4 = QLabel(self)
        label_5 = QLabel(self)
        stack = deque(["0","1","2","3","4"])
        stack.append("new")
        stack.popleft()
        
        label_img = QLabel(self)
        pixmap = QPixmap('logo_nobackground.jpeg')
        label_img.setPixmap(pixmap)
        label_img.setScaledContents(True)
        label_img.setGeometry(QtCore.QRect(0, 0, 140, 50))
        
        label_img1 = QLabel(self)
        pixmap1 = QPixmap('logo_nobackground.jpeg')
        label_img1.setPixmap(pixmap1)
        label_img1.setScaledContents(True)
        label_img1.setGeometry(QtCore.QRect(0, 610, 140, 50))
        
        label_img2 = QLabel(self)
        pixmap2 = QPixmap('logo_nobackground.jpeg')
#        pixmap2.setOpacity(0.5)
        label_img2.setPixmap(pixmap2)
        label_img2.setScaledContents(True)
        label_img2.setGeometry(QtCore.QRect(715, 610, 140, 50))#Here x,y,width,height
        
        label_img3 = QLabel(self)
        pixmap3 = QPixmap('logo_nobackground.jpeg')
#        pixmap2.setOpacity(0.5)
        label_img3.setPixmap(pixmap3)
        label_img3.setScaledContents(True)
        label_img3.setGeometry(QtCore.QRect(715,0, 140, 50))
        
        count = 0
        
        
        cap = cv2.VideoCapture("videoplayback.mp4")
        cap1 = cv2.VideoCapture("videoplayback2.mov")
        cap2 = cv2.VideoCapture("videoplayback2.mov")

        while True:
            ret, frame = cap.read()
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                             QtGui.QImage.Format_RGB888)
            convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
            pixmap = QPixmap(convertToQtFormat)
            resizeImage = pixmap.scaled(900, 500) #changing 640,480
            QApplication.processEvents()
            label.setPixmap(resizeImage)
            self.show()
            
            if count %30 == 0:
                cv2.imwrite("vid%d.jpg" % count, frame)     # save frame as JPEG file      
                picname = "vid%d.jpg" % count
                stack.append(picname)
                stack.popleft()
                print('Read a new frame')
#                print(ll)
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
            
            label.setGeometry(QtCore.QRect(0, 0, 1420, 600))
            label1.setGeometry(QtCore.QRect(0, 610, 705, 500))
            label2.setGeometry(QtCore.QRect(715, 610, 705, 500))
            
      
            ret, frame1 = cap1.read()
            rgbImage1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
            convertToQtFormat1 = QtGui.QImage(rgbImage1.data, rgbImage1.shape[1], rgbImage1.shape[0],
                                             QtGui.QImage.Format_RGB888)
            convertToQtFormat1 = QtGui.QPixmap.fromImage(convertToQtFormat1)
            pixmap1 = QPixmap(convertToQtFormat1)
            resizeImage1 = pixmap1.scaled(1800, 500) #changing 640,480 width & height
            QApplication.processEvents()
            label1.setPixmap(resizeImage1)
            self.show()
            
            ret, frame2 = cap2.read()
            rgbImage2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
            convertToQtFormat2 = QtGui.QImage(rgbImage2.data, rgbImage2.shape[1], rgbImage2.shape[0],
                                             QtGui.QImage.Format_RGB888)
            convertToQtFormat2 = QtGui.QPixmap.fromImage(convertToQtFormat2)
            pixmap2 = QPixmap(convertToQtFormat2)
            resizeImage2 = pixmap2.scaled(1800, 500) #changing 640,480 width & height
            QApplication.processEvents()
            label2.setPixmap(resizeImage2)
            self.show()
            
            
         
                    
        layout = QWidget()
        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label_img)
        layout.addWidget(label_img1)
        layout.addWidget(label_img1)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
#    ex1 = App1()
    ex = App()
    sys.exit(app.exec_())


  

