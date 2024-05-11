from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("majdoor_afterlogin/<str:m_id>", views.majdoor_afterlogin, name='majdoor_afterlogin'),
    path("contact", views.contact, name="contact"),   
    path("majdoor_login", views.majdoor_login, name="majdoor_login"),
    path("customer_login", views.customer_login, name="customer_login"),
    path("customer_afterlogin", views.customer_afterlogin, name="customer_afterlogin"),
    path("customer_sign_up", views.customer_sign_up, name="customer_sign_up"),
    path("forget", views.forget, name="forget"),  
    path("majdoor_signup", views.majdoor_signup, name="majdoor_signup"),
    path("about", views.about, name="about"),
    path("guide", views.guide, name="guide"),
    path("feedback", views.feedback, name="feedback"),
    path("thank", views.thank, name="thank"),
    path('call-support/', views.call_support, name='call_support'),
 

]
