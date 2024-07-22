from datetime import datetime

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.adapters.persistence.notification_rules import model
from app.domain.notification import NotificationCreate


def get_notifications(db: Session, user: str, notification_type: str, date_from: datetime):
    return db.query(model.Notification).filter(
        and_(model.Notification.user_id == user,
             model.Notification.type == notification_type,
             model.Notification.sent_at >= date_from
             )
    ).all()


def create_notification(db: Session, notification: NotificationCreate):
    db_notification = model.Notification(
        type=notification.type,
        user_id=notification.user_id
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)

    return db_notification
