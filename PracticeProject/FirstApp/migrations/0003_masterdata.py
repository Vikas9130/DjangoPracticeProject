# Generated by Django 5.0.1 on 2024-01-25 05:26

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0002_address_reader'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterData',
            fields=[
                ('master_data_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstApp.author')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstApp.book')),
            ],
        ),
    ]
