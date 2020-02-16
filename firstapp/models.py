from django.db import models

class Persons(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    addtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'persons'
