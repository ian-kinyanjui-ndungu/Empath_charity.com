from django.urls import path

from . import views
urlpatterns=[
    path('', views.home, name="my_home"),

    path('404/', views.custom_404, name="error_404"),

    path('about/', views.about, name="my_about"),

    path('contact', views.contact, name="my_contacts"),

    path('donation/', views.donation, name="my_donation"),

    path('event/', views.event, name="my_event"),

    path('feature/', views.feature, name="my_feature"),

    path('service/', views.service, name = "my_service"),

    path('team/', views.team, name = "my_team"),
    
    path('testimonial', views.testimonial, name="my_testimonial")



]
