# Generated by Django 3.0.3 on 2020-02-26 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0014_auto_20200226_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='list_carousel',
        ),
    ]
