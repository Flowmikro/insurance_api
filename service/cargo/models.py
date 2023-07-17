from django.db import models


class CargoModel(models.Model):
    date = models.DateField()
    cargo_type = models.CharField(max_length=100)
    rate = models.FloatField()
    declared_value = models.FloatField()  # добаваил поде на общую стоимость, его не было в ТЗ, но по друрому не знал как решить. Писал по этому впросы в чат но не было ответа хоть так прочтут =)

    def __str__(self):
        return f'{str(self.date)}, {self.cargo_type}, {self.rate}, {self.declared_value}'



