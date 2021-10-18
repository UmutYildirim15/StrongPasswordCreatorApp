from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1200, 900)
        self.setWindowTitle("Strong Password App")
        self.setWindowIcon(QIcon("icon.png"))
        self.setStyleSheet("background : AntiqueWhite;")

        self.label_photo = QLabel(self)
        self.labelPassword = QLabel(self)
        self.msg = QMessageBox()
        self.imagePoint = 0
        self.length = 0

        ## Create Button
        self.create = QPushButton('CREATE!!!', self)
        self.create.setStyleSheet("background: #33FFD2; font-size:8pt; font-weight:600;")
        self.create.resize(250, 50)
        self.create.move(120, 350)
        self.create.clicked.connect(self.createPassword)

        ## About me button
        self.about = QPushButton('About', self)
        self.about.setStyleSheet("background: #A3243B; font-size:8pt; font-weight:600;")
        self.about.resize(100, 50)
        self.about.move(0, 850)
        self.about.clicked.connect(self.About)

        self.UiComponents()
        self.show()

    def UiComponents(self):   ## Inputs for users.

        self.label_title = QLabel(self)
        self.label_title.setFixedHeight(45)
        self.label_title.setFixedWidth(500)
        self.label_title.setText("Strong Password Creator")
        self.label_title.setFont(QFont('Times', 25))
        self.label_title.setStyleSheet("color: darkBlue;")
        self.label_title.move(375, 45)

        self.spin = QSpinBox(self)
        self.label_password_length = QLabel(self)
        self.label_password_length.setText("Password Length: ")
        self.label_password_length.setFont(QFont('Times', 12.5))
        self.label_password_length.setGeometry(45, 145, 140, 50)
        self.spin.setGeometry(200, 150, 50, 40)
        self.spin.valueChanged.connect(self.passwordLength)

        self.label_letters = QLabel(self)
        self.label_letters.setText("Letters in the password? ")
        self.label_letters.setFont(QFont('Times', 12.5))
        self.label_letters.setGeometry(45, 190, 195, 60)
        self.checkbox_letters = QCheckBox(self)
        self.checkbox_letters.setGeometry(250, 200, 50, 40)
        self.checkbox_letters.stateChanged.connect(self.lettersChange)

        self.label_uppercase = QLabel(self)
        self.label_uppercase.setText("Uppercase characters in the password? ")
        self.label_uppercase.setFont(QFont('Times', 12.5))
        self.label_uppercase.setGeometry(45, 240, 310, 60)
        self.checkbox_uppercase = QCheckBox(self)
        self.checkbox_uppercase.setGeometry(360, 250, 50, 40)
        self.checkbox_uppercase.stateChanged.connect(self.uppercaseChange)

        self.label_figures = QLabel(self)
        self.label_figures.setText("Figures in the password? ")
        self.label_figures.setFont(QFont('Times', 12.5))
        self.label_figures.setGeometry(45, 290, 200, 60)
        self.checkbox_figures = QCheckBox(self)
        self.checkbox_figures.setGeometry(260, 295, 50, 50)
        self.checkbox_figures.stateChanged.connect(self.figuresChange)

    def passwordLength(self):
        value = self.spin.value()
        return value

    def lettersChange(self):
        return self.checkbox_letters.isChecked()

    def uppercaseChange(self):
        return self.checkbox_uppercase.isChecked()

    def figuresChange(self):
        return self.checkbox_figures.isChecked()

    def createPassword(self):
        letters = ["q", "w", "e", "r", "t", "y", "u", "ı", "o", "p", "ğ", "ü", "a", "s", "d", "f", "g", "h", "j", "k",
                   "l", "ş", "i", "z", "x", "c", "v", "b", "n", "m", "ö", "ç"]   ##32
        figures = ["!", "'", "^", "+", "%", "&", "/", "(", ")", "=", "?", "-", "#", "$", "½", "{", "[", "]", "}", "*",
                   "_", "<", ">", "|", "€", ",", ";", ".", ]   ##28
        password = []

        passwordLength = self.passwordLength()
        indexLength = 0

        lettersChange = self.lettersChange()
        uppercaseChange = self.uppercaseChange()
        figuresChange = self.figuresChange()

        ## Check password strength and suitable photo for it.
        if (passwordLength >= 8):
            self.imagePoint = self.imagePoint + 1
        if (lettersChange == True and passwordLength > 4):
            self.imagePoint = self.imagePoint + 1
        if (uppercaseChange == True and passwordLength > 4):
            self.imagePoint = self.imagePoint + 1
        if (figuresChange == True and passwordLength > 4):
            self.imagePoint = self.imagePoint + 1


        while (indexLength < passwordLength):   ##create password

            index = random.randint(0, passwordLength-1)  ## which index?
            temp1 = random.randint(0, passwordLength-1)  ## how many letters?
            temp2 = random.randint(0, passwordLength-1)  ## how many uppercase letters?
            temp3 = random.randint(0, passwordLength-1)  ## how many figures?

            password.insert(index, random.randint(0, 9))  ## add a random number
            indexLength = indexLength + 1
            if (lettersChange == True and indexLength < passwordLength):
                while (index == temp1):
                    temp1 = random.randint(0, passwordLength-1)
                password.insert(temp1, letters[random.randint(0, 31)])
                indexLength = indexLength + 1    ## add a random letter
            if (uppercaseChange == True and indexLength < passwordLength):
                while (index == temp2 or temp1 == temp2):
                    temp2 = random.randint(0, passwordLength-1)
                password.insert(temp2, letters[random.randint(0, 31)].upper())
                indexLength = indexLength + 1
            if (figuresChange == True and indexLength < passwordLength):
                while (index == temp3 or temp1 == temp3 or temp2 == temp3):
                    temp3 = random.randint(0, passwordLength-1)
                password.insert(temp3, figures[random.randint(0, 27)])
                indexLength = indexLength + 1

        mypassword = ' '.join(map(str, password))
        self.labelPassword.setText("Password: " + mypassword)
        self.labelPassword.setGeometry(100,750,1200,25)
        self.labelPassword.setFont(QFont('Times', 17.5))
        self.labelPassword.setStyleSheet("font-weight: bold; color: #A32443")
        self.addImage(self.imagePoint)
        self.imagePoint = 0   ##set image point 0 each time.

    def addImage(self, image_point):   ## Add image via help of imagePoint
        self.label_photo.setGeometry(700, 100, 550, 500)
        self.msg.setWindowIcon(QtGui.QIcon("seal.png"))
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Password Strength Box")
        self.msg.setDetailedText(" A strong password must be: " + "\n"
                                 "1) At least 8 digits." + "\n"
                                 "2) Contain letters." + "\n"
                                 "3) Contain uppercase letters." + "\n"
                                "4) Contain some figures.")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if(self.imagePoint == 0):
            self.pixmap = QPixmap('poop-removebg-preview.png')
            self.label_photo.setPixmap(self.pixmap)
            self.msg.setText("Your password is too weak!!!")
            self.msg.exec()
        elif(self.imagePoint == 1):
            self.pixmap = QPixmap("angry-removebg-preview.png")
            self.label_photo.setPixmap(self.pixmap)
            self.msg.setText("Your password is weak!!!")
            self.msg.exec()
        elif(self.imagePoint == 2):
            self.pixmap = QPixmap("neutral-removebg-preview.png")
            self.label_photo.setPixmap(self.pixmap)
            self.msg.setText("Your password is neither weak or strong!!!")
            self.msg.exec()
        elif(self.imagePoint == 3):
            self.pixmap = QPixmap("happy-removebg-preview.png")
            self.label_photo.setPixmap(self.pixmap)
            self.msg.setText("Your password is strong!!!")
            self.msg.exec()
        elif(self.imagePoint == 4):
            self.pixmap = QPixmap("very_happy-removebg-preview.png")
            self.label_photo.setPixmap(self.pixmap)
            self.msg.setText("Your password is too strong!!!")
            self.msg.exec()
    def About(self):   ## About me!
        self.msg.setWindowIcon(QtGui.QIcon("seal.png"))
        self.msg.setText("Hello, I am Umut!")
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("About Me")
        self.msg.setDetailedText(" Some information about me: " + "\n"
                                 "1) My Github Profile: https://github.com/Umudikondik " + "\n"
                                 "2) My Linkedin Profile: https://www.linkedin.com/in/umut-y%C4%B1ld%C4%B1r%C4%B1m-19a9b418b/")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec()
App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())