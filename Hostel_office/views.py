from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from Application.models import Applications
from Hostel_office.models import Department
from login.forms import UserForm
from login.models import VerifiedUser, ApplicationSettings


def test(user):
    if user.Department_portal == "office":
        return True
    return False


# Create your views here.
@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def index(request):
    departments = [
        "Choose department",
        "DDU Kaushal Kendras (DDUKK)",
        "Department of Applied Chemistry",
        "Department of Applied Economics",
        "Department of Atmospheric Sciences",
        "Department of Biotechnology",
        "Department of Chemical Oceanography",
        "Department of Computer Applications",
        "Department of Computer Science",
        "Department of Electronics",
        "Department of Hindi",
        "Department of Instrumentation",
        "Department of Marine Biology, Microbiology and Biochemistry",
        "Department of Marine Geology and Geophysics",
        "Department of Mathematics",
        "Department of Physical Oceanography",
        "Department of Physics",
        "Department of Polymer Science and Rubber Technology",
        "Department of Ship Technology",
        "Department of Statistics",
        "Inter University Centre for IPR Studies (IUCIPRS)",
        "International School of Photonics",
        "National Centre for Aquatic Animal Health (NCAAH)",
        "School of Engineering",
        "School of Environmental Studies",
        "School of Industrial Fisheries",
        "School of Legal Studies",
        "School of Management Studies"]
    context = {
        "departments": departments,
        "models": Applications.objects.all()
    }
    return render(request, 'Hostel_office/index.html', context)


@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def get_data(request):
    print(request.POST)
    models = Applications.objects.all().filter(Department=request.POST['dept'], Course_of_study=request.POST['course'],
                                               Gender=request.POST['gender'], verified_department='1', year_back='0',
                                               Keralite=request.POST['keralite'])


    sortedmodels = sorted(models, key=lambda x: x.create_priority_value(), reverse=True)
    return render(request, 'Hostel_office/get_data.html', {'models': sortedmodels})


@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def save_data(request):
    select = request.POST['select']
    reg = request.POST['reg']
    ischeck = request.POST['ischeck']
    room = request.POST['room']
    print(ischeck)
    models = Applications.objects.get(Registration_No=reg)
    if ischeck == 'true':
        if select != "":
            models.admitted = 1
            models.Hostel_admitted = select
            models.Room_No = room
    else:
        models.admitted = 0
        models.Hostel_admitted = None
        models.Room_No = 0
    models.save()
    return HttpResponse("hello")

@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def add_departments(request):
    return render(request, 'Hostel_office/create_department.html', {})


@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def add_dept(request):
    departments = [
        "Choose department",
        "DDU Kaushal Kendras (DDUKK)",
        "Department of Applied Chemistry",
        "Department of Applied Economics",
        "Department of Atmospheric Sciences",
        "Department of Biotechnology",
        "Department of Chemical Oceanography",
        "Department of Computer Applications",
        "Department of Computer Science",
        "Department of Electronics",
        "Department of Hindi",
        "Department of Instrumentation",
        "Department of Marine Biology, Microbiology and Biochemistry",
        "Department of Marine Geology and Geophysics",
        "Department of Mathematics",
        "Department of Physical Oceanography",
        "Department of Physics",
        "Department of Polymer Science and Rubber Technology",
        "Department of Ship Technology",
        "Department of Statistics",
        "Inter University Centre for IPR Studies (IUCIPRS)",
        "International School of Photonics",
        "National Centre for Aquatic Animal Health (NCAAH)",
        "School of Engineering",
        "School of Environmental Studies",
        "School of Industrial Fisheries",
        "School of Legal Studies",
        "School of Management Studies"]
    context = {
        "departments": departments,
        "models": Applications.objects.all()
    }
    return render(request, 'Hostel_office/add_data.html', context)


@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def create(request):
    # departments = [
    #     "Choose department",
    #     "DDU Kaushal Kendras (DDUKK)",
    #     "Department of Applied Chemistry",
    #     "Department of Applied Economics",
    #     "Department of Atmospheric Sciences",
    #     "Department of Biotechnology",
    #     "Department of Chemical Oceanography",
    #     "Department of Computer Applications",
    #     "Department of Computer Science",
    #     "Department of Electronics",
    #     "Department of Hindi",
    #     "Department of Instrumentation",
    #     "Department of Marine Biology, Microbiology and Biochemistry",
    #     "Department of Marine Geology and Geophysics",
    #     "Department of Mathematics",
    #     "Department of Physical Oceanography",
    #     "Department of Physics",
    #     "Department of Polymer Science and Rubber Technology",
    #     "Department of Ship Technology",
    #     "Department of Statistics",
    #     "Inter University Centre for IPR Studies (IUCIPRS)",
    #     "International School of Photonics",
    #     "National Centre for Aquatic Animal Health (NCAAH)",
    #     "School of Engineering",
    #     "School of Environmental Studies",
    #     "School of Industrial Fisheries",
    #     "School of Legal Studies",
    #     "School of Management Studies"]
    # context = {
    #     "departments": departments,
    #     "models": Applications.objects.all(),
    # }
    if request.method == 'POST':
        dupli_user = VerifiedUser.objects.filter(username=request.POST['username'])
        print(dupli_user)
        if (not dupli_user):
            Dept_user = VerifiedUser.objects.create_user(username=request.POST['username'],
                                                         password=request.POST['password1'])
            Dept_user.is_active = True
            Dept_user.Department_portal = request.POST['dept']
            Dept_user.Accessible = request.POST['course']
            Dept_user.save()
            return HttpResponseRedirect('/office/add_dept/')
        else:
            return HttpResponse('Duplicate User Found,Try other Name')
    else:
        return HttpResponseRedirect('/office/add_dept/')

@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def printdata(request):
    print(request.POST['regno'])
    models = Applications.objects.get(Registration_No=request.POST['regno'])
    return render(request, 'Hostel_office/printuser.html', {'models': models})


@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def control(request):
    settings = ApplicationSettings.objects.get(pk=1)
    if request.method=="POST":
        if "firstyear" in request.POST:
            settings.first_years = not settings.first_years
            settings.save()

        if "close" in request.POST:
            settings.active_applications = not settings.active_applications
            settings.save()

        if "show_allot" in request.POST:
            settings.show_allotment = not settings.show_allotment
            settings.save()

    return render(request,"Hostel_office/control setting.html",{"setting":settings})

#Code
@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def get_departments(request):
    courses = Department.objects.all().values()
    print(courses)
    print ("courses")
    return JsonResponse(list(courses) , safe=False)

@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def create_department(request):
    if request.method == 'POST':
        dupli_dept = Department.objects.filter(Department=request.POST.get('dept', 'default'))
        print(dupli_dept)
        print("here")

        if not dupli_dept:
            Dept = Department()
            Dept.Department = request.POST.get('dept', 'default')
            Dept.Course = request.POST.get('course', 'default')
            Dept.save()
            return HttpResponseRedirect('/office/create_department/')
        else:
            return HttpResponse('Duplicate User Found,Try other Name')
    else:
        return HttpResponseRedirect('/office/create_department/')

@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def delete_department(request):
    return render(request, "Hostel_office/delete_department.html")

@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def delete(request):
    if request.method == 'POST':
        dept = Department.objects.filter(Department=request.POST.get('dept', 'default'))
        if dept:
            dept.delete()
            return HttpResponseRedirect('/office/delete_dept/')
        else:
            return HttpResponse('No such Department Found,Try other Name')
    else:
        return HttpResponseRedirect('/office/delete_dept/')