import os
import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class DeleteProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.deleteName = None
        self.confrimBtn = None
        self.id = id
        uic.loadUi("AdminFncs/deleteProduct/deleteProduct.ui", self)
        self.confrimBtn.clicked.connect(self.deleteProduct)

    def deleteProduct(self):
        name = self.deleteName.text().lower()


        con = sqlite3.connect("products.db")
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
