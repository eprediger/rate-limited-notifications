from sqlalchemy import Column, Integer, String

from app.adapters.persistence.database import Base


class NotificationRule(Base):
    __tablename__ = "notification_rules"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False, unique=True, index=True)
    max_per_user = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    period = Column(String, nullable=False)

