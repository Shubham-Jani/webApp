from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()

    class Meta:
        db_table = 'note'

    def __str__(self):
        return self.title
