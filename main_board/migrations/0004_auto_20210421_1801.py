# Generated by Django 3.1.7 on 2021-04-22 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_board', '0003_auto_20210421_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='numpper',
            field=models.IntegerField(max_length=15, null=True),
        ),
    ]
