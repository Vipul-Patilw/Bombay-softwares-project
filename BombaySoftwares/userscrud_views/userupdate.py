from django.urls import reverse_lazy
from BombaySoftwares.models import UserRegistration
from django.views.generic.edit import UpdateView
from BombaySoftwares.forms import UserCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
class UserAccountUpdate(LoginRequiredMixin,UpdateView):

		model = UserRegistration
		template_name = 'registration/user_registration.html'
		form_class = UserCreateForm	
		success_url = reverse_lazy('home')
		def form_valid(self, form):
			email = form.cleaned_data['email']
			user = self.request.user
			current_email = user.email
			if email != current_email:
				myuser = User.objects.get(email=current_email)
				myuser.email = email
				myuser.username = email
				myuser.save()
				logout(self.request)
			
			return super(UserAccountUpdate, self).form_valid(form)