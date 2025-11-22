import os
import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from AdminFncs.changeInfo.UI_changeInfo import Ui_changeInfo

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class ChangeInfo(QWidget, Ui_changeInfo):
    def __init__(self, id):
        super().__init__()
        self.confrimBtn = None
        self.changeQuanity = None
        self.changePrice = None
        self.cahngeDescription = None
        self.changeDate = None
        self.id = id
        self.setupUi(self)
        self.confrimBtn.clicked.connect(self.changeProduct)

    def changeProduct(self):
        quanity = int(self.changeQuanity.text())
        price = float(self.changePrice.text())
        expirationDate = self.changeDate.text()
        description = self.cahngeDescription.text()
        db_path = resource_path("products.db")
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        cur.execute("UPDATE card_db SET "
                    "quantity = ?,"
                    "price = ?,"
                    "expiration_date = ?,"
                    "description = ? WHERE id = ?",
                    (quanity, price, expirationDate, description, self.id))

        con.commit()
        con.close()

        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setText("Product was changed!")
        msg.exec()