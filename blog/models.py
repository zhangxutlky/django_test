from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=32, default="Title")
    content = models.TextField(null=True)
    #author = models.ForeignKey('auth.User')
    #created_date = models.DateTimeField(
    #        default=timezone.now)
    #published_data = models.DateTimeField(
    #        blank=True, null=True)

    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    def __str__(self):
        return self.title
