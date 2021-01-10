from django.db import models


# Create your models here.
class ShowcmtComments(models.Model):
    stars = models.IntegerField()
    content = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'showcmt_comments'
