from django.urls import path 
from.import views
urlpatterns=[
    path('',views.category_list,name='category_list'),
path('categories/',views.CategoryListCreateView.as_view(),name='categories-list-create'),
path('categories/<int:pk>/',views.CategoryRetrieveUpdateDestroyView.as_view(),name='categories-details'),
]