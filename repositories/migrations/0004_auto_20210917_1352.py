# Generated by Django 3.0.5 on 2021-09-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0003_auto_20210917_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='language',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]