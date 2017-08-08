from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Posts(models.Model):

    post_id = models.CharField(max_length=50, primary_key=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.post_id
