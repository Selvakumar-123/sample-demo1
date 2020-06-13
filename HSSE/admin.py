from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from HSSE.models import Member
from HSSE.models import BiCycle_Registration
from HSSE.models import Appointment
from HSSE.models import Short_Service_Employee
from HSSE.models import EmployeeCourse
from HSSE.models import DailyManpower


# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(ImportExportModelAdmin):
    list_display = ("EmployeeID", "EmployeeName", "Designation",
                    "Group", "Type_of_LOA",
                    "File_No",)
    list_filter = ("EmployeeID", "EmployeeName", "Designation",
                   "Group", "Type_of_LOA",
                   "File_No",)
    search_fields = ("EmployeeID", "EmployeeName", "Designation",
                     "Group", "Type_of_LOA",
                     "File_No",)
    list_per_page = 50


# Register your models here.
@admin.register(Short_Service_Employee)
class Short_Service_EmployeeAdmin(ImportExportModelAdmin):
    list_display = ("EmployeeID", "EmployeeName", "Designation", "Group",
                    "SRC_Pass_No", "IIF_Date", "END_Date"
                    )
    list_filter = ("EmployeeID", "EmployeeName", "Designation", "Group",
                   "SRC_Pass_No", "IIF_Date", "END_Date"
                   )
    search_fields = ("EmployeeID", "EmployeeName", "Designation", "Group",
                     "SRC_Pass_No", "IIF_Date", "END_Date"
                     )
    list_per_page = 50


@admin.register(EmployeeCourse)
class EmployeeCourseAdmin(ImportExportModelAdmin):
    list_display = ("EmployeeID", "EmployeeName", "Designation", "Group", "SRC_Pass_No", "IIFDate", "Work_Permit_Date",
                    "Permit_Applicant_Date",
                    "Work_at_Height_Date", "Confined_Space_Date", "Process_Plant_Date", "Work_at_Height_Date",
                    "Confined_Space_Date", "Process_Plant_Date", "BA_Date", 'Rigger_and_Signalman_Date',
                    "ForkLift_Date", "Boom_Lift_Date",
                    "Over_Head_Crane_Date", "Scaffold_Erection_Date", "Chemical_Handlers_Date",
                    "Bi_Safe_Level_Date", 'Gotcha_Kit_Date', "First_Aid_Date")
    list_filter = ("EmployeeID", "EmployeeName", "Designation", "Group", "SRC_Pass_No", "IIFDate", "Work_Permit_Date",
                   "Permit_Applicant_Date",
                   "Work_at_Height_Date", "Confined_Space_Date", "Process_Plant_Date", "Work_at_Height_Date",
                   "Confined_Space_Date", "Process_Plant_Date", "BA_Date", 'Rigger_and_Signalman_Date',
                   "ForkLift_Date", "Boom_Lift_Date",
                   "Over_Head_Crane_Date", "Scaffold_Erection_Date", "Chemical_Handlers_Date",
                   "Bi_Safe_Level_Date", 'Gotcha_Kit_Date', "First_Aid_Date")
    search_fields = ("EmployeeID", "EmployeeName", "Designation", "Group", "SRC_Pass_No", "IIFDate", "Work_Permit_Date",
                     "Permit_Applicant_Date",
                     "Work_at_Height_Date", "Confined_Space_Date", "Process_Plant_Date", "Work_at_Height_Date",
                     "Confined_Space_Date", "Process_Plant_Date", "BA_Date", 'Rigger_and_Signalman_Date',
                     "ForkLift_Date", "Boom_Lift_Date",
                     "Over_Head_Crane_Date", "Scaffold_Erection_Date", "Chemical_Handlers_Date",
                     "Bi_Safe_Level_Date", 'Gotcha_Kit_Date', "First_Aid_Date")
    list_per_page = 50


# Register your models here.


@admin.register(DailyManpower)
class DailyManpowerAdmin(ImportExportModelAdmin):
    list_display = ("Date", "ALFA", "HAB", "THIAM", "PEC", "PGS_SCAFFOLD",
                    "PGS_INSULATION", "PEI", "PSE", "EBT", "AD_METH",)
    list_filter = ("Date", "ALFA", "HAB", "THIAM", "PEC", "PGS_SCAFFOLD",)
    search_fields = ("Date", "ALFA", "HAB", "THIAM", "PEC", "PGS_SCAFFOLD",)
    list_per_page = 50


