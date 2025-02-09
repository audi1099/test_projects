from django.db import models


class CarRecord(models.Model):
    identifier = models.CharField(max_length=20)  # Гос. номер или VIN
    date = models.DateField(auto_now_add=True)  # Дата записи
    hours = models.FloatField()  # Норма-часы

    def __str__(self):
        return f"{self.identifier} - {self.date} - {self.hours}"
