from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Expense, UserProfile, CustomUser
from .forms import ExpenseForm

# CRUD operations for expenses
def create_expense(request):
    form = ExpenseForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        expense = form.save(commit=False)
        expense.created_by = request.user
        expense.save()
        messages.success(request, 'Expense created successfully!')
        return redirect('view_expenses')

    return render(request, 'expenses/create_expense.html', {'form': form})

def update_delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)

    if request.user != expense.created_by:
        return render(request, '403_forbidden.html')  # Custom 403 Forbidden page

    form = ExpenseForm(request.POST or None, instance=expense)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Expense updated successfully!')
        return redirect('view_expenses')

    return render(request, 'expenses/update_delete_expense.html', {'form': form, 'expense': expense})

def view_expenses(request):
    user_profile = UserProfile.objects.get(user=request.user)
    expenses = Expense.objects.all()

    if user_profile.role == 'Member':
        expenses = expenses.filter(created_by=request.user)

    return render(request, 'expenses/view_expenses.html', {'expenses': expenses})

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)

    if request.user != expense.created_by:
        return render(request, '403_forbidden.html')  # Custom 403 Forbidden page

    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
        return redirect('view_expenses')

# User authentication
def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('view_expenses')
        else:
            messages.error(request, 'Invalid email or password. Please try again.')

    return render(request, 'login_page.html')
#logout
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out successfully')
    return redirect('login_page')
