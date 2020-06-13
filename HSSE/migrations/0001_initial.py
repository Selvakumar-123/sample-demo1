# Generated by Django 3.0.7 on 2020-06-09 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeID', models.CharField(max_length=60, null=True)),
                ('EmployeeName', models.CharField(max_length=60, null=True)),
                ('Designation', models.CharField(choices=[('Manager', 'Manager'), ('Supervisor', 'Supervisor'), ('HSSE_Leader', 'HSSE_Leader'), ('Admin', 'Admin'), ('Pipe_Fitter', 'Pipe_Fitter'), ('Welder', 'Welder'), ('General_Fitter', 'General_Fitter')], max_length=60, null=True)),
                ('Group', models.CharField(choices=[('ALFA', 'ALFA'), ('HAB', 'HAB'), ('THIAM', 'THIAM'), ('PEC', 'PEC')], max_length=60, null=True)),
                ('Type_of_LOA', models.CharField(choices=[('Boom Lift Operator', 'Boom Lift Operator'), ('Confined Space Authorized Manager', 'Confined Space Authorized Manager'), ('Confined Space Safety Assessor', 'Confined Space Safety Assessor'), ('Confined Space Watchman', 'Confined Space Watchman'), ('Coordinator of Health, Safety, Security & Environment (HSSE)', 'Coordinator of Health, Safety, Security & Environment (HSSE)'), ('Crane Operator', 'Crane Operator'), ('Driver ', 'Driver '), ('Hazardous Substance and Chemical Controller', 'Hazardous Substance and Chemical Controller'), ('Forklift Truck Operator', 'Forklift Truck Operator'), (' Lifting Supervisor', ' Lifting Supervisor'), (' Occupational First Aide', ' Occupational First Aide'), ('Overhead Crane Operator', 'Overhead Crane Operator'), ('PTW Authorized Applicant', 'PTW Authorized Applicant'), ('Rigger', 'Rigger'), ('FireWatchman', 'FireWatchman')], max_length=60, null=True)),
                ('File_No', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BiCycle_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeID1', models.CharField(max_length=60, null=True)),
                ('EmployeeID2', models.CharField(max_length=60, null=True)),
                ('EmployeeName1', models.CharField(max_length=60, null=True)),
                ('EmployeeName2', models.CharField(max_length=60, null=True)),
                ('Designation1', models.CharField(choices=[('Manager', 'Manager'), ('Supervisor', 'Supervisor'), ('HSSE_Leader', 'HSSE_Leader'), ('Admin', 'Admin'), ('Pipe_Fitter', 'Pipe_Fitter'), ('Welder', 'Welder'), ('General_Fitter', 'General_Fitter')], max_length=60, null=True)),
                ('Designation2', models.CharField(choices=[('Manager', 'Manager'), ('Supervisor', 'Supervisor'), ('HSSE_Leader', 'HSSE_Leader'), ('Admin', 'Admin'), ('Pipe_Fitter', 'Pipe_Fitter'), ('Welder', 'Welder'), ('General_Fitter', 'General_Fitter')], max_length=60, null=True)),
                ('Group', models.CharField(choices=[('ALFA', 'ALFA'), ('HAB', 'HAB'), ('THIAM', 'THIAM'), ('PEC', 'PEC')], max_length=60, null=True)),
                ('File', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='DailyManpower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(null=True)),
                ('ALFA', models.CharField(blank=True, max_length=60, null=True)),
                ('HAB', models.CharField(blank=True, max_length=60, null=True)),
                ('THIAM', models.CharField(blank=True, max_length=60, null=True)),
                ('PEC', models.CharField(blank=True, max_length=60, null=True)),
                ('PGS_SCAFFOLD', models.CharField(blank=True, max_length=60, null=True)),
                ('PGS_INSULATION', models.CharField(blank=True, max_length=60, null=True)),
                ('PEI', models.CharField(blank=True, max_length=60, null=True)),
                ('PSE', models.CharField(blank=True, max_length=60, null=True)),
                ('EBT', models.CharField(blank=True, max_length=60, null=True)),
                ('AD_METH', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('file', models.FileField(upload_to='object')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeID', models.CharField(max_length=60, null=True)),
                ('EmployeeName', models.CharField(max_length=60, null=True)),
                ('Designation', models.CharField(choices=[('Manager', 'Manager'), ('Supervisor', 'Supervisor'), ('HSSE_Leader', 'HSSE_Leader'), ('Pipe_Fitter', 'Pipe_Fitter'), ('Welder', 'Welder'), ('General_Fitter', 'General_Fitter')], max_length=60, null=True)),
                ('Group', models.CharField(choices=[('ALFA', 'ALFA'), ('HAB', 'HAB'), ('THIAM', 'THIAM'), ('PEC', 'PEC')], max_length=60, null=True)),
                ('SRC_Pass_No', models.CharField(blank=True, max_length=60, null=True)),
                ('IIFDate', models.DateField(blank=True, null=True)),
                ('Work_Permit_Date', models.DateField(blank=True, null=True)),
                ('Permit_Applicant_Date', models.DateField(blank=True, null=True)),
                ('Work_at_Height_Date', models.DateField(blank=True, null=True)),
                ('Confined_Space_Date', models.DateField(blank=True, null=True)),
                ('Process_Plant_Date', models.DateField(blank=True, null=True)),
                ('BA_Date', models.DateField(blank=True, null=True)),
                ('Rigger_and_Signalman_Date', models.DateField(blank=True, null=True)),
                ('ForkLift_Date', models.DateField(blank=True, null=True)),
                ('Boom_Lift_Date', models.DateField(blank=True, null=True)),
                ('Over_Head_Crane_Date', models.DateField(blank=True, null=True)),
                ('Scaffold_Erection_Date', models.DateField(blank=True, null=True)),
                ('Chemical_Handlers_Date', models.DateField(blank=True, null=True)),
                ('Bi_Safe_Level_Date', models.DateField(blank=True, null=True)),
                ('Gotcha_Kit_Date', models.DateField(blank=True, null=True)),
                ('First_Aid_Date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FRC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeID', models.CharField(max_length=60, null=True)),
                ('EmployeeName', models.CharField(max_length=60, null=True)),
                ('Designation', models.CharField(choices=[('Manager', 'Manager'), ('Supervisor', 'Supervisor'), ('HSSE_Leader', 'HSSE_Leader'), ('Admin', 'Admin'), ('Pipe_Fitter', 'Pipe_Fitter'), ('Welder', 'Welder'), ('General_Fitter', 'General_Fitter')], max_length=60, null=True)),
                ('Group', models.CharField(choices=[('ALFA', 'ALFA'), ('HAB', 'HAB'), ('THIAM', 'THIAM'), ('PEC', 'PEC')], max_length=60, null=True)),
                ('ShirtSize', models.CharField(blank=True, choices=[('s', 's'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL'), ('Nomex', 'Nomex')], max_length=60)),
                ('QTY0', models.CharField(blank=True, choices=[('1', '1'), ('2', '2')], max_length=60)),
                ('PantSize', models.CharField(blank=True, choices=[('28', '28'), ('30', '30'), ('32', '32'), ('34', '34'), ('36', '36'), ('38', '38'), ('Nomex', 'Nomex')], max_length=60)),
                ('QTY1', models.CharField(blank=True, choices=[('1', '1'), ('2', '2')], max_length=60)),
                ('BootSize', models.CharField(blank=True, choices=[('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=60)),
                ('QTY2', models.CharField(blank=True, choices=[('1', '1'), ('2', '2')], max_length=60)),
                ('Helmet', models.CharField(blank=True, choices=[('Yellow', 'Yellow'), ('Red', 'Red'), ('White', 'White'), ('Blue', 'Blue')], max_length=60)),
                ('QTY3', models.CharField(blank=True, choices=[('1', '1'), ('2', '2')], max_length=60)),
                ('PR', models.CharField(max_length=60)),
                ('issued_Date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='In_House_Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeID', models.CharField(max_length=60, null=True)),
                ('EmployeeName', models.CharField(max_length=60, null=True)),
                ('Designation', models.CharField(choices=[('Manager', 'Manager'), ('Supervisor', 'Supervisor'), ('HSSE_Leader', 'HSSE_Leader'), ('Admin', 'Admin'), ('Pipe_Fitter', 'Pipe_Fitter'), ('Welder', 'Welder'), ('General_Fitter', 'General_Fitter')], max_length=60, null=True)),
                ('Group', models.CharField(choices=[('ALFA', 'ALFA'), ('HAB', 'HAB'), ('THIAM', 'THIAM'), ('PEC', 'PEC')], max_length=60, null=True)),
                ('File', models.FileField(null=True, upload_to='')),
                ('File_No', models.CharField(max_length=60, null=True)),
                ('AttendDate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('birth_date', models.DateField()),
                ('contact', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActionDate', models.DateField(null=True)),
                ('Action', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Short_Service_Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeID', models.CharField(max_length=60, null=True)),
                ('EmployeeName', models.CharField(max_length=60, null=True)),
                ('Designation', models.CharField(choices=[('Manager', 'Manager'), ('Supervisor', 'Supervisor'), ('HSSE_Leader', 'HSSE_Leader'), ('Pipe_Fitter', 'Pipe_Fitter'), ('Welder', 'Welder'), ('General_Fitter', 'General_Fitter')], max_length=60, null=True)),
                ('Group', models.CharField(choices=[('ALFA', 'ALFA'), ('HAB', 'HAB'), ('THIAM', 'THIAM'), ('PEC', 'PEC')], max_length=60, null=True)),
                ('SRC_Pass_No', models.CharField(blank=True, max_length=60, null=True)),
                ('IIF_Date', models.DateField(null=True)),
                ('END_Date', models.DateField(null=True)),
            ],
        ),
    ]
