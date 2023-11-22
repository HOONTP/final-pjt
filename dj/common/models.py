from django.db import models

class ActiveRecordManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class BaseModel(models.Model):
    objects = ActiveRecordManager()

    class Meta:
        abstract = True
