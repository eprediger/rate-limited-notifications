from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func

from app.adapters.persistence.database import Base
from app.domain.period import Period


class NotificationRule(Base):
    __tablename__ = "notification_rules"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False, unique=True, index=True)
    max_per_user = Column(Integer, nullable=False)
    period = Column(Enum(Period), nullable=False)

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    type = Column(String, nullable=False)
    sent_at = Column(DateTime, nullable=False, server_default=func.now())
