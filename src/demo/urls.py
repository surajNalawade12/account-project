from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from account import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('account.urls')),
	   
	# AUTHENTICATION
	# url(r'^api/auth/token/', obtain_jwt_token),
	# url(r'^api/token/refresh/', refresh_jwt_token),
	url(r'^rest-auth/', include('rest_auth.urls'))	
]
