from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
<<<<<<< HEAD


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
=======
>>>>>>> 616ffbe18db40370cfa9a6c8f7444785d4057556
