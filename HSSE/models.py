from django.db import models


class Appointment(models.Model):
    Designation = [
        ('Manager', 'Manager'),
        ('Supervisor', 'Supervisor'),
        ('HSSE_Leader', 'HSSE_Leader'),
        ('Admin', 'Admin'),
        ('Pipe_Fitter', 'Pipe_Fitter'),
        ('Welder', 'Welder'),
        ('General_Fitter', 'General_Fitter'),

    ]
    LOA = (
        ('Boom Lift Operator', 'Boom Lift Operator'),
        ('Confined Space Authorized Manager', 'Confined Space Authorized Manager'),
        ('Confined Space Safety Assessor', 'Confined Space Safety Assessor'),
        ('Confined Space Watchman', 'Confined Space Watchman'),
        ('Coordinator of Health, Safety, Security & Environment (HSSE)',
         'Coordinator of Health, Safety, Security & Environment (HSSE)'),
        ('Crane Operator', 'Crane Operator'),
        ('Driver ', 'Driver '),
        ('Hazardous Substance and Chemical Controller', 'Hazardous Substance and Chemical Controller'),
        ('Forklift Truck Operator', 'Forklift Truck Operator'),
        (' Lifting Supervisor', ' Lifting Supervisor'),
        (' Occupational First Aide', ' Occupational First Aide'),
        ('Overhead Crane Operator', 'Overhead Crane Operator'),
        ('PTW Authorized Applicant', 'PTW Authorized Applicant'),
        ('Rigger', 'Rigger'),
        ('FireWatchman', 'FireWatchman'),

    )
    Group = (
        ('ALFA', 'ALFA'),
        ('HAB', 'HAB'),
        ('THIAM', 'THIAM'),
        ('PEC', 'PEC'),

    )

    EmployeeID = models.CharField(max_length=60, null=True, blank=False)
    EmployeeName = models.CharField(max_length=60, null=True, blank=False)
    Designation = models.CharField(max_length=60, null=True, blank=False, choices=Designation)
    Group = models.CharField(max_length=60, null=True, blank=False, choices=Group)
    Type_of_LOA = models.CharField(max_length=60, null=True, blank=False, choices=LOA)
    File_No = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.EmployeeID


class DailyManpower(models.Model):
    Date = models.DateField(null=True, blank=False)
    ALFA = models.CharField(max_length=60, null=True, blank=True)
    HAB = models.CharField(max_length=60, null=True, blank=True)
    THIAM = models.CharField(max_length=60, null=True, blank=True)
    PEC = models.CharField(max_length=60, null=True, blank=True)
    PGS_SCAFFOLD = models.CharField(max_length=60, null=True, blank=True)
    PGS_INSULATION = models.CharField(max_length=60, null=True, blank=True)
    PEI = models.CharField(max_length=60, null=True, blank=True)
    PSE = models.CharField(max_length=60, null=True, blank=True)
    EBT = models.CharField(max_length=60, null=True, blank=True)
    AD_METH = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.Date


class Short_Service_Employee(models.Model):
    Designation = (
        ('Manager', 'Manager'),
        ('Supervisor', 'Supervisor'),
        ('HSSE_Leader', 'HSSE_Leader'),
        ('Pipe_Fitter', 'Pipe_Fitter'),
        ('Welder', 'Welder'),
        ('General_Fitter', 'General_Fitter'),

    )
    Group = (
        ('ALFA', 'ALFA'),
        ('HAB', 'HAB'),
        ('THIAM', 'THIAM'),
        ('PEC', 'PEC'),
    )

    EmployeeID = models.CharField(max_length=60, primary_key=True, null=False, blank=False)
    EmployeeName = models.CharField(max_length=60, null=True, blank=False)
    Designation = models.CharField(max_length=60, null=True, blank=False, choices=Designation)
    Group = models.CharField(max_length=60, null=True, blank=False, choices=Group)
    SRC_Pass_No = models.CharField(max_length=60, null=True, blank=True)
    IIF_Date = models.DateField(null=True)
    END_Date = models.DateField(null=True)

    def __str__(self):
        return self.EmployeeID


