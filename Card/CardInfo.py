import os
import sys

from PyQt6.QtCore import QRect
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
import sqlite3
from PyQt6.QtWidgets import QWidget, QMessageBox
import pyqtgraph
import random

from AdminFncs.changeInfo.ChangeInfo import ChangeInfo


class CardInfo(QWidget):

    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS  # Временная папка с ресурсами у PyInstaller
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def __init__(self, id, name, quanity, description, expiration_date, price, filename):
        super().__init__()
        self.changeInfoForm = ChangeInfo(id)
        pixmap = QPixmap(filename).copy(QRect(0, 0, 300, 250))
        pixmap = pixmap.scaled(300, 250)

        uic.loadUi("Card/card_info.ui", self)
        self.img.setPixmap(pixmap)
        self.id = id
        self.fill_graph(quanity)

        self.info = None
        with open("AdminFncs/isAdmin.txt", "r") as f:
            self.info = f.read()

        self.addToCartBtn.clicked.connect(self.addToCart)
        self.deleteBtn.clicked.connect(self.deleteFromCart)
        self.changeInfoBtn.clicked.connect(self.changeInfo)

        self.product_name.setText(f"NAME: {name}")
        self.product_quanity.setText(f"QUANITY: {quanity}")
        self.product_price.setText(f"PRICE: {price}")
        self.product_date.setText(f"EXPIRATION_DATE: {expiration_date}")
        self.product_description.setText(description)



    def fill_graph(self, quanity):
        baseLine = quanity // 10
        x = []
        y = []
        for i in range(5):
            x.append(i + 1)
            y.append(baseLine - random.randint(-baseLine // 2, baseLine // 2))
        self.product_graph.plot(x, y)

    def addToCart(self):
        con = sqlite3.connect("products.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS cart"
                    "(Id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "product_id INTEGER);")

        isAlrInCart = cur.execute(
            "SELECT product_id FROM cart WHERE product_id = ?",
            (self.id,)).fetchall()

        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        if len(isAlrInCart):
            msg.setText("This product already in your cart!")
            msg.exec()
        else:
            cur.execute("INSERT INTO cart (product_id) VALUES (?)", (self.id,))
            msg.setText("This product added to your cart!")
            msg.exec()
        con.commit()
        con.close()

    def deleteFromCart(self):
        con = sqlite3.connect("products.db")
        cur = con.cursor()


        isInCart = cur.execute(
            "SELECT product_id FROM cart WHERE product_id = ?",
            (self.id,)).fetchall()

        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        if len(isInCart):
            cur.execute("DELETE FROM cart WHERE product_id = ?", (self.id,))
            msg.setText("This product deleted from your cart!")
            msg.exec()
        else:
            msg.setText("This product not in your cart!")
            msg.exec()
        con.commit()
        con.close()

    def changeInfo(self):
        if self.info == "1":
            self.changeInfoForm.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setText("You are not Admin!")
            msg.exec()





