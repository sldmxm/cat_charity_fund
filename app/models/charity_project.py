from sqlalchemy import (
    Column, String, Text
)

from .abstract import ProjectAndDonationAbstractModel


class CharityProject(ProjectAndDonationAbstractModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
