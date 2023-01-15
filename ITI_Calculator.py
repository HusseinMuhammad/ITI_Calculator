import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit
a=QApplication(sys.argv)#connection between qt and python(library sys) to create application

t=QWidget()# make screen
t.setWindowTitle("ITI calculator")#make tittle
t.setGeometry(50,100,700,400)#geometry take 4 parameter ( x co-ordinate, y co-ordinate,Width  ,Height ) in  the screen
n1=QLabel("first num",t)#first num
n1.move(30,30)
t1=QLineEdit(t)
t1.move(90,30)
n2=QLabel("second num",t)#second num
n2.move(250,30)
t2=QLineEdit(t)
t2.move(350,30)
b1=QPushButton("+",t)
b1.move(80,80)
b2=QPushButton("-",t)
b2.move(180,80)
b3=QPushButton("*",t)
b3.move(280,80)
b4=QPushButton("/",t)
b4.move(380,80)
b5=QPushButton("%",t)
b5.move(480,80)
result=QLabel("result = ",t)
result.move(220,150)
def addition():
	num1=int(t1.text())
	num2=int(t2.text())
	num_result1=num1+num2
	result.setText(str(num_result1))
b1.clicked.connect(addition)
def subtraction():
	num1=int(t1.text())
	num2=int(t2.text())
	num_result2=num1-num2
	result.setText(str(num_result2))
b2.clicked.connect(subtraction)	
def MUL():
	num1=int(t1.text())
	num2=int(t2.text())
	num_result3=num1*num2
	result.setText(str(num_result3))
b3.clicked.connect(MUL)	
def div():
	num1=int(t1.text())
	num2=int(t2.text())
	num_result4=num1/num2
	result.setText(str(num_result4))
b4.clicked.connect(div)	
def modulus():
	num1=int(t1.text())
	num2=int(t2.text())
	num_result5=num1%num2
	result.setText(str(num_result5))
b5.clicked.connect(modulus)	
t.show()#show screen
sys.exit(a.exec_())