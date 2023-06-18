# Generated by Django 4.2.2 on 2023-06-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Landlord', '0004_alter_tenant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='expiration_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='free_trial',
            field=models.BooleanField(default=True),
        ),
    ]
