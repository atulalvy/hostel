from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render
import requests, json
from Application.models import Applications
from login.models import VerifiedUser, ApplicationSettings


def test(user):
    if user.Department_portal != "student":
        return True
    return False


# Create your views here.
@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def index(request):
    department = request.user.Department_portal
    accecible = request.user.Accessible
    acceciblelist = accecible.split(",")[:-1]
    return render(request, 'Department/index.html', {"courses": acceciblelist})


# def process_data(request):
#     pass

@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def get_data(request):
    settings = ApplicationSettings.objects.get(pk=1)
    if request.POST['verification_seniors'] == '1':
        years = [2, 3, 4, 5]
    else:
        years = [1]
    models = Applications.objects.all().filter(Department=request.user.Department_portal,
                                               Course_of_study=request.POST['course'], Year_of_Study__in=years)

    sortedmodels = sorted(models, key=lambda x: x.create_priority_value())
    return render(request, 'Department/get_data.html', {'models': sortedmodels})


@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def save_data(request):
    print("views function")
    pin = request.POST['pin']
    std_id = int(request.POST['std_id'])
    reg = request.POST['reg']
    yearback = request.POST['yearback']
    category = request.POST['category']
    models = Applications.objects.get(id=std_id)
    models.Pincode = pin
    models.distance = request.POST['distance']
    if yearback == "true":
        models.year_back = 1
    else:
        models.year_back = 0
    if category == "true":
        models.category_isvalid = 1
    else:
        models.category_isvalid = 0
    models.verified_department = 1
    # print(pin)
    # source = "682022"
    # if (pin == "682022"):
    #     models.distance = 0
    # else:
    #     dest = str(pin)
    #     link = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + source + "&destinations=" + dest + "&key=AIzaSyCE69Rb-G9LtjgZ1EEx2qyN19xpNj67_JI"
    #     print(link)
    #     r = requests.get(link)
    #     y = r.json()
    #     dist = y["rows"][0]["elements"][0]["distance"]["text"]
    #     dist = dist[0:len(dist) - 3]
    #     dist = float(dist)
    #     print(dist)
    #     models.distance = dist
    if (request.POST['yearofstudy'] != ''):
        models.Year_of_Study = request.POST['yearofstudy']
    if (request.POST['gender'] != ''):
        models.Gender = request.POST['gender']
    if (request.POST['prime'] != ''):
        models.Prime_Ministers_program = request.POST['prime']
    if (request.POST['handicapped'] != ''):
        models.Physically_Handicapped = request.POST['handicapped']
    if (request.POST['nativity'] != ''):
        models.Keralite = request.POST['nativity']

    models.save()
    return HttpResponse('Hii')


@login_required(redirect_field_name='/auth/')
@user_passes_test(test, redirect_field_name='/')
def priority(request):
    course = request.POST['course']
    department = request.user.Department_portal
    print(request.POST['verification_seniors'])
    if request.POST['verification_seniors'] == '1':
        years = [2, 3, 4, 5]
    else:
        years = [1]

    models_keralite = Applications.objects.all().filter(Department=department, Course_of_study=course,
                                                        verified_department='1', year_back='0', Keralite='1').filter(
        Year_of_Study__in=years)
    models_nonkeralite = Applications.objects.all().filter(Department=department, Course_of_study=course,
                                                           verified_department='1', year_back='0', Keralite='0').filter(
        Year_of_Study__in=years)
    models_valid_malekeralite = []
    models_valid_malenonkeralite = []
    models_valid_femalekeralite = []
    models_valid_femalenonkeralite = []

    for i in models_keralite:
        if i.distance_valid():
            if i.Gender == 'Male':
                models_valid_malekeralite.append(i)
            else:
                models_valid_femalekeralite.append(i)

    for i in models_nonkeralite:
        if i.distance_valid():
            if i.Gender == 'Male':
                models_valid_malenonkeralite.append(i)
            else:
                models_valid_femalenonkeralite.append(i)

    sortedmodels_malekeralite = sorted(models_valid_malekeralite, key=lambda x: x.create_priority_value(), reverse=True)
    sortedmodels_malenonkeralite = sorted(models_valid_malenonkeralite, key=lambda x: x.create_priority_value(),
                                          reverse=True)
    sortedmodels_femalekeralite = sorted(models_valid_femalekeralite, key=lambda x: x.create_priority_value(),
                                         reverse=True)
    sortedmodels_femalenonkeralite = sorted(models_valid_femalenonkeralite, key=lambda x: x.create_priority_value(),
                                            reverse=True)
    return render(request, 'Department/priority.html',
                  {'m_keralite': sortedmodels_malekeralite, 'f_keralite': sortedmodels_femalekeralite,
                   'm_nonkeralite': sortedmodels_malenonkeralite,
                   'f_nonkeralite': sortedmodels_femalenonkeralite, 'Department': department,
                   'Course': course})
