from django.shortcuts import render,HttpResponse,redirect
from BombaySoftwares.userscrud_views.userdelete import UserAccountDelete
from BombaySoftwares.userscrud_views.userupdate import UserAccountUpdate
from BombaySoftwares.usersdetail_view.usersdetail import  UsersDetail
from BombaySoftwares.models import UserRegistration
from django.contrib.auth import logout
import pathlib
UsersDetail
from django.contrib.auth.views import LogoutView,PasswordChangeView,PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.mail import EmailMessage
from BombaySoftwaresProject import settings
from mailqueue.models import MailerMessage
from datetime import datetime

from django.template import RequestContext
# Create your views here.

UserAccountDelete
UserAccountUpdate
 

class ChangePassword(LoginRequiredMixin,PasswordChangeView):
	
	form_class = PasswordChangeForm
	template_name = "registration/change_password.html"
	success_url = reverse_lazy('logout-after-change-pass') 

def logout_after_change_password(request):
	#Using mailqueue method
	my_email = "bankingsolutions701@gmail.com"
	my_name = "Banking Solutions"
	content = f"""
dear user,

Your password is changed successfully.
Please login again to application 

Thanks,
Bombay Softwares 
"""
	msg = MailerMessage()
	msg.subject = "Password Updated"
	msg.to_address = request.user.email
	msg.from_address = '{} <{}>'.format(my_name, my_email)
	msg.content = content
	msg.html_content = content
	#msg.sent = True
	msg.save()
	#Using django mail method
	#email_sub = 'Password Updated'
#	email_body = """
#Dear user,

#Your Password is Changed successfully.
#Login again to application 

#Thanks,
#Bombay Softwares 
#"""
#	email = EmailMessage(
#				email_sub,
#				email_body,
#				settings.EMAIL_HOST_USER,
#				[request.user.email],
#				)
#	email.fail_silently = True
#	email.send()
	logout(request)
	return redirect ('logout-page')
  
def updateProfile(request):
	if request.user.is_anonymous:
		return redirect('login')
	
	if request.method == 'POST':
		profile_pic = request.FILES.get('profile_pic')
		current_user = request.user
		email = current_user.email
		user = UserRegistration.objects.get(email=email)
		user.profile_pic = profile_pic
		user.save()
		return redirect('personal_detail')
	
	return render(request,"index.html")

def search (request):
			if 'search' in request.POST:
			     	search= request.POST.get('search')
			     	users = UserRegistration.objects.filter(Q(first_name__icontains = search) | Q(last_name__icontains = search) | Q(email__icontains = search) | Q(mobile_number__icontains = search) | Q(type__icontains = search)).all()
			     	return render(request,'searchdetail.html',{'search_user':users,"search":search})
			return render (request,"all_users.html")
			
def storesocialacccount(request,email,first_name):
	UserRegistration.objects.create(email=email,first_name=first_name,birthdate=datetime.now(),type="Secondary")
	return redirect('home')




def handler404(request, exception):

    return render(request,'404.html',status=404)

