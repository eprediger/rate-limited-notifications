from pydantic import BaseModel, PositiveInt, constr

from app.domain.time_frame import TimeFrame


class NotificationRule(BaseModel):
    type: constr(min_length=1)
    max_per_user: PositiveInt
    time_frame: TimeFrame
