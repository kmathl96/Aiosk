# Generated by Django 2.2.16 on 2020-11-12 06:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kiosks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
