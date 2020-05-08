from uuid import uuid4

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    """
    Instance of used car
    """

    slug = models.SlugField(max_length=200, unique=True)
    brand = models.CharField(_("car brand"), max_length=50)
    model = models.CharField(_("car model"), max_length=50)
    location = models.CharField(_("car location"), max_length=50)
    year = models.PositiveSmallIntegerField(_("model year"))
    km_driven = models.PositiveIntegerField(_("kilometer driven"))
    fuel_type = models.CharField(_("fuel type"), max_length=50)
    transmission = models.CharField(_("transmission"), max_length=50)
    owner_type = models.CharField(_("owner type"), max_length=50)
    mileage = models.DecimalField(_("car mileage"), max_digits=10, decimal_places=2)
    engine = models.DecimalField(_("engine size"), max_digits=10, decimal_places=2)
    power = models.DecimalField(_("engine power"), max_digits=10, decimal_places=2)
    seats = models.FloatField(_("seating capacity"))
    price = models.DecimalField(_("car price (N)"), max_digits=12, decimal_places=2)

    class Meta:
        ordering = ('brand', 'model', 'year')
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"

    def get_slug(self):
        slug = slugify(f"{self.brand} {self.model} {self.year}")
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = self.get_slug()
            self.slug = f"{slug}-{str(uuid4()).split('-')[0]}"
        return super().save(*args, **kwargs)
