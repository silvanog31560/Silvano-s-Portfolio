# Generated by Django 4.1.4 on 2022-12-31 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_alter_technology_options_technology_percent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myeducation',
            old_name='technology',
            new_name='tech',
        ),
    ]