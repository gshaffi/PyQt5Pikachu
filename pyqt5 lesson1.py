import sys, os, time, uuid, hashlib, re
from PyQt5 import QtCore, QtGui, uic  
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QComboBox, QTextEdit 

winMain = uic.loadUiType("homeScreen.ui") [0]
win2 = uic.loadUiType("InfoOutput.ui") [0]

print("Testing GIT changes")
class HomeScreen(QtWidgets.QMainWindow, winMain): #imports the PyQT 'main window' functionality, winMain links to UI screens above

	def __init__(self, parent = None):
		QtWidgets.QMainWindow.__init__(self,parent) ##setting the screen up, defining where the buttons are linking to, and where text box information is being stored 
		self.setupUi(self)
		self.submitBtn.clicked.connect(self.submitInput)
		self.clearBtn.clicked.connect(self.clearForm)
		nameTxt = self.nameTxt.text()
		ageTxt = self.ageTxt.text()

	def submitInput(self):
		user1.name = self.nameTxt.text()
		user1.age = self.ageTxt.text()
		user1.getDetails()
		QtWidgets.QMessageBox.information(self,"Success", "Name and age recorded", QMessageBox.Yes)
		self.nameTxt.clear()
		self.ageTxt.clear()

		self.hide()
		self.newWindow = InfoOut()
		self.newWindow.show()

		return user1.name, user1.age

	def clearForm(self):
		user1.name = " "
		user1.age = " "
		self.nameTxt.clear()
		self.ageTxt.clear()

class InfoOut(QtWidgets.QMainWindow, win2): #imports the PyQT 'main window' functionality, winMain links to UI screens above

	def __init__(self, parent = None):
		QtWidgets.QMainWindow.__init__(self,parent) ##setting the screen up, defining where the buttons are linking to, and where text box information is being stored 
		self.setupUi(self)
		name = "Your name is: " + user1.name
		age = "Your age is: " + user1.age
		namelabel = self.nameLbl.setText(name)
		agelabel = self.ageLbl.setText(age)
		pikaLabel = self.PikaLbl.text()


class User():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getDetails(self):
		pass
		#print (self.name, self.age)


user1 = User(" ", " ") #creates a customer object with no name or age 

app = QtWidgets.QApplication(sys.argv) #think of this as the 'main ()' section in procedural programming. Allows you to call the program into action 
winMain = HomeScreen()

winMain.show()
app.exec_()
