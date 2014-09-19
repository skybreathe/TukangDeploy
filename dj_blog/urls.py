from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.login', name='login'),
    # url(r'^mkdir/$','blog.views.exemkdir'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^blog/(?P<slug>[-\w]+)$','blog.views.blog', name = 'blog'),	
    url(r'^admin/', include(admin.site.urls)),
	url(r'^add/', 'blog.views.add', name = 'add'),
	url(r'^home/', 'blog.views.home', name = 'home'),
	url(r'^createfile/', 'blog.views.createfile', name='createfile'),
	url(r'^deletedir/', 'blog.views.deletedir', name='deletedir'),
	url(r'^deletefile/', 'blog.views.deletefile', name='deletefile'),
	url(r'^copy/', 'blog.views.copy', name= 'copy'),
	url(r'^makedir/', 'blog.views.makedir', name='makedir'),
	url(r'^execute/', 'blog.views.execpy', name= 'execute'),
	url(r'^putfile/', 'blog.views.doputfile', name='putfile'),
	url(r'^script/', 'blog.views.script', name = 'script'),
	url(r'^refresh/', 'blog.views.dorefresh', name='refresh'),
	
#ngetes ngetes saja	
	url(r'^deletescript/', 'blog.views.deletescript', name='deletescript'),
	url(r'^createscript/', 'blog.views.createscript', name='createscript'),
	url(r'^loginnih/', 'blog.views.login', name ='loginnih'),
	url(r'^logincheck/', 'blog.views.logincheck', name='logincheck'),
	#url(r'^siapaa/','blog.views.siapaa', name='siapaa'),
	url(r'^initscript/','blog.views.initscript', name='initscript'),
	url(r'^tesuseragent/', 'blog.views.tesuseragent', name='tesuseragent'),
	url(r'^logout/', 'blog.views.logout', name ='logout'),
	url(r'^registrationhandle/', 'blog.views.registrationhandle', name='registrationhandle'),
	url(r'^register/', 'blog.views.registration', name='register'),
	url(r'^submit_setting/', 'blog.views.submit_setting', name='submit_setting'),
	url(r'^dorevert/', 'blog.views.revert', name='dorevert'),
	url(r'^customcommand/', 'blog.views.customcommand', name='customcommand'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
