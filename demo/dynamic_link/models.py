from ycyc.collections.tagmaps import TagMaps
from django.db import models


class OrderCreater(models.Model):
    Creaters = TagMaps()
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        abstract = True


class Order(models.Model):
    creater_id = models.BigIntegerField(primary_key=True)
    create_by = models.CharField(max_length=255)

    @property
    def creater(self):
        create_cls = OrderCreater.Creaters.get(self.create_by)
        if create_cls.Type == self.create_by:
            return create_cls.objects.get(id=self.creater_id)


@OrderCreater.Creaters.register("Manager")
class Manager(OrderCreater):
    pass


@OrderCreater.Creaters.register("Customer")
class Customer(OrderCreater):
    pass
