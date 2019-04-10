"""
GaleriaViewer - your best bud for managing images.
Copyright (C) 2018  RudEin

Contact me via e-mail: TheRudEin@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from GaleriaViewer import settings
from GaleriaViewer.menu.thumbnails_list_page.page_button import PageButton

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QScrollArea, QDockWidget, QButtonGroup
from GaleriaViewer.view.layout.horizontal_pages_list import Ui_Form


class PagesListDock(QDockWidget):

    def __init__(self):
        super().__init__()
        self.setWidget(PagesList())


class PagesList(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.pages = QButtonGroup()

        self.set_buttons([1, 2, 3, 4, 5, 6, 7], 3)

    def set_buttons(self, buttons: list, active: int):
        for i in buttons:
            if i is str:
                text = i
            else:
                text = str(i)

            if i == active:
                self.add_button(text, True)
            else:
                self.add_button(text)

    def add_button(self, text, pressed=False):
        btn = PageButton(text)
        self.findChild(QScrollArea, 'pagesListScrollArea').widget().layout().addWidget(btn)
        self.pages.addButton(btn)
        btn.setChecked(pressed)
