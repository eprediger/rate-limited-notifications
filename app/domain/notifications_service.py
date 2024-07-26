from datetime import datetime, timedelta

from fastapi import Depends
from sqlalchemy.orm import Session

from app.adapters.io.gateway import Gateway, get_gateway
from app.adapters.persistence.database import get_db
from app.adapters.persistence.notification_rules.repository import get_notification_rule_by_type
from app.adapters.persistence.notifications import repository
from app.domain.notification import NotificationCreate
from app.domain.period import Period
from app.domain.rate_limit_exceeded_error import RateLimitExceededError


class NotificationsService:
    def __init__(self, gateway: Gateway, db: Session):
        self.gateway = gateway
        self.db = db

    def send(self, notification: NotificationCreate):
        notification_rule = get_notification_rule_by_type(self.db, notification.type)

        period = notification_rule.period
        date_from = datetime.utcnow() - timedelta(seconds=Period.to_seconds(period))

        sent_notifications_to_user = repository.get_notifications(
            db=self.db,
            user=notification.user_id,
            notification_type=notification_rule.type,
            date_from=date_from
        )

        if len(sent_notifications_to_user) >= notification_rule.max_per_user:
            raise RateLimitExceededError()

        self.gateway.send(notification)

        return repository.create_notification(self.db, notification)


def get_notifications_service(gateway: Gateway = Depends(get_gateway),
                              db: Session = Depends(get_db)):
    yield NotificationsService(gateway, db)
