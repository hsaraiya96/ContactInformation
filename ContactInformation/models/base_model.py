from django.db import models

__all__ = ['BaseModel']


class BaseModel(models.Model):
    """
    This base model is used to automatically adding
    bellow fields this to all the models
    """
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
