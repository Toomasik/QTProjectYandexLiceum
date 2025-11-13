import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox


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
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        con = sqlite3.connect("products.db")
        cur = con.cursor()

        isNameAlrIn = cur.execute("SELECT * FROM card_db WHERE name = ?", (name.capitalize(),)).fetchall()
        if isNameAlrIn:
            msg.setText("Product with this name already exicts!")
        else:
            cur.execute(
                "INSERT INTO card_db (name, quantity, description, expiration_date, price, category_id) VALUES (?, ?, ?, ?, ?, ?)",
                (name.capitalize(), quanity, description.capitalize(), expirationDate, price, category_id)
            )
            msg.setText("Product added!")

        con.commit()
        con.close()

        msg.exec()