from django.db import models


class Owner(models.Model):
    login = models.SlugField(unique=True)
    type = models.CharField(max_length=100)

    class Meta:
        ordering = ('login',)

    def __str__(self):
        return self.login
