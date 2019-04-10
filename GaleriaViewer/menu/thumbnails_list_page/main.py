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

from PyQt5.QtWidgets import QMainWindow, QScrollArea
from GaleriaViewer.view.layout.main_thumbnails_list import Ui_MainWindow
from GaleriaViewer.menu.thumbnails_list_page.thumbnails_list import ThumbnailsList
from GaleriaViewer.menu.thumbnails_list_page.pages_list import PagesListDock
import PyQt5.Qt as Qt


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.centralWidget().findChild(QScrollArea, 'mainScrollArea').setWidget(ThumbnailsList())
        self.addDockWidget(Qt.Qt.BottomDockWidgetArea, PagesListDock())
