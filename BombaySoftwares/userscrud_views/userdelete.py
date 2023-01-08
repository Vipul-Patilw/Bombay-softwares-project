from BombaySoftwares.models import UserRegistration
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
class UserAccountDelete(LoginRequiredMixin,DeleteView):
		model = UserRegistration
		template_name = 'delete_user_account.html'
		success_url = reverse_lazy('home')