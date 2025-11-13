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

class AddProduct(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("AdminFncs/addProduct/addProduct.ui", self)
        self.confrimBtn.clicked.connect(self.addProduct)

    def addProduct(self):
        name = self.setName.text().lower()
        quanity = int(self.setQuanity.text())
        price = float(self.setPrice.text())
        expirationDate = self.setDate.text().lower()
        description = self.setDescription.text().lower()
        category = self.setCategory.text().lower()
        categories = {
            "fruits": 1,
            "vegetables": 2,
            "candies": 3,
            "meat": 4,
            "milk": 5,
        }

        category_id = categories[category]


        con = sqlite3.connect("products.db")
        cur = con.cursor()

        isNameAlrIn = cur.execute("SELECT * FROM card_db WHERE name = ?", (name.capitalize(),)).fetchall()
        if isNameAlrIn:
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setText("Product with this name already exicts!")
            msg.exec()
        else:
            cur.execute(
                "INSERT INTO card_db (name, quantity, description, expiration_date, price, category_id) VALUES (?, ?, ?, ?, ?, ?)",
                (name.capitalize(), quanity, description.capitalize(), expirationDate, price, category_id)
            )
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setText("Product added!")
            msg.exec()
        con.commit()
        con.close()
