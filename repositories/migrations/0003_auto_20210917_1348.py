# Generated by Django 3.0.5 on 2021-09-17 10:48

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0001_initial'),
        ('repositories', '0002_auto_20210917_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='license',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.fields.NOT_PROVIDED, related_name='repositories', to='licenses.Licence', verbose_name='Licence'),
        ),
    ]
