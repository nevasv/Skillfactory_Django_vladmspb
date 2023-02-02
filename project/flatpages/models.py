from django.db import models


class UserConfFlatpages(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ImageField(blank=True)
    rating = models.IntegerField(default=1, blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
