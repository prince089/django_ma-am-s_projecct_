# Generated by Django 3.2.9 on 2021-11-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp1', '0004_auto_20211113_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='modify',
            field=models.DateTimeField(auto_now=True),
        ),
    ]