from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette import status

from app.adapters.http.notification_rules import notification_rules_controller
from app.adapters.http.notifications import notifications_controller
from app.adapters.persistence.database import engine
from app.adapters.persistence.notification_rules import model
from app.domain.rate_limit_exceeded_error import RateLimitExceededError

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Rate-Limited Notification Service",
)

app.include_router(notification_rules_controller.router)
app.include_router(notifications_controller.router)

@app.exception_handler(RateLimitExceededError)
async def rate_limit_exception_handler(request: Request, exc: RateLimitExceededError):
    return JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={"message": "Rate limit exceeded"},
    )
