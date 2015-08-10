from django.db import models


class Node(models.Model):
    value = models.CharField(max_length=255)
    next = models.ForeignKey('Node', default=None, null=True)
