from django.db import models


# Abstract class
class Models(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    SearchableFields = ["id"]

    class Meta:
        abstract = True