# Generated by Django 3.1.7 on 2021-10-11 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestpainting',
            name='referencepicture',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
