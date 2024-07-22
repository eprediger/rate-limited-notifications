from fastapi import FastAPI

from app.adapters.http.notification_rules import notification_rules_controller
from app.adapters.http.notifications import notifications_controller
from app.adapters.persistence.database import engine
from app.adapters.persistence.notification_rules import model

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Rate-Limited Notification Service",
)

app.include_router(notification_rules_controller.router)
app.include_router(notifications_controller.router)
