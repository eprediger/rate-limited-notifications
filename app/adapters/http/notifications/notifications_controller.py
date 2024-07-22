from datetime import datetime, timedelta

from fastapi import status, APIRouter
from app.adapters.persistence.notifications import repository
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.adapters.persistence.database import get_db
from app.adapters.persistence.notification_rules.repository import get_notification_rule_by_type
from app.domain.notification import NotificationBase, Notification, NotificationCreate
from app.domain.period import Period

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=Notification)
def send_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    notification_rule = get_notification_rule_by_type(db, notification.type)
    period = notification_rule.period

    date_from = datetime.utcnow() - timedelta(seconds=Period.to_seconds(period))

    sent_notifications_to_user = repository.get_notifications(
        db=db,
        user=notification.user_id,
        notification_type=notification_rule.type,
        date_from=date_from
    )

    if len(sent_notifications_to_user) >= notification_rule.max_per_user:
        return Response(status_code=status.HTTP_429_TOO_MANY_REQUESTS)

    print(f"sending message '{notification.message}' to user '{notification.user_id}'")
    return repository.create_notification(db, notification)
