import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox


class DeleteProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.id = id
        uic.loadUi("AdminFncs/deleteProduct/deleteProduct.ui", self)
        self.confrimBtn.clicked.connect(self.deleteProduct)

    def deleteProduct(self):
        name = self.deleteName.text().lower()
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        con = sqlite3.connect("products.db")
        cur = con.cursor()

        isNameAlrIn = cur.execute("SELECT * FROM card_db WHERE name = ?", (name.capitalize(),)).fetchall()
        if isNameAlrIn:
            cur.execute(
                "DELETE FROM card_db"
                " WHERE name = ?",
                (name.capitalize(),)
            )
            msg.setText("Product Deleted!")
        else:

            msg.setText("Product do not exicts!")

        con.commit()
        con.close()
        msg.exec()