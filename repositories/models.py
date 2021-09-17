from django.db import models

from licenses.models import Licence


class Repository(models.Model):
    name = models.CharField(unique=True, max_length=250)
    full_name = models.CharField(unique=True, max_length=250)
    license = models.ForeignKey(
        Licence,
        verbose_name='Licence',
        on_delete=models.NOT_PROVIDED,
        related_name='repositories',
        blank=False,
        null=False,
    )
    private = models.BooleanField()
    html_url = models.URLField()
    description = models.TextField()
    fork = models.BooleanField()
    language = models.CharField(max_length=250)
    forks_count = models.IntegerField()
    stargazers_count = models.IntegerField()
    watchers_count = models.IntegerField()
    size = models.IntegerField()
    default_branch: models.CharField(max_length=250)
    open_issues_count = models.IntegerField()
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
    has_issues = models.BooleanField()
    has_projects = models.BooleanField()
    has_wiki = models.BooleanField()
    has_pages = models.BooleanField()
    has_downloads = models.BooleanField()
    archived = models.BooleanField()
    disabled = models.BooleanField()
    pushed_at = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    """permissions: {
      admin: false,
      push: false,
      pull: true
    },"""
    allow_rebase_merge = models.BooleanField()
    allow_squash_merge = models.BooleanField()
    allow_auto_merge = models.BooleanField()
    delete_branch_on_merge = models.BooleanField()
    allow_merge_commit = models.BooleanField()
    subscribers_count = models.IntegerField()
    network_count = models.IntegerField()
