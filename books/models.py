from __future__ import unicode_literals

from django.db import models
from mezzanine.pages.models import Page

# The members of Page will be inherited by the Author model, such
# as title, slug, etc. For authors we can use the title field to
# store the author's name. For our model definition, we just add
# any extra fields that aren't part of the Page model, in this
# case, date of birth.

class Book(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField()
    dob = models.DateField("Date of birth")