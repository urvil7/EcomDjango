# Generated by Django 3.1.7 on 2021-03-24 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_order_quntity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='orders'),
        ),
    ]
