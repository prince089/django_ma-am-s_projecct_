# Generated by Django 3.2.9 on 2021-11-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp1', '0012_auto_20211116_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='clientcity',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='equepmentmaster',
            name='equepmentcity',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='equepmentmaster',
            name='equepmentname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectcity',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='werehousecity',
            field=models.CharField(max_length=100),
        ),
    ]