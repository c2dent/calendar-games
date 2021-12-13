import calendar
from datetime import datetime, timedelta
from .models import Game
from django.views import generic
from django.utils.safestring import mark_safe
from .utils import Calendar


class GamesView(generic.ListView):
    model = Game
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = get_date(self.request.GET.get('month', None), self.request.GET.get('day', None))
        cal = Calendar(date.year, date.month)
        html_calendar = cal.formatmonth(date.year, date.month)
        context['calendar'] = mark_safe(html_calendar)
        context['prev_month'] = prev_month(date)
        context['next_month'] = next_month(date)
        context['games'] = Game.objects.all().filter(datetime__year=date.year, datetime__month=date.month, datetime__day=date.day)
        return context


def get_date(month, day):
    if month:
        year, month = (int(x) for x in month.split('-'))
        if day:
            return datetime(year, month, day=int(day))
        return datetime(year, month, day=1)
    return datetime.today()


def prev_month(date):
    first = date.replace(day=1)
    previous_month = first - timedelta(days=1)
    month = 'month=' + str(previous_month.year) + '-' + str(previous_month.month)
    return month


def next_month(date):
    days_in_month = calendar.monthrange(date.year, date.month)[1]
    last = date.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
