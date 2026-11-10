from datetime import datetime
from zoneinfo import ZoneInfo

ARGENTINA_TZ = ZoneInfo("America/Argentina/Buenos_Aires")


def get_today():
    return datetime.now(ARGENTINA_TZ).date()
