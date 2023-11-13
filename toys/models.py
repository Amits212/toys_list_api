from django.db import models

class Toy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, default='')
    toy_category = models.CharField(max_length=200, default='')
    release_date = models.DateTimeField()
    included_in_home = models.BooleanField(default=False)


    class Meta:
        ordering = ('name',)



