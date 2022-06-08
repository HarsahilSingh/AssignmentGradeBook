
from msilib.schema import ListView

import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.files.storage import FileSystemStorage

from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


from Gradebook.forms import addCourseForm, updateCourseForm, addSemesterForm, updateSemesterForm, addLecturerForm, \
    updateLecturerForm, updateClassesForm, addClassesForm, addStudentsForm, updateStudentsForm, assignLecturerForm, \
    studentEnrolmentForm
from Gradebook.models import Course, Semester, Lecturer, Class, Student, StudentEnrollment


# def index(request):
#   context = {"title": "my tittle", "content": "my content"}
#  return render(request, "index.html", context)


# Home Page
class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Home - GradeBook'
        return context


# For Courses
class listCourse(ListView):
    model = Course
    template_name = 'Courses/list_courses.html'


class createCourse(CreateView):
    model = Course
    form_class = addCourseForm
    template_name = "Courses/create_courses.html"


class updateCourse(UpdateView):
    model = Course
    form_class = updateCourseForm
    template_name = "Courses/update_courses.html "


class deleteCourse(DeleteView):
    model = Course
    template_name = 'Courses/delete_course.html'
    success_url = reverse_lazy('list_course')


# For Semesters

class listSemester(ListView):
    model = Semester
    template_name = 'Semester/list_semesters.html'


class createSemester(CreateView):
    model = Semester
    form_class = addSemesterForm
    template_name = "Semester/create_semesters.html"


class updateSemester(UpdateView):
    model = Semester
    form_class = updateSemesterForm
    template_name = "Semester/update_semesters.html "


class deleteSemester(DeleteView):
    model = Semester
    template_name = 'Semester/delete_semester.html'
    success_url = reverse_lazy('list_semester')


# For Lecturer

class listLecturer(ListView):
    model = Lecturer
    template_name = 'Lecturer/list_lecturer.html'



@login_required
def create_lecturer(request):
    staffID = request.POST.get('staffID')
    first_Name = request.POST.get('first_Name')
    last_Name = request.POST.get('last_Name')
    email = request.POST.get('email')
    course = request.POST.get('course')
    dateOfBirth= request.POST.get('dateOfBirth')

    message = ''
    try:
        user = User.objects.create_user(username=first_Name.lower)
        user.set_password(first_Name.lower())
        user.first_name = first_Name
        user.last_name = last_Name
        user.email = email
        lecturer_group = Group.objects.get(name='Lecturer')
        user.groups.add(lecturer_group)
        user.save()
        lecturer = Lecturer(user=user, course=course, staffID=staffID, first_Name=first_Name, last_Name=last_Name,
                            email=email,
                            dateOfBirth=dateOfBirth)
        lecturer.save()
        message = 'Lecturer ' + first_Name + ' ' + last_Name + ' created!'
    except Exception as e:

        message = 'Lecturer creation failed!' + str(e)

    context = {'message': message}
    return render(request, 'Lecturer/create_lecturer.html', context)

@login_required
def create_lecturer_form(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'Lecturer/create_lecturer_form.html', context)



class updateLecturer(UpdateView):
    model = Lecturer
    form_class = updateLecturerForm
    template_name = "Lecturer/update_lecturer.html "


class deleteLecturer(DeleteView):
    model = Lecturer
    template_name = 'Lecturer/delete_lecturer.html'
    success_url = reverse_lazy('list_lecturer')


# For Classes
class listClasses(ListView):
    model = Class
    template_name = 'Classes/list_classes.html'


class createClasses(CreateView):
    model = Class
    form_class = addClassesForm
    template_name = "Classes/create_classes.html"


class updateClasses(UpdateView):
    model = Class
    form_class = updateClassesForm
    template_name = "Classes/update_classes.html "


class deleteClasses(DeleteView):
    model = Class
    template_name = 'Classes/delete_classes.html'
    success_url = reverse_lazy('list_classes')

class assignLecturer(UpdateView):
    model = Class
    form_class = assignLecturerForm
    template_name = 'Classes/assign_lecturer.html'


# For Students
class listStudents(ListView):
        model = Student
        template_name = 'Students/list_students.html'


@login_required
def create_student(request):
    studentID = request.POST.get('studentID')
    first_Name = request.POST.get('first_Name')
    last_Name = request.POST.get('last_Name')
    email = request.POST.get('email')
    dateOfBirth = request.POST.get('dateOfBirth')

    message = ''
    try:
        user = User.objects.create_user(username=first_Name.lower())
        user.set_password(first_Name.lower())
        user.first_name = first_Name
        user.last_name = last_Name
        user.email = email
        student_group = Group.objects.get(name='Student')
        user.groups.add(student_group)
        user.save()
        student = Student(user=user, studentID=studentID, first_Name=first_Name, last_Name=last_Name, email=email,
                          dateOfBirth=dateOfBirth)
        student.save()
        message = 'Student ' + first_Name + ' ' + last_Name + ' created!'
    except Exception as e :

        message = 'Student creation failed!' + str(e) + first_Name.lower()

    context = {'message': message}
    return render(request, 'Students/create_students.html', context)


