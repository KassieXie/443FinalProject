from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
from django.db import connection 
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

class About(LoginRequiredMixin, TemplateView):
    template_name = 'hello/about.html'

def login(request):
    pass

@login_required
def home(request):
    context = {'name':'Andy', 'age':'40'}
    return render(request, 'hello/hello.html', context)

@login_required
def about(request):
    return render(request, 'hello/details.html')


def dictfetchall(cursor):
	columns = [col[0] for col in cursor.description]
	return[ dict(zip(columns,row)) for row in cursor.fetchall()]

@login_required
def studentdetails(request):
    students = Students.objects.all()
#    paginator = Paginator(student_list, 1)
#    page = request.GET.get('page')
#    try:
#        students = paginator.get_page(page)
#    except PageNotAnInteger:
#        students = paginator.get_page(1)
#    except EmptyPage:
#        students = paginator.get_page(1)
#    except:
#        students = paginator.get_page(1)

#    cursor = connection.cursor()
#    cursor.execute("SELECT * FROM HELLO_STUDENTS")
#    student_list = dictfetchall(cursor)
    return render(request, 'hello/details.html', {'students':students})


class Studentdetails(LoginRequiredMixin, ListView):
    template_name = 'hello/student.html'
    queryset = Students.objects.all()
    context_object_name = 'students'
    paginate_by = 3


def studentinfo(request):
    cursor = connection.cursor()
    if 'student' not in request.session:
        cursor.execute("SELECT LASTNAME FROM HELLO_STUDENTS LIMIT 1")
        name = cursor.fetchone()
        request.session['student'] = name[0]
    if('student' in request.GET):
        request.session['student'] = request.GET.get('student')
    cursor.execute("SELECT * FROM HELLO_STUDENTS WHERE LASTNAME = %s",[request.session['student']])
    info = dictfetchall(cursor)
    students = Students.objects.all()
    return render(request, 'hello/studentinfo.html', {'info':info, 'students':students})




# Create your views here.
