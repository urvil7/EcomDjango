# Generated by Django 3.1.7 on 2021-03-26 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20210326_1324'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactU',
            new_name='Contact',
        ),
    ]