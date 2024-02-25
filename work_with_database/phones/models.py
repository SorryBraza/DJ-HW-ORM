from django.db import models
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=200, verbose_name='Модель')
    image = models.ImageField()
    price = models.DecimalField(verbose_name='Стоимость', max_digits=20,  decimal_places=2,)
    release_date = models.DateField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})
