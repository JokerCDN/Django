from django.shortcuts import render, redirect
from .models import Classes, Student, Teacher


# Create your views here.


def class_list(request):
    data = Classes.objects.all()
    return render(request, 'class_list.html', {'class_list': data})


def delete_list(request):
    delete_id = request.GET.get('id')
    Classes.objects.get(id=delete_id).delete()
    return redirect('/class_list/')


def edit_list(request):
    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        class_name = request.POST.get('class_name')
        obj = Classes.objects.get(id=class_id)
        obj.name = class_name
        obj.save()
        return redirect('/class_list/')

    edit_id = request.GET.get('id')
    edit_obj = Classes.objects.get(id=edit_id)

    return render(request, 'edit_list.html', {'class': edit_obj})


def student_list(request):
    """

    :param request:
    :return:
    """
    data = Student.objects.all()
    return render(request, 'student_list.html', {'student_list': data})


def add_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        class_id = request.POST.get('class_id')
        Student.objects.create(name=student_name, classes_id=class_id)
        return redirect('/student_list/')
    data = Classes.objects.all()
    return render(request, 'add_student.html', {'class_list': data})


def delete_student(request):
    delete_id = request.GET.get('id')
    Student.objects.get(id=delete_id).delete()
    return redirect('/student_list/')


def edit_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        classesid = request.POST.get('class_id')
        obj = Student.objects.get(id=student_id)
        obj.name = student_name
        obj.classes_id = classesid
        obj.save()
        return redirect('/student_list/')

    edit_id = request.GET.get('id')
    obj = Student.objects.get(id=edit_id)
    data = Classes.objects.all()
    return render(request, 'edit_student.html', {'student': obj, 'class_lis': data})


def teacher_list(request):
    data = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teacher_list': data})


def add_teacher(request):
    if request.method == "POST":
        teacher_name = request.POST.get('teacher_name')
        teacher_class = request.POST.getlist('class_id')
        teacher_obj = Teacher.objects.create(name=teacher_name)
        teacher_obj.classes.set(teacher_class)
        teacher_obj.save()
        return redirect('/teacher_list/')
    class_lis = Classes.objects.all()
    return render(request, 'add_teacher.html', {'class_list': class_lis})


def edit_teacher(request):
    if request.method == 'POST':
        edit_name = request.POST.get('teacher_name')
        edit_class = request.POST.getlist('class_id')
        teacher_id = request.POST.get('teacher_id')
        obj = Teacher.objects.get(id=teacher_id)
        obj.name = edit_name
        obj.classes.set(edit_class)
        obj.save()
        return redirect('/teacher_list/')
    edit_id = request.GET.get('id')
    teacher_obj = Teacher.objects.get(id=edit_id)
    data = Classes.objects.all()
    return render(request, 'edit_teacher.html', {'teacher': teacher_obj, 'classes': data})


def test(request):
    s = 'datadfsgxfgbrds'
    l = ['d', 'f', 'gx']
    d = {"name": "小东北", "hobby": "社会摇"}

    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return self.name + '********'

        def dream(self):
            return '------------'

    p1 = Person('alex', 38)
    p2 = Person('alex02', 58)
    file_size = 1024444444444
    import _datetime
    now = _datetime.datetime.now()
    print(now)
    # p_list = [p1, p2]
    p_list = [p1, p2]
    s_a = '<a href=''>1111111111</a>'
    # s_a = "<a href='http://www.sogo.com'>点我直达！</a>"
    s_1 = """
            世情薄，
            人情恶，
            雨送黄昏花易落。
            晓风干，
            泪痕残，
            欲笺心事，
            独倚斜栏，
            难，难，难！
        """


    return render(request,
                  'test.html',
                  {'data': s, 'l': l, 'd': d,
                   'p1': p1,
                   'p2': p2,
                   'P_list': p_list,
                   'file_size': file_size,
                   'now': now,
                   's_a': s_a,
                   's_1':s_1,


                   }
                  )
