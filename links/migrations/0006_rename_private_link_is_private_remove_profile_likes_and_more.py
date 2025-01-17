# Generated by Django 5.1.4 on 2025-01-06 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0005_link_created_at_alter_link_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='private',
            new_name='is_private',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='likes',
        ),
        migrations.AddField(
            model_name='link',
            name='is_reported',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saves', to='links.link')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saves', to='links.profile')),
            ],
            options={
                'unique_together': {('link', 'profile')},
            },
        ),
    ]
