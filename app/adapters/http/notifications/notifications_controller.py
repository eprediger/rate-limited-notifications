from fastapi import Depends
from fastapi import status, APIRouter

from app.domain.notification import Notification, NotificationCreate
from app.domain.notifications_service import NotificationsService, get_notifications_service

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=Notification)
def send_notification(notification: NotificationCreate,
                      notification_service: NotificationsService = Depends(get_notifications_service)):
    return notification_service.send(notification)
