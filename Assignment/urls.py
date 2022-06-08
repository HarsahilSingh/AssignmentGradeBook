"""Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.backends import django
from django.urls import path, include

from Gradebook.views import listCourse, HomePageView, createCourse, updateCourse, deleteCourse, listSemester, \
    createSemester, deleteSemester, updateSemester, listLecturer, updateLecturer, deleteLecturer, \
    listClasses, createClasses, updateClasses, deleteClasses, listStudents, updateStudents, \
    deleteStudents, assignLecturer, listStudentEnrolment, enrolStudent, removeStudent, \
    create_student_form, create_student, GradeBookSemesterView, gradebook_class, gradebook_student_list, \
    gradebook_grade_student, gradebook_grade_student_form, create_lecturer_form, create_lecturer, \
     file_upload

urlpatterns = [
 path('admin/', admin.site.urls),

   #For home
    path('',HomePageView.as_view(),name="home"),
   #For Course
    path("listcourse/",listCourse.as_view(), name="list_course"),
    path("createcourse/",createCourse.as_view(),name="create_course"),
    path('updatecourse/<int:pk>',updateCourse.as_view(),name="update_course"),
    path('deletecourse/<int:pk>', deleteCourse.as_view(), name="delete_course"),
    #For Semesters
    path("listsemester/",listSemester.as_view(), name="list_semester"),
    path("createsemester/",createSemester.as_view(),name="create_semester"),
    path('updatesemester/<int:pk>',updateSemester.as_view(),name="update_semester"),
    path('deletesemester/<int:pk>', deleteSemester.as_view(), name="delete_semester"),

    #For Lecturers
    path("listlecturer/",listLecturer.as_view(), name="list_lecturer"),
    path("createlecturer/",create_lecturer,name="create_lecturer"),
    path("createlecturerform",create_lecturer_form,name="create_lecturer_form"),
    path('updatelecturer/<int:pk>',updateLecturer.as_view(),name="update_lecturer"),
    path('deletelecturer/<int:pk>', deleteLecturer.as_view(), name="delete_lecturer"),

   # For Classes
   path("listclasses/", listClasses.as_view(), name="list_classes"),
   path("createclasses/", createClasses.as_view(), name="create_classes"),
   path('updateclasses/<int:pk>', updateClasses.as_view(), name="update_classes"),
   path('deleteclasses/<int:pk>', deleteClasses.as_view(), name="delete_classes"),
   path('assignlecturer/<int:pk>',assignLecturer.as_view(),name="assign_lecturer"),

    # For Students
    path("liststudents/", listStudents.as_view(), name="list_students"),
    path("createstudents/", create_student, name="create_students"),
    path("createstudentform",create_student_form,name="create_student_form"),
    path('updatestudents/<int:pk>', updateStudents.as_view(), name="update_students"),
    path('deletestudents/<int:pk>', deleteStudents.as_view(), name="delete_students"),
    path('uploadfile/',file_upload,name='upload_file'),

    #For enrolmets
    path('liststudent/', listStudentEnrolment.as_view(), name="list_student"),
    path('enrolstudent/', enrolStudent.as_view(), name="enrol_student"),
    path("removestudent/<int:pk>", removeStudent.as_view(), name="remove_student"),

#For gradebook
    path('gradebook',GradeBookSemesterView.as_view(),name="semesters_gradebook"),
    path('gradebook/<int:pk>/classes', gradebook_class, name='classes_gradebook'),
    path('gradebook/<int:pk>/students', gradebook_student_list, name='student_list_gradebook'),
    path('gradebook/grade_student', gradebook_grade_student, name='grade_student'),
    path('gradebook/grade_student_form/<int:pk>', gradebook_grade_student_form, name='grade_student_form'),


    #login(/users)
    path('members/',include('django.contrib.auth.urls'))


]
