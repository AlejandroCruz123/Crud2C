# Generated by Django 5.0.6 on 2024-07-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('civil_status', models.CharField(max_length=20)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('blood_type', models.CharField(max_length=3)),
                ('gsis_id_no', models.CharField(max_length=20)),
                ('pagibig_id_no', models.CharField(max_length=20)),
                ('philhealth_no', models.CharField(max_length=20)),
                ('sss_no', models.CharField(max_length=20)),
                ('tin_no', models.CharField(max_length=20)),
                ('agency_employee_no', models.CharField(max_length=20)),
                ('citizenship', models.CharField(max_length=50)),
                ('residential_address', models.TextField()),
                ('residential_zip_code', models.CharField(max_length=10)),
                ('residential_telephone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('permanent_address', models.TextField()),
                ('permanent_zip_code', models.CharField(max_length=10)),
                ('permanent_telephone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('email_address', models.EmailField(max_length=254)),
                ('cell_phone_no', models.CharField(max_length=20)),
                ('agency_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
