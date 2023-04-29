from django.urls import path
from . import views

# define your urls here
urlpatterns = [
    path('', views.index, name='index'),
    path('guides', views.guides, name='guides'),
    path('register/', views.register, name='register'),
    path('new_ticket', views.new_ticket, name='new_ticket'),
    path('my_tickets', views.my_tickets, name='my_tickets'),
    path('tickets', views.tickets, name='tickets'),
    path('ticket/<int:ticket_id>', views.ticket, name='ticket'),
    path('edit_ticket/int:<ticket_id>', views.edit_ticket, name='edit_ticket'),
    path('edit_comment/int:<comment_id>', views.edit_comment, name='edit_comment'),
]
