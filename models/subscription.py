import calendar
from datetime import date

from utils.date_utils import get_today


class Subscription:
    def __init__(self, s_date_start, s_date_end, s_status, s_client = None, s_plan = None):
        self.date_start = s_date_start
        self.date_end = s_date_end
        self.status = s_status
        self.cancellation_requested = False
        self.client = s_client
        self.plan = s_plan

    def _calculate_next_date(self, current_date):
        month = current_date.month + 1
        year = current_date.year

        if month > 12:
            month = 1
            year += 1

        last_day = calendar.monthrange(year, month)[1]
        day = min(current_date.day, last_day)

        return date(year, month, day)

    def activate(self, date_start):
        if self.status not in ["pending", "expired"]:
            raise ValueError("Subscription cannot be activated")

        if date_start != get_today():
            raise ValueError("Activation date must be today")
        
        self.date_start = date_start
        self.date_end = self._calculate_next_date(date_start)
        self.status = "active"
        self.cancellation_requested = False

    def renew(self):
        if self.status != "active":
            raise ValueError("Only active subscriptions can be renewed")

        if self.cancellation_requested:
            raise ValueError("Subscription cancellation has been requested")

        today = get_today()

        if today >= self.date_end:
            self.status = "expired"
            raise ValueError("Subscription has expired")

        self.date_end = self._calculate_next_date(self.date_end)

    def cancel(self):
        if self.status != "active":
            raise ValueError("Only active subscriptions can be cancelled")

        today = get_today()

        if today < self.date_end:
            self.cancellation_requested = True
        else:
            self.status = "cancelled"

    def expire(self):
        if self.status != "active":
            raise ValueError("Only active subscriptions can expire")

        today = get_today()

        if today < self.date_end:
            raise ValueError("Subscription has not expired yet")

        if self.cancellation_requested:
            self.status = "cancelled"
        else:
            self.status = "expired"
