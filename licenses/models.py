from django.db import models


class Licence(models.Model):
    key = models.SlugField(unique=True)
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
