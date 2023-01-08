from BombaySoftwares.models import UserRegistration
from django.views.generic import ListView
from django.shortcuts import  redirect,render


from django.contrib.auth.mixins import LoginRequiredMixin
class UsersDetail(LoginRequiredMixin,ListView,):
		model = UserRegistration
		template_name = 'all_users.html'
		context_object_name = 'users_list'
		paginate_by = 5
		
		def get_queryset(self):
			order_by = self.request.GET.get('order_by', 'first_name')
			user = UserRegistration.objects.all().order_by(order_by)
			return user
		
	#	return render (request,"all_users.html",{'users_list':user})
		
		