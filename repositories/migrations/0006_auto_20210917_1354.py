# Generated by Django 3.0.5 on 2021-09-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0005_auto_20210917_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]