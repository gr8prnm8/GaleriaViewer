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

from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from GaleriaViewer.model.base import Base
from GaleriaViewer.model import content_tag


class Tag(Base):
    """Model for all tags stored in database"""
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(Text)

    time_of_add = Column(DateTime)
    time_of_last_modification = Column(DateTime)

    thumbnail_id = Column(Integer, ForeignKey('content.id'))
    thumbnail = relationship("Content")

    contents = relationship('Content',
                            secondary=content_tag,
                            back_populates='tags'
                            )
