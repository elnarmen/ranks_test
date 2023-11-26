from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    price = models.DecimalField(
        "Стоимость",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