class EmployeeCourse(models.Model):
    Designation = (
        ('Manager', 'Manager'),
        ('Supervisor', 'Supervisor'),
        ('HSSE_Leader', 'HSSE_Leader'),
        ('Pipe_Fitter', 'Pipe_Fitter'),
        ('Welder', 'Welder'),
        ('General_Fitter', 'General_Fitter'),

    )
    Group = (
        ('ALFA', 'ALFA'),
        ('HAB', 'HAB'),
        ('THIAM', 'THIAM'),
        ('PEC', 'PEC'),
    )

    EmployeeID = models.CharField(max_length=60, primary_key=True, null=False, blank=False, unique=True)
    EmployeeName = models.CharField(max_length=60, null=True, blank=False)
    Designation = models.CharField(max_length=60, null=True, blank=False, choices=Designation)
    Group = models.CharField(max_length=60, null=True, blank=False, choices=Group)
    SRC_Pass_No = models.CharField(max_length=60, null=True, blank=True, )
    IIFDate = models.DateField(null=True, blank=True)
    Work_Permit_Date = models.DateField(null=True, blank=True)
    Permit_Applicant_Date = models.DateField(null=True, blank=True)
    Work_at_Height_Date = models.DateField(null=True, blank=True, help_text='Supervisor_Course_only',
                                           verbose_name='Supervisor_Course_only')
    Confined_Space_Date = models.DateField(null=True, blank=True, help_text='Supervisor_Course_only',
                                           verbose_name='Supervisor_Course_only', )
    Process_Plant_Date = models.DateField(null=True, blank=True, help_text='Supervisor_Course_only',
                                          verbose_name='Supervisor_Course_only')
    Work_at_Height_Date = models.DateField(null=True, blank=True)
    Confined_Space_Date = models.DateField(null=True, blank=True)
    Process_Plant_Date = models.DateField(null=True, blank=True)
    BA_Date = models.DateField(null=True, blank=True)
    Rigger_and_Signalman_Date = models.DateField(null=True, blank=True)
    ForkLift_Date = models.DateField(null=True, blank=True)
    Boom_Lift_Date = models.DateField(null=True, blank=True)
    Over_Head_Crane_Date = models.DateField(null=True, blank=True)
    Scaffold_Erection_Date = models.DateField(null=True, blank=True)
    Chemical_Handlers_Date = models.DateField(null=True, blank=True)
    Bi_Safe_Level_Date = models.DateField(null=True, blank=True)
    Gotcha_Kit_Date = models.DateField(null=True, blank=True)
    First_Aid_Date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.EmployeeID


class FRC(models.Model):
    ShirtSize = (
        ('s', 's'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
        ('Nomex', 'Nomex'),
    )
    PantSize = (
        ('28', '28'),
        ('30', '30'),
        ('32', '32'),
        ('34', '34'),
        ('36', '36'),
        ('38', '38'),
        ('Nomex', 'Nomex'),
    )
    BootSize = (
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),

    )
    QTY0 = (
        ('1', '1'),
        ('2', '2'),
    )
    QTY1 = (
        ('1', '1'),
        ('2', '2'),
    )
    QTY2 = (
        ('1', '1'),
        ('2', '2'),
    )
    QTY3 = (
        ('1', '1'),
        ('2', '2'),
    )
    Helmet = (
        ('Yellow', 'Yellow'),
        ('Red', 'Red'),
        ('White', 'White'),
        ('Blue', 'Blue'),

    )

    Designation = (
        ('Manager', 'Manager'),
        ('Supervisor', 'Supervisor'),
        ('HSSE_Leader', 'HSSE_Leader'),
        ('Admin', 'Admin'),
        ('Pipe_Fitter', 'Pipe_Fitter'),
        ('Welder', 'Welder'),
        ('General_Fitter', 'General_Fitter'),

    )
    Group = (
        ('ALFA', 'ALFA'),
        ('HAB', 'HAB'),
        ('THIAM', 'THIAM'),
        ('PEC', 'PEC'),
    )

    EmployeeID = models.CharField(max_length=60, null=True, blank=False)
    EmployeeName = models.CharField(max_length=60, null=True, blank=False)
    Designation = models.CharField(max_length=60, null=True, blank=False, choices=Designation)
    Group = models.CharField(max_length=60, null=True, blank=False, choices=Group)

    ShirtSize = models.CharField(max_length=60, blank=True, choices=ShirtSize)
    QTY0 = models.CharField(max_length=60, blank=True, choices=QTY0)

    PantSize = models.CharField(max_length=60, blank=True, choices=PantSize)
    QTY1 = models.CharField(max_length=60, blank=True, choices=QTY1)
    BootSize = models.CharField(max_length=60, blank=True, choices=BootSize)
    QTY2 = models.CharField(max_length=60, blank=True, choices=QTY2)
    Helmet = models.CharField(max_length=60, blank=True, choices=Helmet)
    QTY3 = models.CharField(max_length=60, blank=True, choices=QTY3)
    PR = models.CharField(max_length=60, blank=False)
    issued_Date = models.DateField(null=True)

    def __str__(self):
        return self.EmployeeID


