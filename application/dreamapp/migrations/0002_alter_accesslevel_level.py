# Generated by Django 4.1.2 on 2022-10-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslevel',
            name='level',
            field=models.IntegerField(unique=True),
        ),
    ]