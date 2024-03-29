# Generated by Django 3.1.8 on 2021-07-29 20:11

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meetupapp', '0010_auto_20210729_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='end_date',
            field=models.DateTimeField(default='2021-01-01 12:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meetup',
            name='creator',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
