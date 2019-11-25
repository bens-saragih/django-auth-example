from django.conf.urls import url,include
from django.contrib import admin
from .views import home,signup,secret_page,secretpage2,izin,myview
#password_change

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^izin/',izin,name='izin'),
    url(r'^$', home,name='home'),
    url(r'^secret/',secret_page,name='secret'),
    url(r'^email/',myview.as_view(),name='email_cek'),
    url(r'^secret2/',secretpage2.as_view(),name='secret2'),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    #url(r'^accounts/login/$',auth_views.LoginView.as_view(template_name='registration/login.html',redirect_authenticated_user=True)),
	url(r'^signup/', signup,name='signup'),
	#url(r'^change/',password_change,name='change'),

]
