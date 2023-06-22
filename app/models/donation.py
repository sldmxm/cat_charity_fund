from sqlalchemy import (
    Column, ForeignKey, Integer, Text
)

from .abstract import ProjectAndDonationAbstractModel


class Donation(ProjectAndDonationAbstractModel):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
