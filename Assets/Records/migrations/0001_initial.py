# Generated by Django 5.0.1 on 2024-01-05 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employee', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_assign_date', models.DateField(blank=True, null=True)),
                ('asset_returning_date', models.DateField(blank=True, null=True)),
                ('Asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.asset')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.employee')),
            ],
        ),
    ]
