# Generated by Django 3.1.7 on 2021-03-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Description', models.TextField(max_length=100)),
                ('Image', models.ImageField(default='default.img', upload_to='images')),
            ],
        ),
    ]
