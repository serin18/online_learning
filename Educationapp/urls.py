"""
URL configuration for Education project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.func1),
    path('1',views.func2),
    path('2',views.pythoncourse),
    path('3',views.register),
    path('4',views.register1),
    path('5',views.DScourse),
    path('6',views.mernstackcourse),
    path('7',views.DMcourse),
    path('8',views.pythonbook),
    path('9',views.pythonbook1),
    path('10',views.dsbook),
    path('11',views.dsbook1),
    path('12',views.mernstackbook),
    path('13',views.mernstackbook1),
    path('14',views.DMbook),
    path('15',views.DMbook1),
    path('16',views.usersignup),
    path('17',views.usersignup1),
    path('18',views.home),
    path('19',views.login),
    path('20',views.userlogin),
    path('21',views.fluttercourse),
    path('22',views.tutorsignup),
    path('23',views.tutorsignup1),
    path('24',views.trialpython),
    path('25',views.pythontrial1),
    path('26',views.trialDS),
    path('27',views.trialDS1),
    path('28',views.trialMS),
    path('29',views.trialMS1),
    path('30',views.trialdigitalmarketing),
    path('31',views.trialdigitalmarketing1),
    path('32',views.trialflutter),
    path('33',views.trialflutter1),
    path('34',views.flutterbook),
    path('35',views.flutterbook1),
    path('36',views.adminpage),
    path('37',views.tutorhome),
    path('38',views.tutorlogin),
    path('39',views.tutorlogin1),
    path('40',views.sendhost),
    path('41',views.sendhost1),
    path('42',views.certificateupload),
    path('43',views.certificateupload1),
    path('44',views.adminlogin),
    path('45',views.adminlogin1),
    path('46',views.meeting),
    path('meeting',views.classes),
    path('approvetutor',views.approvetutor),
    path('47/<id>',views.accept_tutor),
    path('48/<id>',views.reject_tutor),
    path('managestudent',views.managestudent),
    path('update_status/',views.update_status),
    path('49',views.interview),
    path('50',views.resume),
    path('51',views.placement),
    path('52',views.applyjob),
    path('53',views.applyjob1),
    path('54',views.viewtutor),
    path('55/<id>',views.remove_tutor),
    path('56',views.adviewclass),
    path('57',views.adviewbook),
    path('58',views.interviewform),
    path('59',views.interviewform1),
    path('60',views.tutorinterview)
]