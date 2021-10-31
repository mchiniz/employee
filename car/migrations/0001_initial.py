# Generated by Django 3.2.8 on 2021-10-23 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.IntegerField(unique=True)),
                ('color', models.CharField(max_length=200)),
                ('plaque', models.CharField(max_length=200)),
            ],
        ),
    ]