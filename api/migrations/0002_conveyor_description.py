# Generated by Django 2.2.2 on 2019-06-20 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conveyor',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
