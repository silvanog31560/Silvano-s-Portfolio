# Generated by Django 4.1.4 on 2023-01-21 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_myproject_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproject',
            name='github_url',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='myproject',
            name='link_url',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
