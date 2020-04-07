# Generated by Django 3.0.3 on 2020-03-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_remove_category_exercises'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AddField(
            model_name='category',
            name='short_name',
            field=models.TextField(blank=True, max_length=10),
        ),
    ]
