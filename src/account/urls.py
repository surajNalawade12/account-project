from django.conf.urls import url, include
from rest_framework import routers
from account import views

account_list = views.AccountViewSet.as_view({
	'get':'retrieve',
	'post': 'create',
	'put' : 'update'
})

employee_list = views.EmployeeViewSet.as_view({
	'get':'retrieve',
	'post': 'create'
})

registration_list = views.RegistrationViewSet.as_view({
	 'get':'retrieve',
	 'post': 'create'
})

user_list = views.UserViewSet.as_view({
	 'get':'retrieve',
	 'put': 'update'
})

# account_detail = views.AccountViewSet.as_view({
#    'get' : 'retrieve',
#    'put' : 'update',
#    'patch' : 'partial_update',
#    'delete' : 'destroy'
# })

router = routers.SimpleRouter()
router.register(r'account', views.AccountViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'signup', views.RegistrationViewSet)
router.register(r'user', views.UserViewSet)

#  path('signup/', views.SignUp.as_view(), name='signup'),

urlpatterns = router.urls
