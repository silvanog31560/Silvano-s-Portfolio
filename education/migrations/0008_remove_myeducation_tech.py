# Generated by Django 4.1.4 on 2022-12-31 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0007_myeducation_technology'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myeducation',
            name='tech',
        ),
    ]
