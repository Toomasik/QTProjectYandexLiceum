import os
import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from AdminFncs.deleteProduct.UI_deleteProduct import Ui_deleteProduct

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class DeleteProduct(QWidget, Ui_deleteProduct):
    def __init__(self):
        super().__init__()
        self.deleteName = None
        self.confrimBtn = None
        self.id = id
        self.setupUi(self)
        self.confrimBtn.clicked.connect(self.deleteProduct)

    def deleteProduct(self):
        name = self.deleteName.text().lower()

        db_path = resource_path("products.db")
        con = sqlite3.connect(db_path)
        cur = con.cursor()

        isNameAlrIn = cur.execute("SELECT * FROM card_db WHERE name = ?", (name.capitalize(),)).fetchall()
        if isNameAlrIn:
            cur.execute(
                "DELETE FROM card_db"
                " WHERE name = ?",
                (name.capitalize(),)
            )
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setText("Product Deleted!")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setText("Product do not exicts!")
            msg.exec()

        con.commit()
        con.close()
