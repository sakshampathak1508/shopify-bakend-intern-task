# Generated by Django 3.2.11 on 2022-01-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256)),
                ('image', models.ImageField(blank=True, null=True, upload_to='prod/images')),
                ('price', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('brand', models.CharField(default='', max_length=256)),
                ('stock_count', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(default='', max_length=256)),
                ('about', models.TextField(blank=True)),
            ],
        ),
    ]