import os
import sys

from PyQt6.QtCore import QRect
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Card.CardInfo import CardInfo

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Card(QWidget):

    def __init__(self, id, name, quanity, description, expiration_date, price, category):
        super().__init__()
        self.product_quanity = None
        self.img = None
        self.product_price = None
        self.product_name = None

        self.id = id
        self.name = name
        self.quanity = quanity
        self.description = description
        self.expiration_date = expiration_date
        self.price = price

        self.cardInfo = CardInfo(
            self.id,
            self.name,
            self.quanity,
            self.description,
            self.expiration_date,
            self.price,
            category
        )
        self.ImageName = f"Images/{category}.png"
        uic.loadUi("Card/card.ui", self)
        pixmap = QPixmap(self.ImageName).copy(QRect(0, 0, 300, 250))
        pixmap = pixmap.scaled(300, 250)

        self.img.setPixmap(pixmap)
        self.product_name.setText(name)
        self.product_quanity.setText(f"Quanity: {self.quanity} pcs.")
        self.product_price.setText(f"Price: {self.price}$")

    def mousePressEvent(self, event):
        self.cardInfo.close()
        self.cardInfo = CardInfo(
            self.id,
            self.name,
            self.quanity,
            self.description,
            self.expiration_date,
            self.price,
            self.ImageName
        )
        self.cardInfo.show()
