# Generated by Django 3.1.2 on 2020-10-05 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201005_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distance',
            old_name='destination',
            new_name='source',
        ),
    ]
