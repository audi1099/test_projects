# Generated by Django 5.1.6 on 2025-02-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('hours', models.FloatField()),
            ],
        ),
    ]
