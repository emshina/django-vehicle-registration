# Generated by Django 4.2 on 2023-05-30 06:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("carownerapp", "0007_alter_charges_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="charges",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
