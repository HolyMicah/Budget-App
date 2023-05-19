from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton
import sys
import data_handler

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Budget App")
        self.setGeometry(200, 200, 1920, 1080)
        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
            QMainWindow{
                background-color: #3A3335;
            }

            QLabel{
                color: #FDF0D5;
                align-content: center; 
            }

            QLineEdit{
                
            }
        """)

        month_label = QLabel("Month:", self)
        month_label.setGeometry(50, 50, 100, 30)

        self.month_field = QLineEdit(self)
        self.month_field.setGeometry(150, 50, 200, 30)

        income_label = QLabel("Projected Income:", self)
        income_label.setGeometry(50, 100, 100, 30)

        self.income_field = QLineEdit(self)
        self.income_field.setGeometry(150, 100, 200, 30)

        save_button = QPushButton("Save", self)
        save_button.setGeometry(150, 150, 200, 30)
        save_button.clicked.connect(self.save_data)

    def save_data(self):
            month = self.month_field.text()
            projected_income = self.income_field.text()

            data_handler.write_data_to_csv(month, projected_income)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())