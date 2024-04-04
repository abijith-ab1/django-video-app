from django.db import models

# Create your models here.

class VideoAsset(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption