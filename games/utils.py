from datetime import datetime
from calendar import HTMLCalendar


class Calendar(HTMLCalendar):
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day: int, weekday: int) -> str:
        if day != 0:
            query = "{% url `games:index` %}?{{month="+ str(self.year) + "-" + str(self.month) + "&&day=" + str(day) + "}}"
            return f"<td><a class='btn btn-info left' href='?month={self.year}-{self.month}&&day={day}'>{day}</a></td>"
        return f"<td></td>"