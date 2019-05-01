# Generated by Django 2.2 on 2019-05-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20190430_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('book_number', models.IntegerField(verbose_name=20)),
                ('author', models.ManyToManyField(to='app1.Test')),
            ],
        ),
    ]