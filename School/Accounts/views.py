from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import FeesCollection, Expense, Salary
from student.models import Student
from Teacher.models import Teacher

def fees_list(request):
    fees = FeesCollection.objects.all()
    return render(request, 'Accounts/fees.html', {'fees': fees})

def add_fees(request):
    students = Student.objects.all()
    if request.method == 'POST':
        student_id = request.POST.get('student')
        amount = request.POST.get('amount')
        payment_date = request.POST.get('payment_date')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')
        description = request.POST.get('description')
        student = get_object_or_404(Student, id=student_id)
        FeesCollection.objects.create(
            student=student,
            amount=amount,
            payment_date=payment_date,
            due_date=due_date,
            status=status,
            description=description
        )
        messages.success(request, 'Fee added successfully')
        return redirect('fees_list')
    return render(request, 'Accounts/add_fees.html', {'students': students})

def delete_fees(request, fee_id):
    fee = get_object_or_404(FeesCollection, id=fee_id)
    fee.delete()
    messages.success(request, 'Fee deleted successfully')
    return redirect('fees_list')


def expenses_list(request):
    expenses = Expense.objects.all()
    return render(request, 'Accounts/expenses.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        description = request.POST.get('description')
        Expense.objects.create(
            title=title,
            category=category,
            amount=amount,
            date=date,
            description=description
        )
        messages.success(request, 'Expense added successfully')
        return redirect('expenses_list')
    return render(request, 'Accounts/add_expense.html')

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.delete()
    messages.success(request, 'Expense deleted successfully')
    return redirect('expenses_list')


def salary_list(request):
    salaries = Salary.objects.all()
    return render(request, 'Accounts/salary.html', {'salaries': salaries})

def add_salary(request):
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher')
        amount = request.POST.get('amount')
        payment_date = request.POST.get('payment_date')
        month = request.POST.get('month')
        status = request.POST.get('status')
        description = request.POST.get('description')
        teacher = get_object_or_404(Teacher, id=teacher_id)
        Salary.objects.create(
            teacher=teacher,
            amount=amount,
            payment_date=payment_date,
            month=month,
            status=status,
            description=description
        )
        messages.success(request, 'Salary added successfully')
        return redirect('salary_list')
    return render(request, 'Accounts/add_salary.html', {'teachers': teachers})

def delete_salary(request, salary_id):
    salary = get_object_or_404(Salary, id=salary_id)
    salary.delete()
    messages.success(request, 'Salary deleted successfully')
    return redirect('salary_list')