# Generated by Django 5.1.4 on 2025-01-06 13:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0006_rename_private_link_is_private_remove_profile_likes_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='save',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saves', to=settings.AUTH_USER_MODEL),
        ),
    ]
