from django.db import models


class Licence(models.Model):
    key = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