class Monthly_Action(models.Model):
    ActionDate = models.DateField(null=True)

    Action = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self):
        return self.Action


class BiCycle_Registration(models.Model):
    Designation = (
        ('Manager', 'Manager'),
        ('Supervisor', 'Supervisor'),
        ('HSSE_Leader', 'HSSE_Leader'),
        ('Admin', 'Admin'),
        ('Pipe_Fitter', 'Pipe_Fitter'),
        ('Welder', 'Welder'),
        ('General_Fitter', 'General_Fitter'),

    )
    Group = (
        ('ALFA', 'ALFA'),
        ('HAB', 'HAB'),
        ('THIAM', 'THIAM'),
        ('PEC', 'PEC'),
    )

    EmployeeID1 = models.CharField(max_length=60, null=True, blank=False)
    EmployeeID2 = models.CharField(max_length=60, null=True, blank=False)
    EmployeeName1 = models.CharField(max_length=60, null=True, blank=False)
    EmployeeName2 = models.CharField(max_length=60, null=True, blank=False)
    Designation1 = models.CharField(max_length=60, null=True, blank=False, choices=Designation)
    Designation2 = models.CharField(max_length=60, null=True, blank=False, choices=Designation)
    Group = models.CharField(max_length=60, null=True, blank=False, choices=Group)
    BiCycle_No = models.CharField(max_length=60, null=True, blank=False)
    File = models.FileField(null=True, blank=False)

    def __str__(self):
        return self.Group


class In_House_Training(models.Model):
    Designation = (
        ('Manager', 'Manager'),
        ('Supervisor', 'Supervisor'),
        ('HSSE_Leader', 'HSSE_Leader'),
        ('Admin', 'Admin'),
        ('Pipe_Fitter', 'Pipe_Fitter'),
        ('Welder', 'Welder'),
        ('General_Fitter', 'General_Fitter'),

    )
    Group = (
        ('ALFA', 'ALFA'),
        ('HAB', 'HAB'),
        ('THIAM', 'THIAM'),
        ('PEC', 'PEC'),
    )
    Training = (
        ('Fire_Watchman', 'Fire_Watchman'),
        ('confined_space', 'confined_space'),
        ('cut_line_Tape', 'cut_line_Tape'),
        ('Rigger&Signalman', 'Rigger&Signalman'),
        ('Pipe_Fitter', 'Pipe_Fitter'),
        ('Welder', 'Welder'),
        ('General_Fitter', 'General_Fitter'),
        ('BA', 'Rigger&Signalman'),
        ('Turn_Around_Awareness', 'Turn_Around_Awareness'),
        ('Banksman', 'Banksman'),
        ('Respirator_Fit_Test', 'Respirator_Fit_Test'),
        ('Hearing_Test', 'Hearing_Test'),
        ('NID', 'NID'),
    )

    EmployeeID = models.CharField(max_length=60, null=True, blank=False)

    EmployeeName = models.CharField(max_length=60, null=True, blank=False)

    Designation = models.CharField(max_length=60, null=True, blank=False, choices=Designation)

    Group = models.CharField(max_length=60, null=True, blank=False, choices=Group)
    Training = models.CharField(max_length=60, null=True, blank=False, choices=Training)
    File = models.FileField(null=True, blank=True, )
    File_No = models.CharField(max_length=60, null=True, blank=False)

    AttendDate = models.DateField(null=True)

    def __str__(self):
        return self.EmployeeID


