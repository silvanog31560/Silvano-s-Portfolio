# Generated by Django 4.1.4 on 2022-12-31 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_technology'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'Technologies'},
        ),
        migrations.AddField(
            model_name='technology',
            name='percent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]