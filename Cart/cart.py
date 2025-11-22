import os
import sys

from PyQt6 import uic
import sqlite3
from PyQt6.QtWidgets import QWidget

from AdminFncs.addProduct.addProduct import AddProduct
from AdminFncs.deleteProduct.deleteProduct import DeleteProduct
from Card.Card import Card
from Cart.UI_cart import Ui_cart


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Cart(QWidget, Ui_cart):
    def __init__(self):
        super().__init__()
        self.isAdmin = None
        self.products_grid = None
        self.addProduct = None
        self.deleteProduct = None
        self.setupUi(self)
        self.init_items()
        self.update()
        self.isAdmin.clicked.connect(self.changeRole)
        self.addProductForm = AddProduct()
        self.deleteProductForm = DeleteProduct()
        self.addProduct.clicked.connect(self.openAddProductForm)
        self.deleteProduct.clicked.connect(self.openDeleteProductForm)

        path = resource_path("AdminFncs/isAdmin.txt")

        with open(path, "r", encoding="utf-8") as f:
            info = f.read()
            if info == "1":
                self.isAdmin.setChecked(True)
            else:
                self.addProduct.setVisible(False)
                self.deleteProduct.setVisible(False)


    def init_items(self):
        db_path = resource_path("products.db")
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        products = cur.execute("""SELECT 
            card_db.id,
            card_db.name,
            card_db.quantity,
            card_db.description,
            card_db.expiration_date,
            card_db.price,
            category_db.name AS category
            FROM card_db
            JOIN category_db ON card_db.category_id = category_db.id 
            WHERE card_db.id IN (SELECT product_id FROM cart)""").fetchall()

        for i, (id, name, quanity, description, expiration_date, price, category) in enumerate(products):
            card = Card(id, name, quanity, description, expiration_date, price, category)
            row, col = divmod(i, 2)
            self.products_grid.addWidget(card, row, col)
        con.commit()
        cur.close()
        con.close()

    def changeRole(self):
        info = None
        path = resource_path("AdminFncs/isAdmin.txt")

        with open(path, "w", encoding="utf-8") as f:
            if self.isAdmin.isChecked():
                info = "1"
                self.addProduct.setVisible(True)
                self.deleteProduct.setVisible(True)
            else:
                info = "0"
                self.addProduct.setVisible(False)
                self.deleteProduct.setVisible(False)

            f.write(info)

    def openAddProductForm(self):
        self.addProductForm.show()
    def openDeleteProductForm(self):
        self.deleteProductForm.show()
