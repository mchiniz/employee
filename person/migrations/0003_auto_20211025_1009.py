# Generated by Django 3.2.8 on 2021-10-25 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basemap', '0001_initial'),
        ('person', '0002_alter_user_basemap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='basemap',
        ),
        migrations.AddField(
            model_name='user',
            name='basemap',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basemap.basemap'),
        ),
    ]
