# Generated by Django 3.1.8 on 2021-07-28 18:36

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meetupapp', '0006_auto_20210728_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='creator',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]