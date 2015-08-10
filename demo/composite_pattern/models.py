from django.db import models


class Node(models.Model):
    name = models.CharField(
        max_length=255, default=None,
        null=False, blank=False,
    )

    class Meta:
        abstract = True


class Folder(Node):
    parent = models.ForeignKey('Folder', null=True, default=None)

    @property
    def folders(self):
        return list(Folder.objects.filter(parent=self))

    @property
    def files(self):
        return list(File.objects.filter(parent=self))

    @property
    def children(self):
        nodes = self.folders
        nodes.extend(self.files)
        return nodes


class File(Node):
    parent = models.ForeignKey('Folder')
