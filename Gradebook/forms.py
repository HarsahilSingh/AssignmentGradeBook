from django import forms

from Gradebook.models import Course, Semester, Lecturer, Class, Student, StudentEnrollment



class DatePickerInput(forms.DateInput):
    input_type = 'date'


class addCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('code', 'name')

        widgets = {
            'code': forms.NumberInput(attrs={'class': 'form-content', 'placeholder': 'Course Code'}),
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'})

        }


class updateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('code', 'name')

        widgets = {
            'code': forms.NumberInput(attrs={'class': 'form-content', 'placeholder': 'Course Code'}),
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class addSemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ('year', 'semester')
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'min': '2022', 'max': '2100'}),
            'semester': forms.Select(attrs={'class': 'form-select'}),
        }


class updateSemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ('year', 'semester')

        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'min': '2022', 'max': '2100'}),
            'semester': forms.Select(attrs={'class': 'form-select'}),
        }


# Lecturer

class addLecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ('staffID', 'first_Name', 'last_Name', 'email', 'course', 'dateOfBirth')

        widgets = {
            'staffID': forms.NumberInput(attrs={'class': 'form-content', 'placeholder': 'staffID'}),
            'first_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'dateOfBirth': forms.DateInput(attrs={'class': 'form-control'}),
        }

class LecturerToClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('lecturer',)

        widgets = {
            'lecturer': forms.Select(attrs={'class': 'form-select'}),
        }


class updateLecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ('staffID', 'first_Name', 'last_Name', 'email', 'dateOfBirth')

        widgets = {
            'first_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'dateOfBirth': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Classes


class addClassesForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('number', 'semester', 'course', 'lecturer')

        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-content',}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'lecturer': forms.Select(attrs={'class': 'form-control'}),

        }


class updateClassesForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('number', 'semester', 'course', 'lecturer')

        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-content', 'placeholder': 'Course Number'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'lecturer': forms.Select(attrs={'class': 'form-control'}),
        }


class   assignLecturerForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('number', 'lecturer')

        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-content', 'placeholder': 'Course Number'}),
            'lecturer': forms.Select(attrs={'class': 'form-control'}),
        }


# Students

class addStudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('studentID', 'first_Name', 'last_Name', 'email', 'dateOfBirth')

        widgets = {
            'studentID': forms.NumberInput(attrs={'class': 'form-content', 'placeholder': 'studentID'}),
            'first_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'dateOfBirth': forms.DateInput(attrs={'class': 'form-control'}),

        }


class updateStudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('studentID', 'first_Name', 'last_Name', 'email', 'dateOfBirth')

        widgets = {
            'studentID': forms.NumberInput(attrs={'class': 'form-content', 'placeholder': 'studentID'}),
            'first_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'dateOfBirth': forms.DateInput(attrs={'class': 'form-control'}),

        }

#Student Enrolment Form

class studentEnrolmentForm(forms.ModelForm):
    class Meta:
        model = StudentEnrollment
        fields = ('student_id', 'class_id', 'grade', 'gradeTime')

        widgets = {
            'student_id': forms.Select(attrs={'class': 'form-select'}),
            'class_id': forms.Select(attrs={'class': 'form-select'}),
            'grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'gradeTime': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
