from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def display_jspider(request):
    c = input('enter course name : ')
    jo = jspider.objects.create(course_name = c)
    jo.save()



def display(request):

    cn = input('enter course name : ')
    jo = jspider.objects.get(course_name = cn)

    n = input('ennter name :')
    m = input('enter mobile number : ')
    d = input('enter date of joining : ')
    e = input('enter email : ')

    so = student.objects.create(course_name = jo ,name = n , mob = m ,doj =d,email=e)
    so.save()

    qso = student.objects.all()

    d={'qso': qso}

    return render(request,'display.html',d)


def d1(request):
    qso = student.objects.all()

    qso=student.objects.all().order_by('name')
    qso=student.objects.all().order_by('-name')
    qso=student.objects.all().order_by('email')
    qso=student.objects.all().order_by(Length('name'))
    qso=student.objects.all().order_by(Length('name'))
    qso=student.objects.filter(course_name = 'PYTHON').order_by(Length('name'))
    qso=student.objects.all()[2:3]
    qso=student.objects.all().order_by()
    qso=student.objects.filter(name__startswith = 's')
    qso=student.objects.filter(name__endswith = 'z')
    qso=student.objects.filter(name__contains = 's')
    qso=student.objects.filter(mob__gt = '10')
    qso=student.objects.filter(email__endswith = 'com')
    qso=student.objects.all()
    qso=student.objects.filter(Q(name__endswith='y') & Q(email__endswith='com') )
    
    qso = student.objects.all()
    qso = student.objects.filter(Q(name__contains ='y') |  Q(mob__endswith=0))
    qso = student.objects.all()
    qso = student.objects.filter(Q(course_name = 'PYTHON')  & Q(name__contains = 'r'))







    d={'qso': qso}

    return render(request,'d1.html',d)

