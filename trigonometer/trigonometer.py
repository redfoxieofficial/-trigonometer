import  sys
from PyQt5 import QtWidgets
from sys import path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By




class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()


    def init_ui(self):

        self.deger =  QtWidgets.QLineEdit()
        self.giris = QtWidgets.QPushButton("Deger Girin")
        self.yazi_alani = QtWidgets.QLabel("")


        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.deger)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)


        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.setWindowTitle("Trigonometre")
        self.giris.clicked.connect(self.login)

        self.show()


    def login(self):
        sondeger = self.deger.text()

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(executable_path=r"chromedriver.exe",options=chrome_options)

        url = "https://trigonometri-hesaplama.hesabet.com/"

        browser.get(url)

        time.sleep(5)

        input = browser.find_element(By.XPATH,'//*[@id="ctl10_ctl01_tbSayi"]')
        input.clear()
        input.send_keys(sondeger)
        time.sleep(0.2)
        buton = browser.find_element(By.XPATH,'//*[@id="ctl10_ctl01_btnHesapla"]')
        buton.click()


        time.sleep(0.5)

        elements = browser.find_element(By.XPATH,'//*[@id="ctl10_ctl01_dvSonuc"]')

        self.yazi_alani.setText(elements.text)

        browser.close()






app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
