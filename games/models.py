from django.db import models


class Game(models.Model):
    class Status(models.TextChoices):
        RESERVE = 'Резерв'
        PAID = 'Оплачено'
        CARRIED_OUT = 'Проведено'
        CANCELED = 'Отменено'
    datetime = models.DateTimeField()
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    status = models.CharField(max_length=10, choices=Status.choices)

    def __str__(self):
        return self.title
