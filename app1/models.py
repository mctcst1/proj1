from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=50)
    degree = models.IntegerField(10)

    def __str__(self):
        return '%s: %s' % (self.name, self.degree)