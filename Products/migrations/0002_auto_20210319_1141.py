# Generated by Django 3.1.7 on 2021-03-19 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Quntity', models.IntegerField()),
                ('Size', models.CharField(max_length=10)),
                ('Color', models.CharField(max_length=20)),
                ('Image', models.ImageField(default='default.jpg', upload_to='images')),
                ('CategoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Size', models.CharField(max_length=10)),
                ('Color', models.CharField(max_length=20)),
                ('Image', models.ImageField(default='default.jpg', upload_to='images')),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
