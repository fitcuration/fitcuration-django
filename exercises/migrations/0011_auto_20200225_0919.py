# Generated by Django 3.0.3 on 2020-02-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0010_exercise_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image_url',
            field=models.URLField(),
        ),
    ]
