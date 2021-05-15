from django.urls import path
from . import views

urlpatterns=[
    path('', views.books),
    path('create', views.create),
    path('<int:book_id>', views.show),
    path('<int:book_id>/add_fav', views.add_fav),
    path('<int:book_id>/remove', views.remove),
    path('<int:book_id>/destroy', views.delete),
    path('<int:book_id>/edit', views.edit),
]