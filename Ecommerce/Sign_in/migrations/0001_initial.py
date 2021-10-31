# Generated by Django 3.2.7 on 2021-10-10 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=10)),
                ('description', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
    ]
