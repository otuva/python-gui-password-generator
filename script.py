import random
import string
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QSlider, \
                            QGroupBox, QVBoxLayout, QGridLayout, QCheckBox, QLabel

special_characters = "+!/-#@"


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # properties
        self.title = "Random Password Generator"
        self.top = 150
        self.left = 150
        self.width = 640
        self.height = 480

        # group boxes
        self.include_box = QGroupBox("Random password generator")
        self.slider_box = QGroupBox()
        self.button_box = QGroupBox()

        # bool variables
        self.is_special = True
        self.is_number = True
        self.is_upper = True

        # Widget variables
        self.window_layout = QVBoxLayout()
        self.include_layout = QGridLayout()
        self.slider_layout = QGridLayout()
        self.button_layout = QGridLayout()

        self.length_slider = QSlider()
        self.slider_value = QLabel("15")
        self.output_line = QLineEdit()

        # password
        self.the_password = ""

        # call screen
        self.main_screen()

    def main_screen(self):
        # setting window's properties
        self.setLayout(self.window_layout)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        # add widgets
        self.window_layout.addWidget(self.include_box)
        self.window_layout.addWidget(self.slider_box)
        self.window_layout.addWidget(self.button_box)

        # call widgets
        self.checkbox_widgets()  # first box
        self.slider_widgets()  # second box
        self.button_widgets()  # third box

        # widget layouts
        self.include_box.setLayout(self.include_layout)
        self.slider_box.setLayout(self.slider_layout)
        self.button_box.setLayout(self.button_layout)

        self.show()

    def special_checkbox(self, state):
        if state == Qt.Checked:
            self.is_special = True
        else:
            self. is_special = False

    def number_checkbox(self, state):
        if state == Qt.Checked:
            self.is_number = True
        else:
            self.is_number = False

    def upper_checkbox(self, state):
        if state == Qt.Checked:
            self.is_upper = True
        else:
            self.is_upper = False

    def slider_value_change(self):
        size = self.length_slider.value()
        self.slider_value.setText(str(size))

    def generate_buttons_event(self):
        self.password_creator()
        self.output_line.setText(self.the_password)

    def password_creator(self):
        length = self.length_slider.value()
        if self.is_special and self.is_number and self.is_upper:
            self.the_password = "".join(random.choice(string.ascii_letters + special_characters + string.digits) for x in range(length))

        elif self.is_special and self.is_number:
            self.the_password = "".join(random.choice(string.ascii_lowercase + special_characters + string.digits) for x in range(length))
        elif self.is_special and self.is_upper:
            self.the_password = "".join(random.choice(string.ascii_letters + special_characters) for x in range(length))
        elif self.is_number and self.is_upper:
            self.the_password = "".join(random.choice(string.ascii_letters + string.digits) for x in range(length))

        elif self.is_special:
            self.the_password = "".join(random.choice(string.ascii_lowercase + special_characters) for x in range(length))
        elif self.is_number:
            self.the_password = "".join(random.choice(string.ascii_lowercase + string.digits) for x in range(length))
        elif self.is_upper:
            self.the_password = "".join(random.choice(string.ascii_letters) for x in range(length))

        else:
            self.the_password = "".join(random.choice(string.ascii_lowercase) for x in range(length))

    def checkbox_widgets(self):
        text = QLabel()
        text.setText("Include:")
        self.include_layout.addWidget(text, 0, 0)

        special = QCheckBox("Special Characters")
        special.setCheckState(Qt.Checked)
        special.stateChanged.connect(self.special_checkbox)
        self.include_layout.addWidget(special, 1, 0)

        number = QCheckBox("Numbers (0-9)")
        number.setCheckState(Qt.Checked)
        number.stateChanged.connect(self.number_checkbox)
        self.include_layout.addWidget(number, 1, 1)

        upper = QCheckBox("Uppercase Letters")
        upper.setCheckState(Qt.Checked)
        upper.stateChanged.connect(self.upper_checkbox)
        self.include_layout.addWidget(upper, 1, 2)

    def slider_widgets(self):
        self.length_slider.setOrientation(Qt.Horizontal)
        self.length_slider.setTickInterval(1)
        self.length_slider.setMinimum(4)
        self.length_slider.setMaximum(30)
        self.length_slider.setValue(15)
        self.length_slider.valueChanged.connect(self.slider_value_change)
        self.slider_value.setFont(QFont("Sanserif", 15))

        self.slider_layout.addWidget(self.slider_value, 0, 1)
        self.slider_layout.addWidget(self.length_slider, 0, 0)

    def button_widgets(self):
        generate_button = QPushButton()
        generate_button.setText("Generate")
        generate_button.clicked.connect(self.generate_buttons_event)

        self.button_layout.setRowStretch(1, 5)

        self.button_layout.addWidget(generate_button, 0, 0)
        self.button_layout.addWidget(self.output_line, 1, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
