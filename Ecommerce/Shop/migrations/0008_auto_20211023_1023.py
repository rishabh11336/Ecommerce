# Generated by Django 3.2.7 on 2021-10-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_alter_about_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
