# Generated by Django 4.2 on 2024-12-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(decimal_places=6, max_digits=6),
        ),
    ]
