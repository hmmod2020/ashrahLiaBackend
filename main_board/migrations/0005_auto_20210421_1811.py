# Generated by Django 3.1.7 on 2021-04-22 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_board', '0004_auto_20210421_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='numpper',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
