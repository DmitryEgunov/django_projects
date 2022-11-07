from django.db import models
from django.urls import reverse

class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
    # TODO: Добавьте требуемые поля

    def get_absolute_url(self):
        return reverse('phone_detail', kwargs={'slug': self.slug})