class Member(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.firstname


class Medical_Leave(models.Model):
    Designation = (
        ('Manager', 'Manager'),
        ('Supervisor', 'Supervisor'),
        ('HSSE_Leader', 'HSSE_Leader'),
        ('Admin', 'Admin'),
        ('Pipe_Fitter', 'Pipe_Fitter'),
        ('Welder', 'Welder'),
        ('General_Fitter', 'General_Fitter'),

    )
    Group = (
        ('ALFA', 'ALFA'),
        ('HAB', 'HAB'),
        ('THIAM', 'THIAM'),
        ('PEC', 'PEC'),
    )
    Type = (
        ('Work_Related', 'Work_Related'),
        ('Non_Work_Related', 'Non_Work_Related'),

    )

    EmployeeID = models.CharField(max_length=60, null=True, blank=False)

    EmployeeName = models.CharField(max_length=60, null=True, blank=False)

    Designation = models.CharField(max_length=60, null=True, blank=False, choices=Designation)
    Group = models.CharField(max_length=60, null=True, blank=False, choices=Group)
    Type = models.CharField(max_length=60, null=True, blank=False, choices=Type)
    Remark = models.CharField(max_length=60, null=True, blank=True)
    GivenDate = models.DateField()

    def __str__(self):
        return self.EmployeeID


class Phone_Number(models.Model):
    Designation = (
        ('Manager', 'Manager'),
        ('Supervisor', 'Supervisor'),
        ('HSSE_Leader', 'HSSE_Leader'),
        ('Admin', 'Admin'),
        ('Pipe_Fitter', 'Pipe_Fitter'),
        ('Welder', 'Welder'),
        ('General_Fitter', 'General_Fitter'),

    )

    Group = (
        ('ALFA', 'ALFA'),
        ('HAB', 'HAB'),
        ('THIAM', 'THIAM'),
        ('PEC', 'PEC'),
    )

    Type1 = (
        ('Grid', 'Grid'),
        ('Cellular', 'Cellular'),

    )

    Type2 = (
        ('Grid', 'Grid'),
        ('Cellular', 'Cellular'),
    )

    EmployeeID = models.CharField(max_length=60, primary_key=True, null=False, blank=False)
    EmployeeName = models.CharField(max_length=60, null=True, blank=False)
    Designation = models.CharField(max_length=60, null=True, blank=False, choices=Designation)
    Group = models.CharField(max_length=60, null=True, blank=False, choices=Group)
    Type1 = models.IntegerField(null=True, blank=True, choices=Type1)
    Type2 = models.IntegerField(null=True, blank=True, choices=Type2)

    def __str__(self):
        return self.EmployeeID


class Document(models.Model):
    Name = models.CharField(max_length=60, null=True, blank=False)
    file = models.FileField('Document', upload_to='media/')

    @property
    def filename(self):
        name = self.file.name.split("/")[1].replace('_', ' ').replace('-', ' ')
        return name

    def get_absolute_url(self):
        return reverse('HSSE:document-detail', kwargs={'pk': self.pk})


class LG_or_LA_or_LM(models.Model):
    Group = (
        ('ALFA', 'ALFA'),
        ('HAB', 'HAB'),
        ('THIAM', 'THIAM'),
        ('PEC', 'PEC'),
    )
    Type = (
        ('Lifting_Gear', 'Lifting_Gear'),
        ('Lifting_Mechine', 'Lifting_Mechine'),
        ('Lifting_Appliance', 'Lifting_Appliance'),

    )
    Type = models.CharField(max_length=60, null=True, blank=False, choices=Type)
    ID_No = models.CharField(max_length=60, primary_key=True, null=False, blank=False)
    Weight_or_Length = models.CharField(max_length=60, null=True, blank=False)
    Group = models.CharField(max_length=60, null=True, blank=False, choices=Group)
    File_No = models.CharField(max_length=60, null=True, blank=True)
    Date_of_inspection = models.DateField()
    Date_of_expiry = models.DateField()

    def __str__(self):
        return self.Type
