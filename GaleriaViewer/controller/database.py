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


import datetime

# SQLAlchemy imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session
from GaleriaViewer.model import base, content, tag, content_tag

engine = create_engine('sqlite:///:memory:', echo=False)


def setup():
    base.Base.metadata.create_all(engine)


def get_session() -> session.Session:
    session = sessionmaker(engine)
    session = session()
    return session


def test():
    session = get_session()
    c1 = content.Content(time_of_add=datetime.datetime.now(), url='file:///home/einrud/Obrazy/Images/01.jpeg', file_type='jpg')
    c2 = content.Content(time_of_add=datetime.datetime.now(), url='file:///home/einrud/Obrazy/Images/01-1.jpeg', file_type='png')
    c3 = content.Content(time_of_add=datetime.datetime.now(), url='file:///home/einrud/Obrazy/Images/1 (1).jpg', file_type='jpg')
    t1 = tag.Tag(name='tag1')
    t2 = tag.Tag(name='tag2')
    t3 = tag.Tag(name='tag3')
    c1.tags.append(t1)
    c1.tags.append(t2)
    c1.tags.append(t3)
    session.add(c1)
    session.add(c2)
    session.add(c3)
    session.add(t1)
    session.add(t2)
    session.add(t3)
    session.commit()