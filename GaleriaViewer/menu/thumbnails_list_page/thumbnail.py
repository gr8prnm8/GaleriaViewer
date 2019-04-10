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

import urllib.request

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import PyQt5.Qt as Qt

from GaleriaViewer import settings
import GaleriaViewer.controller.database as db
from GaleriaViewer.model.content import Content
from GaleriaViewer.view.layout.thumbnail import Ui_Form


class ImageThumb(QLabel):
    def __init__(self, content_id):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.content_id = content_id
        self.size = settings.get('thumbnail_size')

        self.show_image(content_id)

        self.setAlignment(Qt.Qt.AlignCenter)

    def show_image(self, content_id: int):
        self.setPixmap(self.resize_image(self.get_image(content_id), self.size))

    @staticmethod
    def get_image(content_id: int) -> QPixmap:
        session = db.get_session()
        content = session.query(Content).get(content_id)

        with urllib.request.urlopen(content.url) as url:
            file = url.read()
        pixmap = QPixmap()
        pixmap.loadFromData(file)
        return pixmap

    @staticmethod
    def resize_image(pixmap: QPixmap, new_size: int):
        if pixmap.height() > new_size:
            return pixmap.scaledToHeight(new_size)

        if pixmap.width() > new_size:
            return pixmap.scaledToWidth(new_size)

