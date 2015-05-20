from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

import os
import uuid

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

# Team choices
STATUS_CHOICES = (
     (0, 'None'),
     (1, 'In Process'),
     (2, 'Finished')
    )

WORKING_STATUS = (
     (0, 'None'),
     (1, 'Part Time'),
     (2, 'Full Time')
    )

class Team(models.Model):
    title = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    project_status = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True)

    image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname="team_list", args=[self.id])

    def get_users(self):
        return self.profile_set.all()


class Profile(models.Model):
    members = models.ForeignKey(Team, null=True, blank=True)
    user = models.ForeignKey(User, unique=True)
    working_status = models.IntegerField(choices=WORKING_STATUS, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse(viewname="profile_list", args=[self.id])
