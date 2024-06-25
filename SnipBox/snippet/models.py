from django.db import models

from accounts.models import User


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "Tag"

    def __str__(self):
        return self.title


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    status = models.SmallIntegerField(default=1)

    class Meta:
        db_table = "Snippet"

    def __str__(self):
        return self.title
