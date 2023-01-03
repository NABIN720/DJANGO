from django.urls import path
from pages.views import home, about,todo,remove_todo

urlpatterns = [
    path('',home),
    path('about/',about),
    # path('send/',send),
    
    # path('recieve/',recieve,name="recieve"),

    path('todo/',todo,name="todo"),

    path('remove_todo/<str:todo>/',remove_todo,name="remove_todo"),
]
