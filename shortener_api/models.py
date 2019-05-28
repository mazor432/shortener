from django.contrib.auth import get_user_model
from django.db import models

from .utils import create_shortcode

User = get_user_model()


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Url(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')
    url = models.CharField(max_length=2500)
    shortcode = models.CharField(max_length=15, unique=True, blank=False, null=False, )
    description = models.TextField(null=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(Url, self).save(*args, **kwargs)
