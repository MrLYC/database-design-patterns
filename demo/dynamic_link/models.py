from django.db import models


class OrderCreater(models.Model):
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        abstract = True


class Order(models.Model):
    creater_id = models.BigIntegerField(primary_key=True)
    create_by = models.CharField(max_length=255)

    @property
    def creater(self):
        for create_cls in OrderCreater.__subclasses__():
            if create_cls.Type == self.create_by:
                return create_cls.objects.get(id=self.creater_id)


class Manager(OrderCreater):
    Type = "Manager"


class Customer(OrderCreater):
    Type = "Customer"
