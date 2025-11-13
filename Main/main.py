import sys

from PyQt6 import uic
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from Card.Card import Card
from Cart.cart import Cart

import os, sys

def resource_path(relative_path):
    """Корректный путь к ресурсу."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = resource_path("main.ui")
        uic.loadUi(ui_path, self)
        self.cart.clicked.connect(self.open_cart)
        self.cart = Cart()
        self.init_items()

        self.all.clicked.connect(lambda checked: self.show_products("All"))
        self.fruits.clicked.connect(lambda checked: self.show_products("Fruits"))
        self.vegetables.clicked.connect(lambda checked: self.show_products("Vegetables"))
        self.candies.clicked.connect(lambda checked: self.show_products("Candies"))
        self.meat.clicked.connect(lambda checked: self.show_products("Meat"))
        self.milk.clicked.connect(lambda checked: self.show_products("Milk"))

    def init_items(self):
        con = sqlite3.connect("products.db")
        cur = con.cursor()
        self.products = cur.execute("""SELECT 
            card_db.id,
            card_db.name,
            card_db.quantity,
            card_db.description,
            card_db.expiration_date,
            card_db.price,
            category_db.name AS category
            FROM card_db
            JOIN category_db ON card_db.category_id = category_db.id;""").fetchall()
        for i, (id, name, quanity, description, expiration_date, price, category) in enumerate(self.products):
            card = Card(id, name, quanity, description, expiration_date, price, category)
            row, col = divmod(i, 2)
            self.products_grid.addWidget(card, row, col)
        con.commit()
        cur.close()
        con.close()

    def open_cart(self):
        self.cart = Cart()
        self.cart.show()

    def clear_grid(self):
        while self.products_grid.count():
            item = self.products_grid.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def show_products(self, category):
        self.clear_grid()
        products = [i for i in self.products if category.lower() == i[6].lower()]
        if category.lower() != "all":
            for i, p in enumerate(products):
                row, col = divmod(i, 2)
                card = Card(*p)
                self.products_grid.addWidget(card, row, col)
        else:
            for i, (id, name, quanity, description, expiration_date, price, category) in enumerate(self.products):
                card = Card(id, name, quanity, description, expiration_date, price, category)
                row, col = divmod(i, 2)
                self.products_grid.addWidget(card, row, col)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
