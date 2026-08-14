import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QKeySequence, QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar
from PyQt6.QtWebEngineWidgets import QWebEngineView
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
         
        # Create a web view
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("https://www.duckduckgo.com/"))
        self.setCentralWidget(self.web_view)
 
        # Create a toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
         
        # Add a back action to the toolbar
        back_action = QAction("Back", self)
        back_action.setShortcut(QKeySequence("Back"))
        back_action.triggered.connect(self.web_view.back)
        toolbar.addAction(back_action)
         
        # Add a forward action to the toolbar
        forward_action = QAction("Forward", self)
        forward_action.setShortcut(QKeySequence("Forward"))
        forward_action.triggered.connect(self.web_view.forward)
        toolbar.addAction(forward_action)
         
        # Add a reload action to the toolbar
        reload_action = QAction("Reload", self)
        reload_action.setShortcut(QKeySequence("Refresh"))
        reload_action.triggered.connect(self.web_view.reload)
        toolbar.addAction(reload_action)
         
        # Add a search bar to the toolbar
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.load_url)
        toolbar.addWidget(self.search_bar)
         
         
    def load_url(self):
        url = self.search_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.web_view.load(QUrl(url))
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
