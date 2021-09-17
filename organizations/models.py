from django.db import models


class Organization(models.Model):
    login = models.CharField(unique=True, max_length=250)
    description = models.TextField()

    class Meta:
        ordering = ('login',)

    def __str__(self):
        return self.login
