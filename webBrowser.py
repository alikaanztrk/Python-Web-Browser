#pip install PyQtWebEngine
#pip install PyQt5

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
#import gerekli kütüphaneler////  import necessary libraries
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser= QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        #create main window and set main url

        navbar= QToolBar()
        self.addToolBar(navbar)

        #ileri buton / forward button
        forwardButton=QAction("İleri",self)
        forwardButton.triggered.connect(self.browser.forward)
        navbar.addAction(forwardButton)
        #geri butonu / back button
        backbutton=QAction("geri",self)
        backbutton.triggered.connect(self.browser.back)
        navbar.addAction(backbutton)
        #yenile butonu///refresh button

        reloadButton= QAction("Yenile",self)
        reloadButton.triggered.connect(self.browser.reload)
        navbar.addAction(reloadButton)

        #ana sayfa butonu //// home button

        homeButton=QAction("Ana Sayfa",self)
        homeButton.triggered.connect(self.navigate_home)
        navbar.addAction(homeButton)

        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(("http://google.com"))

    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())

app= QApplication(sys.argv)
QApplication.setApplicationName("PYTHON BROWSER BY ALIKAAN OZTURK")
window= MainWindow()
app.exec_()

