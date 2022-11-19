import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import Ui_catchweek
def open_real(path):
    path=r"C:\Users\dell\Downloads\抓周\\"+path
    from PIL import Image
    import matplotlib.pyplot as plt
    img = Image.open(path)
    
    plt.figure("image")
    plt.imshow(img)
    plt.show()

    plt.close() 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_catchweek.Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
#pyuic5 -o catchweek.py catchweek.ui
#pyrcc5 -o pic_rc.py pic.qrc 