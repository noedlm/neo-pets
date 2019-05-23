# Generated by Django 2.2.1 on 2019-05-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petfinder', '0003_auto_20190521_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='description',
            field=models.CharField(max_length=500, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='size',
            field=models.CharField(max_length=50, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='status',
            field=models.CharField(max_length=50, null=True),
            preserve_default=False,
        ),
    ]