# Generated by Django 3.0.7 on 2020-06-13 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HSSE', '0002_auto_20200610_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='LG_or_LA_or_LM',
            fields=[
                ('Type', models.CharField(choices=[('Lifting_Gear', 'Lifting_Gear'), ('Lifting_Mechine', 'Lifting_Mechine'), ('Lifting_Appliance', 'Lifting_Appliance')], max_length=60, null=True)),
                ('ID_No', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('Weight_or_Length', models.CharField(max_length=60, null=True)),
                ('Group', models.CharField(choices=[('ALFA', 'ALFA'), ('HAB', 'HAB'), ('THIAM', 'THIAM'), ('PEC', 'PEC')], max_length=60, null=True)),
                ('File_No', models.CharField(blank=True, max_length=60, null=True)),
                ('Date_of_inspection', models.DateField()),
                ('Date_of_expiry', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='Name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='employeecourse',
            name='EmployeeID',
            field=models.CharField(max_length=60, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='in_house_training',
            name='Training',
            field=models.CharField(choices=[('Fire_Watchman', 'Fire_Watchman'), ('confined_space', 'confined_space'), ('cut_line_Tape', 'cut_line_Tape'), ('Rigger&Signalman', 'Rigger&Signalman'), ('Pipe_Fitter', 'Pipe_Fitter'), ('Welder', 'Welder'), ('General_Fitter', 'General_Fitter'), ('BA', 'Rigger&Signalman'), ('Turn_Around_Awareness', 'Turn_Around_Awareness'), ('Banksman', 'Banksman'), ('Respirator_Fit_Test', 'Respirator_Fit_Test'), ('Hearing_Test', 'Hearing_Test'), ('NID', 'NID')], max_length=60, null=True),
        ),
    ]
