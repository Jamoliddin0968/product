
from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=255, verbose_name=("nomi"))
    value = models.FloatField(default=0, verbose_name=("narxi"))
    description = models.TextField(verbose_name=("Ta'rifi"))
    type = models.CharField(max_length=100, null=True, blank=True, default="")
    img_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = ("Maxsulot")
        verbose_name_plural = ("Maxsulotlar")
