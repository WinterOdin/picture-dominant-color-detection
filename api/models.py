import uuid
from django.db import models
from imagekit.models import ImageSpecField
from django_extensions.db.fields import AutoSlugField
from imagekit.processors import ResizeToFill, TrimBorderColor, Adjust


class Pictures(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    album_id = models.CharField(max_length=10, unique=True)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    dominant_hex = models.CharField(max_length=7)
    slug = AutoSlugField(populate_from="title", unique=True, max_length=50)
    image = models.ImageField(upload_to="topic", null=True, blank=True)
    image_large = ImageSpecField(source="image",
                                 processors=[ResizeToFill(1440, 900), Adjust(contrast=1.2, sharpness=1.1),
                                             TrimBorderColor()], format="JPEG", options={"quality": 70})
    image_medium = ImageSpecField(source="image",
                                  processors=[ResizeToFill(1280, 720), Adjust(contrast=1.2, sharpness=1.1),
                                              TrimBorderColor()], format="JPEG", options={"quality": 70})
    image_small = ImageSpecField(source="image",
                                 processors=[ResizeToFill(1024, 1024), Adjust(contrast=1.2, sharpness=1.1),
                                             TrimBorderColor()], format="JPEG", options={"quality": 70})

    def __str__(self):
        return str(self.title)