# Generated by Django 2.1.5 on 2019-04-30 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0021_contributions_technical_contests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='land_phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]