import sys
from PySide.QtCore import *
from PySide.QtGui import *

class accounting_calculator(QWidget):
        def __init__(self):
                QWidget.__init__(self, None)

                ## WIDGET ##
                self.nameLabel = QLabel("Name: ")
                self.nameEntry = QLineEdit()

                self.surnameLabel = QLabel("Surname: ")
                self.surnameEntry = QLineEdit()
                
                self.genderLabel = QLabel("Gender: ")
                self.genders = [QRadioButton("Male"), QRadioButton("Female")]
                self.genderButtonGroup = QButtonGroup()

                self.ageLabel = QLabel("Age: ")
                self.ageEntry = QLineEdit()
                
                self.birthLabel = QLabel("BirthDate: ")
                self.birthEntry = QLineEdit("DD/MM/YYYY")
                
                self.emailLabel = QLabel("Email: ")
                self.emailEntry = QLineEdit()

                self.submitButton = QPushButton("Submit")
                self.connect(self.submitButton, SIGNAL("clicked()"), self.submit)

                self.cancelButton = QPushButton("Cancel")
                self.connect(self.cancelButton, SIGNAL("clicked()"), self.cancel)

                ## LAYOUT ##
                pageLayout = QGridLayout()

                genderLayout = QHBoxLayout()
                buttonLayout = QHBoxLayout()

                pageLayout.addWidget(self.nameLabel, 1, 0)
                pageLayout.addWidget(self.nameEntry, 1, 1)

                pageLayout.addWidget(self.surnameLabel, 2, 0)
                pageLayout.addWidget(self.surnameEntry, 2, 1)
                
                pageLayout.addWidget(self.genderLabel, 3, 0)
                for i in range(len(self.genders)):
                        genderLayout.addWidget(self.genders[i])
                        self.genderButtonGroup.addButton(self.genders[i],i)
                pageLayout.addLayout(genderLayout, 3, 1)

                pageLayout.addWidget(self.ageLabel, 4, 0)
                pageLayout.addWidget(self.ageEntry, 4, 1)
                
                pageLayout.addWidget(self.birthLabel, 5, 0)
                pageLayout.addWidget(self.birthEntry, 5, 1)

                pageLayout.addWidget(self.emailLabel, 6, 0)
                pageLayout.addWidget(self.emailEntry, 6, 1)

                buttonLayout.addWidget(self.cancelButton)
                buttonLayout.addWidget(self.submitButton)
                pageLayout.addLayout(buttonLayout, 7, 1)
 

                self.setLayout(pageLayout)

        def submit(self):
                outfile = open("profile.txt", "a")
                outfile.write("\n\n")
                outfile.write("Name: " + self.nameEntry.text() + "\n")
                outfile.write("Surname: " + self.surnameEntry.text() + "\n")
                
                self.genderButtonGroup.setExclusive(False)
                if(self.genderButtonGroup.checkedId() == 0):
                        outfile.write("Gender: Male\n")
                        self.genders[0].setChecked(False)
                else:
                        outfile.write("Gender: Female\n")
                        self.genders[1].setChecked(False)
                self.genderButtonGroup.setExclusive(True)
                
                outfile.write("Age: " + self.ageEntry.text() + "\n")
                outfile.write("Birthday: " + self.birthEntry.text() + "\n")
                outfile.write("Email: " + self.emailEntry.text() + "\n")

                
                self.nameEntry.setText("")
                self.surnameEntry.setText("")
                self.ageEntry.setText("")
                self.birthEntry.setText("DD/MM/YYYY")
                self.emailEntry.setText("")

        def cancel(self):
                dialog = QDialog(self)

                layout = QVBoxLayout()
                   
                label = QLabel("You need to fill all the information\nbefore using this program :)")
                closeButton = QPushButton("OK")
                self.connect(closeButton, SIGNAL("clicked()"), dialog.close)


                layout.addWidget(label)
                layout.addWidget(closeButton)

                dialog.setLayout(layout)
                dialog.show()
                

def main():
        app = QApplication(sys.argv)

        a = accounting_calculator()
        a.show()

        return app.exec_()

if __name__ == "__main__":
        sys.exit(main())
