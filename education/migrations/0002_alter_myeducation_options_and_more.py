# Generated by Django 4.1.4 on 2022-12-27 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myeducation',
            options={'ordering': ['created'], 'verbose_name_plural': 'My education'},
        ),
        migrations.AlterField(
            model_name='myeducation',
            name='cert_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
