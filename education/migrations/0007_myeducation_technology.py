# Generated by Django 4.1.4 on 2022-12-31 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_rename_technology_myeducation_tech'),
    ]

    operations = [
        migrations.AddField(
            model_name='myeducation',
            name='technology',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='education.technology'),
        ),
    ]
