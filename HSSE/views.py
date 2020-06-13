from django.shortcuts import render
from .models import *
from HSSE.resources import MemberResource
from django.shortcuts import render, redirect
from django.http import HttpResponse
from HSSE.resources import BiCycle_RegistrationResource
from HSSE.resources import AppointmentResource


# Create your views here.
def download_image(request, image_id):
    cover = ImageModel.objects.get(id=image_id)


FILE_TYPES = ['csv', 'pdf', 'jpeg']


def create_File(request):
    form = Bicycle_Form()
    if request.method == 'POST':
        form = Bycycle_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_File = request.FILES['display_File']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()


def create_File(request):
    form = Bicycle_Form()
    if request.method == 'Get':
        form = Bycycle_Form(request.Get, request.FILES)


default_file_view = ObjectDownloadView.as_view(model=Document)


def export(request):
    member_resource = MemberResource()
    dataset = member_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="member.csv"'
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def export(request):
    Medical_Leave_resource = Medical_LeaveResource()
    dataset = Medical_Leave_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="member.csv"'
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

def export(request):
    LG_or_LA_or_LM_resource = LG_or_LA_or_LMResource()
    dataset = LG_or_LA_or_LM_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="member.csv"'
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response
def export(request):
    BiCycle_Registration_resource = BiCycle_RegistrationResource()
    dataset = BiCycle_Registration_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="member.csv"'
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def export(request):
    Appointment_resource = AppointmentResource()
    dataset = Appointment_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="member.csv"'
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def export(request):
    In_House_Training_resource = In_House_TrainingResource()
    dataset = In_House_Training_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="member.csv"'
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def export(request):
    Short_Service_Employee_resource = Short_Service_EmployeeResource()
    dataset = Short_Service_Employee_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="member.csv"'
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def export(request):
    Document_resource = DocumentResource()
    dataset = Document_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="member.csv"'
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def export(request):
    Short_Service_Employee_resource = Short_Service_EmployeeResource()
    dataset = Short_Service_Employee_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="member.csv"'
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def export(request):
    EmployeeCourse_resource = EmployeeCourseResource()
    dataset = EmployeeCourse_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="member.csv"'
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def export(request):
    Phone_Number_resource = Phone_NumberResource()
    dataset = Phone_Number_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="member.csv"'
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


class DocumentCreate(CreateView):
    model = Document
    fields = ['file']

    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.FILES:
            for f in self.request.FILES.getlist('file'):
                obj = self.model.objects.create(file=f)

    return super(DocumentCreate, self).form_valid(form)


def Form(request):
    return render(request, "index/form.html", {})


def Upload(request):
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open('/Users/benq/djangogirls/upload/media/file_' + str(count), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

        process(x)
    return HttpResponse("File(s) uploaded!")
