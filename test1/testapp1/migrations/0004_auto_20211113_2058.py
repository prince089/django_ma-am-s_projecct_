# Generated by Django 3.2.9 on 2021-11-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp1', '0003_auto_20211113_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='role',
            name='modify',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='modify',
            field=models.DateTimeField(),
        ),
    ]
