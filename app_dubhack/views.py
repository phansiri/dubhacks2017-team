# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# from app_dubhack.models import RequiredCourses


def grabClientData(request):
    requireds = RequiredCourses.objects.all()
    user = UserData.objects.all()
    userList = []
    for row in user:
        userList.append(row.imputShortNumber)

    result = []

    for re in requireds:
        if re.requiredCourseNumber in userList:
            print("not needed")
        else:
            result.append(re)
            print(re)

    winterCourses = Course.objects.all()
    classes = Class.objects.all()
    courseSchedule = Courseschedule.objects.all()

    classes14 = classes.filter(coursescheduleid=12)
    classes15 = classes.filter(coursescheduleid=10)


    result14 = []
    result15 = []

    # for me in classes14:
    #     if me.courseid.departmentid.departmentshortname == 'CSE':
    #         if me.courseid.coursenumber in result:
    #             result14.append(me)

    # for fe in classes15:
    #     if fe.courseid.coursenumber in result:
    #         result15.append(me)


    context = {
        'results': result,
        'winter': winterCourses,
        # 'qtr': quarters,
        'coursesS': courseSchedule,
        '14results': result14,
        # '15results': result15,
        '14classes': classes14,

    }
    return render(request, 'app_dubhack/grabClientData.html', context)


@login_required
def home(request):
    quarters = Quarter.objects.all()
    context = {
        "objs": quarters
    }
    return render(request, 'app_dubhack/home.html', context)

@login_required
def input_classes_new(request):
    if request.method == "POST":
        form = UserDataForm(request.POST)
        if form.is_valid():
            insertData = form.save(commit=False)
            insertData.userID = request.user
            insertData.save()
            return redirect('input_classes_new')
    else:
        form = UserDataForm()

    context = {
        'form': form
    }
    return render(request, 'app_dubhack/input_classes_new.html', context)
