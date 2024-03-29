# Generated by Django 3.1.8 on 2021-07-29 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meetupapp', '0009_auto_20210728_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetup',
            old_name='location',
            new_name='city',
        ),
        migrations.AddField(
            model_name='meetup',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meetup',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meetup',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
