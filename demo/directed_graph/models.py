from django.db import models


class Person(models.Model):
    name = models.CharField(
        max_length=255, default=None,
        null=False,
    )
    friend_objects = models.ManyToManyField('Person')

    @property
    def friends(self):
        return self.friend_objects.all()
