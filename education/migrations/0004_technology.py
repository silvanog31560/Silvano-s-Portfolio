# Generated by Django 4.1.4 on 2022-12-30 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_myeducation_default_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
