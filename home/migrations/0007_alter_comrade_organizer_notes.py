# Generated by Django 4.2.9 on 2024-01-13 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20230503_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comrade',
            name='organizer_notes',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.organizernotes'),
        ),
    ]
