# Generated by Django 2.2 on 2019-05-01 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Id',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name=50)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.Id'),
        ),
    ]
