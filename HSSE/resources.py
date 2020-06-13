from import_export import resources
from HSSE.models import Member
from HSSE.models import Appointment
from HSSE.models import BiCycle_Registration
from HSSE.models import DailyManpower


class MemberResource(resources.ModelResource):
    class Meta:
        model = Member


class AppointmentResource(resources.ModelResource):
    class Meta:
        model = Appointment


class BiCycle_RegistrationResource(resources.ModelResource):
    class Meta:
        model = BiCycle_Registration

        class Short_Service_EmployeeResource(resources.ModelResource):
            class Meta:
                model = Short_Service_Employee


class EmployeeCourseResource(resources.ModelResource):
    class Meta:
        model = EmployeeCourse

        class DailyManpowerResource(resources.ModelResource):
            class Meta:
                model = DailyManpower

                class FRCResource(resources.ModelResource):
                    class Meta:
                        model = FRC

                        class FRCResource(resources.ModelResource):
                            class Meta:
                                model = Monthly_Action

                                class Phone_NumberResource(resources.ModelResource):
                                    class Meta:
                                        model = Phone_Number

                                        class Medical_LeaveResource(resources.ModelResource):
                                            class Meta:
                                                model = Medical_Leave

                                                class In_House_TrainingResource(resources.ModelResource):
                                                    class Meta:
                                                        model = In_House_Training

                                                        class In_House_TrainingResource(resources.ModelResource):
                                                            class Meta:
                                                                model = In_House_Training

                                                        class LG_or_LA_or_LMResource(resources.ModelResource):
                                                            class Meta:
                                                                model = LG_or_LA_or_LM