@login_required
def create_student_form(request):
    return render(request, 'Students/create_student_form.html', None)



class updateStudents(UpdateView):
        model = Student
        form_class = updateStudentsForm
        template_name = "Students/update_students.html "

class deleteStudents(DeleteView):
        model = Student
        template_name = 'Students/delete_students.html'
        success_url = reverse_lazy('list_students')

#For Student Enrolment

class listStudentEnrolment(ListView):
    model = StudentEnrollment
    template_name = 'Students/enrolment/list_student.html'


class enrolStudent(CreateView):
    model = StudentEnrollment
    form_class = studentEnrolmentForm
    template_name = 'Students/enrolment/enrol_student.html'

class removeStudent(DeleteView):
    model = StudentEnrollment
    template_name = 'Students/enrolment/remove_student.html'
    success_url = reverse_lazy('list_student')


#for adding the student files

def file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        import pandas as pd
        excel_data= pd.read_excel(myfile)
        data = pd.DataFrame(excel_data)
        ids = data["ID"].tolist()
        firstnames = data["Firstname"].tolist()
        lastnames= data["Lastname"].tolist()
        emails = data["Email"].tolist()
        dobs= data["DOB"].tolist()
        courses = data["Course"].tolist()
        classes = data["Class"].tolist()
        i =0
        while i < len(ids):
            id = ids[i]
            firstname = firstnames[i]
            lastname = lastnames[i]
            email = emails[i]
            dob = dobs[i]
            course = courses[i]
            classs = classes[i]
            enrolTime = timezone.now()

            user = User.objects.create_user(username=firstname.lower())
            user.set_password(firstname.lower())
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            student_group = Group.objects.get(name='Student')
            user.groups.add(student_group)
            user.save()
            student = Student(user=user, studentID=id, first_Name=firstname, last_Name=lastname, email=email,
                              dateOfBirth=dob)
            class1 = Class.objects.get(number=classs)
            student.save()
            studentEnrolment = StudentEnrollment(student_id=student,class_id=class1,enrollTime=enrolTime)
            studentEnrolment.save

            i= i+1


        return render(request,'Students/file_upload_form.html', {
            'uploaded_file_url':uploaded_file_url
        })
    return render(request,'Students/file_upload_form.html',None)


#GradeBook

class GradeBookSemesterView(ListView):
    model = Semester
    template_name = 'gradebook/semesters_gradebook.html'

@login_required
def gradebook_class(request, pk):
    classes = Class.objects.filter(semester_id=pk)
    studentEnrolment = StudentEnrollment.objects.all()
    context = {
        "classes": classes,
        "studentEnrolment": studentEnrolment
    }
    return render(request, 'gradebook/classes_gradebook.html', context)


@login_required
def gradebook_student_list(request, pk):
    studentEnrolment = StudentEnrollment.objects.filter(class_id_id=pk)
    current_class = Class.objects.get(id=pk)
    context = {
        "semester_id": current_class.semester.id,
        "studentEnrolment": studentEnrolment
    }
    return render(request, 'gradebook/student_list_gradebook.html', context)


@login_required
def gradebook_grade_student(request):
    id = request.POST.get("id")
    grade = request.POST.get("grade")
    try:
        studentEnrolment = StudentEnrollment.objects.get(id=id)
        studentEnrolment.grade = grade
        studentEnrolment.gradeTime = timezone.now()
        studentEnrolment.save()
        senderemail= 'singhh59@myunitec.ac.nz'
        send_mail('Class Grade Notification', 'Your grade has been published! \nPlease check in gradebook :).',
                   senderemail, [studentEnrolment.student_id.email], fail_silently=False)
        message = "Student " + studentEnrolment.student_id.first_Name + " graded successfully!"
    except Exception as e:
        message = "Could not grade " + studentEnrolment.student_id.first_Name + "!" + str(e)

    context = {
        "message": message,
        "studentEnrolment": studentEnrolment
    }
    return render(request, 'gradebook/grade_student.html', context)


@login_required
def gradebook_grade_student_form(request, pk):
    studentEnrolment = StudentEnrollment.objects.get(id=pk)
    context = {"studentEnrolment": studentEnrolment}
    return render(request, 'gradebook/grade_student_form.html', context)
