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
from PyQt5.QtCore import Qt

from sqlalchemy import create_engine
from GaleriaViewer.model import base, content, tag, content_tag
from GaleriaViewer.menu.main_window import MainWindow

engine = create_engine('sqlite:///:memory:', echo=True)

base.Base.metadata.create_all(engine)


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("GaleriaViewer")
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()