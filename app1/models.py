from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=50)
    degree = models.IntegerField(8)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '%s: %s' % (self.name, self.degree)


class Id(models.Model):
    id = models.IntegerField(50, primary_key=True)
    id_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.id


class Book(models.Model):
    name = models.CharField(max_length=50)
    book_number = models.IntegerField(20)
    author = models.ManyToManyField(Test)
    test = models.ForeignKey(Id, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Gene(models.Model):
    genes = models.CharField(max_length=50)

    def __str__(self):
        return self.genes

