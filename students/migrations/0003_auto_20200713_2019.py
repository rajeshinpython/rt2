# Generated by Django 3.0.8 on 2020-07-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200713_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='no',
            field=models.IntegerField(auto_created=True, null=True),
        ),
    ]
