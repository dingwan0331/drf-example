from django.db import models

# Create your models here.
class Comment(models.Model):
    email = models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateTimeField()

    class Meta:
        db_table = "comments"
