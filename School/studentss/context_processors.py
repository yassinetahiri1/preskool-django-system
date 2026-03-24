from student.models import Student
from Teacher.models import Teacher
from Departement.models import Department
from Subject.models import Subject
from Holidays.models import Holiday
def sidebar_context(request):
    first_student = Student.objects.first()
    first_teacher = Teacher.objects.first()
    first_departement = Department.objects.first()
    first_subject = Subject.objects.first()
    first_holiday = Holiday.objects.first()
    return {
        'first_student': first_student,
        'first_teacher': first_teacher,
        'first_departement' : first_departement,
        'first_subject' : first_subject ,
        'first_holiday' : first_holiday ,
    }