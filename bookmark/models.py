from django.db import models


# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __srt__(self):
        return self.title

