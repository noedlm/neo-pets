# Generated by Django 2.2.1 on 2019-05-21 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('animal_type', models.CharField(max_length=50)),
                ('detail_link', models.CharField(max_length=300)),
                ('age', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
            ],
        ),
    ]