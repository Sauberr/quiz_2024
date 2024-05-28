from django.db import models


class BaseModel(models.Model):
    create_datetime = models.DateTimeField(auto_now_add=True, null=True)
    last_update = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
