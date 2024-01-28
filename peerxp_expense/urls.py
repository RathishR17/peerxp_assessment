from django.urls import path
from .views import create_expense, update_delete_expense, view_expenses, delete_expense, login_page, logout_page

urlpatterns = [
    path('create-expense/', create_expense, name='create_expense'),
    path('update-delete-expense/<int:expense_id>/', update_delete_expense, name='update_delete_expense'),
    path('view-expenses/', view_expenses, name='view_expenses'),
    path('delete-expense/<int:expense_id>/', delete_expense, name='delete_expense'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
]