@admin.register(FRC)
class FRCAdmin(ImportExportModelAdmin):
    list_display = ("EmployeeID", "EmployeeName", "Designation", "Group", "ShirtSize", "QTY0",
                    "PantSize", "QTY1", "BootSize", "QTY2", "Helmet", "QTY3", "PR", "issued_Date",)

    list_filter = ("EmployeeID", "EmployeeName", "Designation", "Group", "ShirtSize", "QTY0",
                   "PantSize", "QTY1", "BootSize", "QTY2", "Helmet", "QTY3", "PR", "issued_Date",)

    search_fields = ("EmployeeID", "EmployeeName", "Designation", "Group", "ShirtSize", "QTY0",
                     "PantSize", "QTY1", "BootSize", "QTY2", "Helmet", "QTY3", "PR", "issued_Date",)

    list_per_page = 50


@admin.register(Monthly_Action)
class Monthly_ActionAdmin(ImportExportModelAdmin):
    list_display = ("ActionDate", "Action",)

    list_filter = ("ActionDate", "Action",)

    search_fields = ("ActionDate", "Action",)

    list_per_page = 50


@admin.register(In_House_Training)
class In_House_TrainingAdmin(ImportExportModelAdmin):
    list_display = ("EmployeeID", "EmployeeName", "Designation",
                    "Group", "Training", "File", "File_No", "AttendDate")
    list_filter = ("EmployeeID", "EmployeeName", "Designation",
                   "Group", "File", "File_No", "AttendDate")
    search_fields = ("EmployeeID", "EmployeeName", "Designation",
                     "Group", "File", "File_No", "AttendDate")
    list_per_page = 50


@admin.register(Medical_Leave)
class Medical_LeaveAdmin(ImportExportModelAdmin):
    list_display = ("EmployeeID", "EmployeeName", "Designation",
                    "Group", "Type", "Remark", "GivenDate")
    list_filter = ("EmployeeID", "EmployeeName", "Designation",
                   "Group", "Type", "Remark", "GivenDate")
    search_fields = ("EmployeeID", "EmployeeName", "Designation",
                     "Group", "Type", "Remark", "GivenDate")
    list_per_page = 50


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    list_display = ("firstname", "lastname", "email", "birth_date")
    pass


@admin.register(BiCycle_Registration)
class BiCycle_RegistrationAdmin(ImportExportModelAdmin):
    list_display = ("EmployeeID1", "EmployeeID2", "EmployeeName1", "EmployeeName2", "Designation1", "Designation2",
                    "Group", "BiCycle_No", "File")
    list_filter = ("EmployeeID1", "EmployeeID2", "EmployeeName1", "EmployeeName2", "Designation1", "Designation2",
                   "Group", "BiCycle_No", "File")
    search_fields = ("EmployeeID1", "EmployeeID2", "EmployeeName1", "EmployeeName2", "Designation1", "Designation2",
                     "Group", "BiCycle_No", "File")
    list_per_page = 50
    pass


@admin.register(Phone_Number)
class Phone_NumberAdmin(ImportExportModelAdmin):
    list_display = ("EmployeeID", "EmployeeName", "Designation",
                    "Group", "Type1", "Type2")
    list_filter = ("EmployeeID", "EmployeeName", "Designation",
                   "Group", "Type1", "Type2")
    search_fields = ("EmployeeID", "EmployeeName", "Designation",
                     "Group", "Type1", "Type2")
    list_per_page = 50


@admin.register(Document)
class DocumentAdmin(ImportExportModelAdmin):
    list_display = ("Name", "file",)
    list_filter = ("Name", "file",)
    search_fields = ("Name", "file",)
    list_per_page = 50


@admin.register(LG_or_LA_or_LM)
class LG_or_LA_orLMAdmin(ImportExportModelAdmin):
    list_display = ("Type", "ID_No", "Weight_or_Length", "Group", "File_No", "Date_of_inspection", "Date_of_expiry",)
    list_filter = ("Type", "ID_No", "Weight_or_Length", "Group", "File_No", "Date_of_inspection", "Date_of_expiry",)
    search_fields = ("Type", "ID_No", "Weight_or_Length", "Group", "File_No", "Date_of_inspection", "Date_of_expiry",)
    list_per_page = 50
