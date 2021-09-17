from django.db import models

from licenses.models import Licence


class Repository(models.Model):
    name = models.CharField(max_length=250)
    full_name = models.CharField(unique=True, max_length=250)
    license = models.ForeignKey(
        Licence,
        verbose_name='Licence',
        on_delete=models.NOT_PROVIDED,
        related_name='repositories',
        blank=True,
        null=True,
    )
    private = models.BooleanField()
    html_url = models.URLField()
    description = models.TextField()
    language = models.CharField(max_length=250, blank=True, null=True)
    forks_count = models.IntegerField()
    size = models.IntegerField()
    default_branch: models.CharField(max_length=250)
    is_template = models.BooleanField()
    template_repository = models.ForeignKey(
        'self',
        verbose_name='Repository',
        on_delete=models.SET_NULL,
        related_name='repositories',
        blank=True,
        null=True,
    )
    """topics: [
      octocat,
      atom,
      electron,
      api
    ],"""
    pushed_at = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    """permissions: {
      admin: false,
      push: false,
      pull: true
    },"""
