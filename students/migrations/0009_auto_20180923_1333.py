# Generated by Django 2.1.1 on 2018-09-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20180923_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='is_varified',
            new_name='is_lateral',
        ),
        migrations.RemoveField(
            model_name='details',
            name='is_lateral',
        ),
        migrations.AddField(
            model_name='student',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
