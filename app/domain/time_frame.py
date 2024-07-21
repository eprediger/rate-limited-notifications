from pydantic import BaseModel, PositiveInt

from app.domain.period import Period


class TimeFrame(BaseModel):
    amount: PositiveInt
    period: Period
