# Generated by Django 3.1.7 on 2021-04-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_board', '0005_auto_20210421_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_up',
            name='supject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
