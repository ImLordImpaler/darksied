# Generated by Django 3.0.5 on 2020-11-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20201031_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]