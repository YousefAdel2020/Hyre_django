# Generated by Django 4.2.2 on 2023-06-17 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Landlord', '0004_alter_tenant_name'),
        ('Tenant', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Landlord.tenant'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Landlord.tenant'),
        ),
        migrations.AlterField(
            model_name='position',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Landlord.tenant'),
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Landlord.tenant'),
        ),
    ]
