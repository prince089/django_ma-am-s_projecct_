# Generated by Django 3.2.9 on 2021-11-13 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp1', '0002_rename_product_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('cityid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('lititude', models.CharField(max_length=22)),
                ('lonigtude', models.CharField(max_length=22)),
                ('created', models.CharField(max_length=100)),
                ('modify', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('clientid', models.AutoField(primary_key=True, serialize=False)),
                ('clientname', models.CharField(max_length=100)),
                ('compenyname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('created', models.CharField(max_length=100)),
                ('modify', models.CharField(max_length=100)),
                ('cityid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp1.city')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('countryid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('lititude', models.CharField(max_length=22)),
                ('lonigtude', models.CharField(max_length=22)),
                ('created', models.CharField(max_length=100)),
                ('modify', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='role',
            name='id',
        ),
        migrations.AddField(
            model_name='role',
            name='roleid',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='whWarehouse',
            fields=[
                ('warehouseid', models.AutoField(primary_key=True, serialize=False)),
                ('warehousename', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('created', models.CharField(max_length=100)),
                ('modify', models.CharField(max_length=100)),
                ('clientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp1.client')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('status', models.CharField(max_length=1)),
                ('created', models.CharField(max_length=100)),
                ('modify', models.CharField(max_length=100)),
                ('roleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp1.role')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('regionid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created', models.CharField(max_length=100)),
                ('modify', models.CharField(max_length=100)),
                ('countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp1.country')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectid', models.AutoField(primary_key=True, serialize=False)),
                ('projecttitle', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('contecnumber', models.IntegerField()),
                ('state', models.CharField(max_length=1)),
                ('created', models.CharField(max_length=100)),
                ('modify', models.CharField(max_length=100)),
                ('cityid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp1.city')),
                ('clientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp1.client')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('plantid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('created', models.CharField(max_length=100)),
                ('modify', models.CharField(max_length=100)),
                ('clientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp1.client')),
            ],
        ),
        migrations.CreateModel(
            name='EquepmentMaster',
            fields=[
                ('equepmentSerialNumbeer', models.CharField(max_length=50)),
                ('equepmentid', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=1)),
                ('created', models.CharField(max_length=100)),
                ('modify', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=200)),
                ('dimension', models.CharField(max_length=50)),
                ('cityid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp1.city')),
                ('plantid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp1.plant')),
            ],
        ),
        migrations.CreateModel(
            name='Equepmentdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equepmentname', models.CharField(max_length=50)),
                ('equepmentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp1.equepmentmaster')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='countryid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp1.country'),
        ),
        migrations.AddField(
            model_name='city',
            name='regionid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp1.region'),
        ),
    ]
