from django.db import models


class Group(models.Model):
    name = models.CharField(
        max_length=255, default=None,
        null=False,
    )


class Tag(models.Model):
    name = models.CharField(
        max_length=255, default=None,
        null=False,
    )


class Item(models.Model):
    name = models.CharField(
        max_length=255, default=None,
        null=False,
    )
    group = models.ForeignKey(Group)
    tags_objects = models.ManyToManyField(Tag)

    @property
    def tags(self):
        return self.tags_objects.all()
