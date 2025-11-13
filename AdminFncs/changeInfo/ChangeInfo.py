import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox


class ChangeInfo(QWidget):
    def __init__(self, id):
        super().__init__()
        self.id = id
        uic.loadUi("AdminFncs/changeInfo/changeInfo.ui", self)
        self.confrimBtn.clicked.connect(self.changeProduct)

    def changeProduct(self):
        quanity = int(self.changeQuanity.text())
        price = float(self.changePrice.text())
        expirationDate = self.changeDate.text()
        description = self.cahngeDescription.text()
        con = sqlite3.connect("products.db")
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