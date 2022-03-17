from django.db import models
from django.utils import timezone


class Page(models.Model):
    slug = models.CharField(max_length=254, blank=False, unique=True)
    title = models.CharField(max_length=254, blank=False, default='')
    content = models.TextField(blank=True, default='')
    
    view_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Page, self).save(*args, **kwargs)
