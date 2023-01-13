from BombaySoftwares.models import UserRegistration
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
class UserAccountDelete(LoginRequiredMixin,DeleteView):
		model = UserRegistration
		template_name = 'delete_user_account.html'
		success_url = reverse_lazy('home')
		def form_valid(self,form):
			email= self.object.email
			user = User.objects.get(username=email)
			user.delete()
			return super(UserAccountDelete, self).form_valid(form)
