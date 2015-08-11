from django.db import models


class Employee(models.Model):
    leader = models.ForeignKey('Employee', null=True)
    name = models.CharField(max_length=255, null=False, default=None)

    @property
    def subordinates(self):
        return Employee.objects.filter(leader=self)
