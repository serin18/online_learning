from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from django.contrib import messages


def func1(request):
    return render(request,'index.html')

def func2(request):
    return render(request,'f1.html')

def pythoncourse(request):
    return render(request,'pythoncourse.html')

def register(request):
    return render(request,'register.html')

def register1(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        photo = request.FILES['photo']
        address = request.POST['address']
        qualification = request.POST['qualification']
        course = request.POST['course']
        data=course_register.objects.create(full_name=name,email=email,phone=phone,dob=dob,photo=photo,address=address,qualification=qualification,course=course)
        data.save()
    return render(request,'home.html')

def DScourse(request):
    return render(request,'DScourse.html')

def mernstackcourse(request):
    return render(request,'mernstackcourse.html')

def DMcourse(request):
    return render(request,'DMcourse.html')

def fluttercourse(request):
    return render(request,'fluttercourse.html')

def pythonbook(request):
    return render(request,'pythonbook.html')

def pythonbook1(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        photo = request.FILES['photo']
        address = request.POST['address']
        qualification = request.POST['qualification']
        payid = request.POST['payid']
        data=python_book.objects.create(full_name=name,email=email,phone=phone,dob=dob,photo=photo,address=address,qualification=qualification,payid=payid)
        data.save()
    return render(request,'pythoncourse.html')

def dsbook(request):
    return render(request,'DSbook.html')

def dsbook1(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        photo = request.FILES['photo']
        address = request.POST['address']
        qualification = request.POST['qualification']
        payid = request.POST['payid']
        data=DS_book.objects.create(full_name=name,email=email,phone=phone,dob=dob,photo=photo,address=address,qualification=qualification,payid=payid)
        data.save()
    return render(request,'DScourse.html')

def mernstackbook(request):
    return render(request,'mernstackbook.html')

def mernstackbook1(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        photo = request.FILES['photo']
        address = request.POST['address']
        qualification = request.POST['qualification']
        payid = request.POST['payid']
        data=mernstack_book.objects.create(full_name=name,email=email,phone=phone,dob=dob,photo=photo,address=address,qualification=qualification,payid=payid)
        data.save()
    return render(request,'mernstackcourse.html')

def DMbook(request):
    return render(request,'DMbook.html')

def flutterbook(request):
    return render(request,'flutterbook.html')

def DMbook1(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        photo = request.FILES['photo']
        address = request.POST['address']
        qualification = request.POST['qualification']
        payid = request.POST['payid']
        data=DM_book.objects.create(full_name=name,email=email,phone=phone,dob=dob,photo=photo,address=address,qualification=qualification,payid=payid)
        data.save()
    return render(request,'DMcourse.html')

def flutterbook1(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        photo = request.FILES['photo']
        address = request.POST['address']
        qualification = request.POST['qualification']
        payid = request.POST['payid']
        data=flutter_book.objects.create(full_name=name,email=email,phone=phone,dob=dob,photo=photo,address=address,qualification=qualification,payid=payid)
        data.save()
    return render(request,'fluttercourse.html')

def usersignup(request):
    return render(request,'usersignup.html')

def usersignup1(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        photo = request.FILES['photo']
        dob = request.POST['dob']
        if user_log.objects.filter(user_name=name):
            messages.info(request, 'Username already exist! Try another Username...')
            return redirect(usersignup)
        else:
            if user_log.objects.filter(email=email):
                messages.info(request, 'E-mail already exist! Try another E-mail...')
                return redirect(usersignup)
            else:
                if password1 == password2:
                    data=user_log.objects.create(user_name=name,email=email,password=password1,photo=photo,dob=dob)
                    data.save()
                    return render(request,'index.html')
                else:
                    messages.info(request, 'Password did not matched!')
                    return redirect(usersignup)

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def userlogin(request):
    if request.method == 'POST':
        mail = request.POST['email']
        pswd = request.POST['password']
        data = user_log.objects.filter(email=mail)
        admindata = admin_login.objects.filter(email=mail)
        tutordata = tutor_log.objects.filter(email=mail)
        if data:
            data1 = user_log.objects.get(email=mail)
            if data1.password == pswd:
                request.session['id'] = mail
                current_login.objects.update(email=mail)
                return redirect(home)
            else:
                messages.info(request,'invalid E-mail or Password')
                return redirect(login)
        elif admindata:
            data2 = admin_login.objects.get(email=mail)
            if data2.pasw == pswd:
                request.session['id'] = mail
                return redirect(adminpage)
            else:
                messages.info(request, 'invalid E-mail or Password')
                return redirect(login)
        elif tutordata:
            data3 = tutor_log.objects.get(email=mail)
            if data3.password == pswd:
                request.session['id'] = mail
                if data3.status == "approve":
                    return redirect(tutorhome)
                else:
                    messages.info(request, 'You are not accepted yet')
                    return redirect(login)
            else:
                messages.info(request, 'invalid E-mail or Password')
                return redirect(login)
        else:
            messages.info(request, 'invalid E-mail or Password')
            return redirect(login)


def tutorsignup(request):
    return render(request,'tutorsignup.html')

def tutorsignup1(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        resume = request.FILES['resume']
        if tutor_log.objects.filter(user_name=name):
            messages.info(request, 'Username already exist! Try another Username...')
            return redirect(tutorsignup)
        else:
            if tutor_log.objects.filter(email=email):
                messages.info(request, 'E-mail already exist! Try another E-mail...')
                return redirect(tutorsignup)
            else:
                if password1 == password2:
                    data=tutor_log.objects.create(user_name=name,email=email,password=password1,resume=resume)
                    data.save()
                    return render(request,'index.html')
                else:
                    messages.info(request, 'Password did not matched!')
                    return redirect(tutorsignup)

def trialpython(request):
    return render(request,'trialpython.html')

def pythontrial1(request):
    if request.method=='POST':
        name = request.POST['name']
        course = request.POST['course']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        payid = request.POST['payid']
        data=trial.objects.create(full_name=name,course=course,email=email,phone=phone,date=date,payid=payid)
        data.save()
    return render(request,'pythoncourse.html')

def trialDS(request):
    return render(request,'trialDS.html')

def trialDS1(request):
    if request.method=='POST':
        name = request.POST['name']
        course = request.POST['course']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        payid = request.POST['payid']
        data=trial.objects.create(full_name=name,course=course,email=email,phone=phone,date=date,payid=payid)
        data.save()
    return render(request,'DScourse.html')

def trialMS(request):
    return render(request,'trialMS.html')

def trialMS1(request):
    if request.method=='POST':
        name = request.POST['name']
        course = request.POST['course']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        payid = request.POST['payid']
        data=trial.objects.create(full_name=name,course=course,email=email,phone=phone,date=date,payid=payid)
        data.save()
    return render(request,'mernstackcourse.html')

def trialdigitalmarketing(request):
    return render(request,'trialdigitalmarketing.html')

def trialdigitalmarketing1(request):
    if request.method=='POST':
        name = request.POST['name']
        course = request.POST['course']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        payid = request.POST['payid']
        data=trial.objects.create(full_name=name,course=course,email=email,phone=phone,date=date,payid=payid)
        data.save()
    return render(request,'DMcourse.html')

def trialflutter(request):
    return render(request,'trialflutter.html')

def trialflutter1(request):
    if request.method=='POST':
        name = request.POST['name']
        course = request.POST['course']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        payid = request.POST['payid']
        data=trial.objects.create(full_name=name,course=course,email=email,phone=phone,date=date,payid=payid)
        data.save()
    return render(request,'fluttercourse.html')

def tutorlogin(request):
    return render(request,'tutorlogin.html')

def tutorlogin1(request):
    if request.method == 'POST':
        mail = request.POST['email']
        pswd = request.POST['password']
        data = tutor_log.objects.filter(email=mail)
        if data:
            data1 = tutor_log.objects.get(email=mail)
            if data1.password == pswd:
                request.session['id'] = mail
                return redirect(tutorhome)
            else:
                messages.info(request,'invalid E-mail or Password')
                return redirect(tutorlogin)
        else:
            messages.info(request,'invalid E-mail or Password')
            return redirect(tutorlogin)

def adminpage(request):
    return render(request,'admin.html')

def tutorhome(request):
    return render(request,'tutorhome.html')

def sendhost(request):
    return render(request,'sendhostdetails.html')

def sendhost1(request):
    if request.method=='POST':
        date = request.POST['date']
        starting_time = request.POST['starting_time']
        duration = request.POST['duration']
        subject = request.POST['subject']
        topic = request.POST['topic']
        data=class_link.objects.create(date=date,time=starting_time,duration=duration,subject=subject,topic=topic)
        data.save()
        return render(request, 'tutorhome.html')

def certificateupload(request, *args, **kwargs):
    current_user = current_login.objects.first()  # Assuming you are getting the first logged-in user
    email = current_user.email
    data = user_log.objects.get(email=email)
    print(data)
    if data.status == "certificate":
        return render(request,'certificateupload.html')
    else:
        # Pass a flag to indicate access denied
        return render(request, 'home.html', {'access_denied': True})

def certificateupload1(request):
    if request.method=='POST':
        email = request.POST['email']
        sslc = request.FILES['SSLC']
        plustwo = request.FILES['plustwo']
        degree = request.FILES['degree']
        data=certificate.objects.create(email=email,sslc=sslc,plustwo=plustwo,degree=degree)
        data.save()
    return render(request,'certificateupload.html')

def adminlogin(request):
    return render(request,'adminlogin.html')

def adminlogin1(request):
    if request.method == 'POST':
        name = request.POST['email']
        pswd = request.POST['password']
        data = admin_login.objects.filter(full_name=name)
        if data:
            data1 = admin_login.objects.get(pasw=pswd)
            if data1.pasw == pswd:
                request.session['id'] = name
                return redirect(adminpage)
            else:
                messages.info(request,'invalid E-mail or Password')
                return redirect(adminlogin)
        else:
            messages.info(request,'invalid E-mail or Password')
            return redirect(adminlogin)

def meeting(request):
    return render(request,'meeting.html')

def classes(request, *args, **kwargs):
    mail_queryset = current_login.objects.all()
    mail = [obj.email for obj in mail_queryset]
    data1=class_link.objects.all()
    current_user = current_login.objects.first()  # Assuming you are getting the first logged-in user
    email = current_user.email
    data = user_log.objects.get(email=email)
    for mail in mail:
        d=user_log.objects.filter(email=mail)
        print(email)
    if data.status == "classes":
        course_data = course_register.objects.filter(email=email)
        courses = [data.course for data in course_data]
        related_courses = class_link.objects.filter(subject__in=courses)
        print(related_courses)
        return render(request,'classes.html', {'data': d,'data1': related_courses})
    else:
        # Pass a flag to indicate access denied
        return render(request, 'home.html', {'access_denied': True})

def approvetutor(request):
    data=tutor_log.objects.filter(status='pending')
    return render(request,'approvetutor.html',{'data':data})

def accept_tutor(request,id):
    tutor_log.objects.filter(pk=id).update(status='approve')
    return redirect(approvetutor)

def reject_tutor(request,id):
    tutor_log.objects.filter(pk=id).delete()
    return redirect(approvetutor)

def managestudent(request):
    data = user_log.objects.all()
    return render(request,'managestudent.html',{'data':data})


def update_status(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        action = request.POST.get('action')

        try:
            # Fetch the user_log instance and update the status
            user = user_log.objects.get(email=email)
            user.status = action
            user.save()
            return redirect(managestudent)  # Replace with your dashboard view name
        except user_log.DoesNotExist:
            return HttpResponse("User with given email does not exist", status=404)
    return HttpResponse("Invalid request method", status=405)

def interview(request):
    return render(request, 'progress.html')

def resume(request, *args, **kwargs):
    current_user = current_login.objects.first()  # Assuming you are getting the first logged-in user
    email = current_user.email
    data = user_log.objects.get(email=email)
    print(data)
    if data.status == "resume":
        return render(request, 'progress.html')
    else:
        # Pass a flag to indicate access denied
        return render(request, 'home.html', {'access_denied': True})

def placement(request, *args, **kwargs):
    current_user = current_login.objects.first()
    email = current_user.email
    data = user_log.objects.get(email=email)
    if data.status == "placement":
        return render(request,'placement.html')
    else:
        return render(request, 'home.html', {'access_denied': True})

def applyjob(request):
    return render(request,'applyjob.html')

def applyjob1(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        resume = request.FILES['resume']
        data=apply_job.objects.create(full_name=name,email=email,phone=phone,resume=resume)
        data.save()
    return render(request,'placement.html')

def viewtutor(request):
    d=tutor_log.objects.filter(status="approve")
    return render(request,'viewtutor.html',{'data':d})

def remove_tutor(request,id):
    tutor_log.objects.filter(pk=id).delete()
    return redirect(viewtutor)

def adviewclass(request):
    d=class_link.objects.all()
    return render(request,'adminviewclass.html',{'data':d})

def adviewbook(request):
    d=python_book.objects.all()
    d1 = DS_book.objects.all()
    d2 = mernstack_book.objects.all()
    d3 = DM_book.objects.all()
    d4 = flutter_book.objects.all()
    return render(request,'adviewbook.html',{'data':d,'data1':d1,'data2':d2,'data3':d3,'data4':d4})

def interviewform(request, *args, **kwargs):
    current_user = current_login.objects.first()
    email = current_user.email
    data = user_log.objects.get(email=email)
    if data.status == "interview":
        return render(request,'interviewform.html')
    else:
        return render(request, 'home.html', {'access_denied': True})

def interviewform1(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        qualification = request.POST['qualification']
        course = request.POST['course']
        data=interviewsave.objects.create(full_name=name,email=email,phone=phone,qualification=qualification,course=course)
        data.save()
    return render(request,'interviewform.html')

def tutorinterview(request):
    d=interviewsave.objects.all()
    return render(request,'tutorinterview.html',{'data':d})