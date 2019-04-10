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

from itertools import product
from GaleriaViewer import settings

from PyQt5.QtWidgets import QWidget, QGridLayout
from GaleriaViewer.view.layout.thumbnails_list import Ui_Form
from GaleriaViewer.menu.thumbnails_list_page.thumbnail import ImageThumb


class ThumbnailsList(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.update_thumbs_list([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

    def update_thumbs_list(self, contents: list):
        self.clear_thumbs_list()
        for i, j in product(range(settings.get('thumbs_list_size')[0]), range(settings.get('thumbs_list_size')[1])):
                index = j+i*settings.get('thumbs_list_size')[1]
                if len(contents)-1 < index:
                    break
                self.layout().addWidget(ImageThumb(contents[index]), i, j)

    def clear_thumbs_list(self):
        for i in reversed(range(self.layout().count())):
            self.layout().itemAt(i).widget().deleteLater()
            self.layout().itemAt(i).widget().setParent(None)
