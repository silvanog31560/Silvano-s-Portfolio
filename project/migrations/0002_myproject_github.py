# Generated by Django 4.1.4 on 2022-12-25 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproject',
            name='github',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
