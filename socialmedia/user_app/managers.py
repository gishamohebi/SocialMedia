from django.db import models
from datetime import datetime, timedelta


class PostsOfWeek(models.Manager):
    def posts_of_week(self):
        return super().get_queryset().filter(date__gte=datetime.now() - timedelta(days=7))
