# Generated by Django 3.1.8 on 2021-07-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetupapp', '0012_auto_20210729_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='location',
            new_name='address',
        ),
        migrations.AddField(
            model_name='job',
            name='choice',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
