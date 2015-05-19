from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse

import os
import uuid

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)


class Team(models.Model):
    title = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname="team_list", args=[self.id])
