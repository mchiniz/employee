# Generated by Django 3.2.8 on 2021-10-26 05:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basemap', '0003_alter_basemap_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basemap',
            name='user',
        ),
        migrations.AddField(
            model_name='basemap',
            name='user',
            field=models.ManyToManyField(null=True, related_name='basemap', to=settings.AUTH_USER_MODEL),
        ),
    ]
