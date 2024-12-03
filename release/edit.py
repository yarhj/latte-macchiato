import sys
import sqlite3

from edit_widget import Ui_EditForm
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox


class Edit(QWidget, Ui_EditForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(self.size())
        self.setWindowTitle('Редактор')

        self.btnAdd.clicked.connect(self.add)
        self.btnEdit.clicked.connect(self.edit)
        self.btnBack.clicked.connect(self.back)

        self.con = sqlite3.connect("../data/coffee.sqlite")
        self.cursor = self.con.cursor()

        self.show()

    def add(self):
        coffee_id = self.spinID.value()
        title = self.lineTitle.text()
        combo_box = self.comboBox.currentText()
        combo_roasting = self.comboRoasting.currentText()
        combo_type = self.comboType.currentText()
        line_taste = self.lineTaste.text()
        spin_price = self.spinPrice.value()
        spin_volume = self.spinVolume.value()

        columns = []
        values = []

        if title:
            columns.append("title")
            values.append(title)
        if combo_box:
            columns.append("comboBox")
            values.append(combo_box)
        if combo_roasting:
            columns.append("comboRoasting")
            values.append(combo_roasting)
        if combo_type:
            columns.append("comboType")
            values.append(combo_type)
        if line_taste:
            columns.append("lineTaste")
            values.append(line_taste)
        if spin_price:
            columns.append("spinPrice")
            values.append(spin_price)
        if spin_volume:
            columns.append("spinVolume")
            values.append(spin_volume)

        if columns:
            placeholders = ", ".join("?" for _ in columns)
            query = f"INSERT INTO coffee ({', '.join(columns)}) VALUES ({placeholders})"
            try:
                self.cursor.execute(query, tuple(values))
                self.con.commit()
                QMessageBox.information(self, "Сообщение", "Кофе добавлено")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка добавления: {e}")

    def edit(self):
        coffee_id = self.spinID.value()
        title = self.lineTitle.text()
        combo_box = self.comboBox.currentText()
        combo_roasting = self.comboRoasting.currentText()
        combo_type = self.comboType.currentText()
        line_taste = self.lineTaste.text()
        spin_price = self.spinPrice.value()
        spin_volume = self.spinVolume.value()

        set_clause = []
        values = []

        if title:
            set_clause.append("title = ?")
            values.append(title)
        if combo_box:
            set_clause.append("sort = ?")
            values.append(combo_box)
        if combo_roasting:
            set_clause.append("roasting = ?")
            values.append(combo_roasting)
        if combo_type:
            set_clause.append("type = ?")
            values.append(combo_type)
        if line_taste:
            set_clause.append("taste = ?")
            values.append(line_taste)
        if spin_price:
            set_clause.append("price = ?")
            values.append(spin_price)
        if spin_volume:
            set_clause.append("volume = ?")
            values.append(spin_volume)

        if set_clause:
            query = f"UPDATE coffee SET {', '.join(set_clause)} WHERE id = ?"
            values.append(coffee_id)
            try:
                self.cursor.execute(query, tuple(values))
                self.con.commit()
                QMessageBox.information(self, "Сообщение", "Кофе изменено")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка изменения: {e}")

    def closeEvent(self, event):
        self.con.close()

    def back(self):
        from table import Cappuccino
        self.hide()
        self.main_window = Cappuccino()
        self.main_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Edit()
    sys.exit(app.exec())
