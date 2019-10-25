from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student
# from articles.models import Article


def students_list(request):
    template = 'school/students_list.html'
    list_students = []
    # без values - QuerySet:
    students = Student.objects.all().prefetch_related('teachers').order_by('group')# .values()
    for student in students:
        object_student = {}
        object_student['name'] = student.name
        object_student['group'] = student.group
        # с values - Dict:
        object_student['teachers'] = student.teachers.all().order_by('name').values('name', 'subject')

        list_students.append(object_student)
    context = {'list_students': list_students}

    return render(request, template, context)
