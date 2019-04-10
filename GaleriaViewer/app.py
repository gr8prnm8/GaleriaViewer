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

import sys

from PyQt5 import QtWidgets
from GaleriaViewer.menu.thumbnails_list_page.main import Main
from GaleriaViewer.menu.thumbnails_list_page.thumbnails_list import ThumbnailsList
import GaleriaViewer.controller.database as db


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = Main()
    window.setWindowTitle("GaleriaViewer")

    window.show()

    sys.exit(app.exec_())


db.setup()
db.test()


if __name__ == '__main__':
    main()
