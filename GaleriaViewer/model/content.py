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

from sqlalchemy import Column, Integer, DateTime, Text
from sqlalchemy.orm import relationship
from GaleriaViewer.model.base import Base
from GaleriaViewer.model import content_tag


class Content(Base):
    """Model for all files stored in database"""
    __tablename__ = 'content'

    id = Column(Integer, primary_key=True)

    time_of_add = Column(DateTime)
    time_of_last_modification = Column(DateTime)

    url = Column(Text)
    original_source = Column(Text)

    rate = Column(Integer, nullable=True)

    thumbnail_url = Column(Text, nullable=True)

    tags = relationship('Tag',
                        secondary=content_tag,
                        back_populates='contents'
                        )
