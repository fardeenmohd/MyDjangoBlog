from django.db import models


class Post(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    date = models.DateField()
    content = models.CharField(max_length=255)

    def __str__(self):
        return str(self.content)
