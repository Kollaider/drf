# Generated by Django 4.1.3 on 2022-11-24 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women',
            old_name='cat',
            new_name='category',
        ),
    ]
