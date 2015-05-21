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
INDUSTRY = (
     (0, 'None'),
     (1, 'IT'),
     (2, 'Finance'),
     (3, 'Hardware'),
     (4, 'Bio'),
     (5, 'Others'),
    )

TEAM_STATUS = (
     (0, 'None'),
     (1, 'MVP - SEEKING ANGEL'),
     (2, 'SEEKING - A Round'),
     (3, 'SEEKING - B Round'),
     (4, 'Others'),
    )


class Team(models.Model):
    title = models.CharField(max_length=300) # Team Name
    project_status = models.IntegerField(choices=TEAM_STATUS, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname="team_list", args=[self.id])

    def get_users(self):
        return self.profile_set.all()


class Profile(models.Model):
    members = models.ForeignKey(Team, null=True, blank=True)
    user = models.OneToOneField(User)
    # Basic Info both required
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    # Experience & Skills    
    # Need to investigate how to make as multiple choices as Linkedin
    company = models.CharField(max_length=100, blank= True)
    skills = models.CharField(max_length=100, blank= True)

    industry = models.IntegerField(choices=INDUSTRY, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)

    def __unicode__(self):
        return self.description

    def get_absolute_url(self):
        return reverse(viewname="profile_list", args=[self.id])
