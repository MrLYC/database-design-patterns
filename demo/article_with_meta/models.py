from django.db import models


class ArticleMeta(models.Model):
    title = models.CharField(
        max_length=255, db_index=True,
        null=False, blank=False, default=None,
    )
    author = models.CharField(
        max_length=255, null=False,
        blank=False, default=None,
    )
    update_on = models.DateTimeField(
        auto_now_add=True, auto_now=True,
    )

    @property
    def details(self):
        pass


class ArticleDetails(models.Model):
    meta = models.ForeignKey(ArticleMeta)
    content = models.CharField(
        max_length=65535,
    )
    type = models.CharField(
        max_length=255, choices=(
            ("md", "markdown"),
            ("txt", "text"),
            ("rtxt", "richtext"),
        )
    )
