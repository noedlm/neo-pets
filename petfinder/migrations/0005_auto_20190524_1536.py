# Generated by Django 2.2.1 on 2019-05-24 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petfinder', '0004_auto_20190522_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='image',
            new_name='image_small',
        ),
        migrations.AddField(
            model_name='pet',
            name='image_full',
            field=models.CharField(default='http://placekitten.com/400/550', max_length=300),
        ),
    ]
