from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.template import Template, Context
from django.shortcuts import get_object_or_404, render
from blog.models import Blog
from django.core.files import File
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from fabric.api import execute
#from fabfile import *
import io
import os
import datetime
# Create your views here.
#################################################
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
import socket
i = 3
a = ''
pather =''
from django.contrib.auth.models import User
from django.contrib import auth

#user = User.objects.create_user(username = 'admintes', password='admin')
#user.is_staff = True
#user.save()

def home(request):
	return TemplateResponse(request, "index.html")
def blog(request, slug):
	blog = get_object_or_404(Blog, slug=slug)
	return TemplateResponse(request,"blog.html",{'blog' : blog})
	
#deployment tool - toolnya
def createfile(request):
	if request.method == 'POST':
		param_a = request.POST['namafile']
		if(param_a != ''):
			#with open('D:/FilePKl/latihan_django/11agustus/djangoproj/djangoapp/execute.py', 'r') as file:
			with open('temp/'+request.session['name']+ '_execute.py', 'r') as file : 	
				data = file.readlines()
			data[request.session['counter']] = ("execute (touchfile, '"+param_a+"' , '"+request.session['name']+"')\n ")
			#with open('D:/FilePKl/latihan_django/11agustus/djangoproj/djangoapp/execute.py', 'w') as file:
			with open('temp/'+request.session['name']+ '_execute.py', 'w') as file	:
				file.writelines(data)
			file.close()
			#return TemplateResponse(request, "index.html")
			#return TemplateResponse (request, "execute.html")
			return HttpResponseRedirect("/")
		else:
			return HttpResponse ("masukkan inputannya!!")
def copy(request):
	if request.method == 'POST':
		param_a = request.POST['location']
		param_b = request.POST['destination']
		if (param_a != '') and (param_b != ''):
			with open('temp/'+request.session['name']+ '_execute.py', 'r') as file:
				data = file.readlines()
			data[request.session['counter']] = ("execute (copy, '"+param_a+"', '"+param_b+"' , '"+request.session['name']+"')\n ")
			with open('temp/'+request.session['name']+ '_execute.py', 'w') as file:
				file.writelines(data)
			file.close()
			#return TemplateResponse (request,"index.html")
			return HttpResponseRedirect("/")
		else:
			return HttpResponse ("masukkan inputannya!!")
def deletedir(request):
	if request.method == 'POST':
		param_a = request.POST['namadir']
		if(param_a != ''):
			with open('temp/'+request.session['name']+ '_execute.py', 'r') as file:
				data = file.readlines()
			data[request.session['counter']] = ("execute (deldir, '"+param_a+"' , '"+request.session['name']+"')\n ")
			with open('temp/'+request.session['name']+ '_execute.py', 'w') as file:
				file.writelines(data)
			file.close()
			#return TemplateResponse (request, "index.html")
			return HttpResponseRedirect("/")
		else:
			return HttpResponse ("masukkan inputannya!!")
def deletefile(request):
	if request.method == "POST":
		param_a =  request.POST['namafile']
		if(param_a != ''):
			with open('temp/'+request.session['name']+ '_execute.py', 'r') as file:
				data = file.readlines()
			data[request.session['counter']] = ("execute (removefile, '"+param_a+"' , '"+request.session['name']+"')\n ")
			with open('temp/'+request.session['name']+ '_execute.py', 'w') as file:
				file.writelines(data)
			file.close()
			#return TemplateResponse (request, "index.html")
			return HttpResponseRedirect("/")
		else:
			return HttpResponse ("masukkan inputannya!!")
def makedir(request):
	if request.method == 'POST':
		param_a = request.POST['namadir']
		if(param_a != ''):
			with open('temp/'+request.session['name']+ '_execute.py', 'r') as file:
				data = file.readlines()
			data[request.session['counter']] = ("execute (mkdir, '"+param_a+"' , '"+request.session['name']+"')\n ")
			with open('temp/'+request.session['name']+ '_execute.py', 'w') as file:
				file.writelines(data)
			file.close()
			#return TemplateResponse (request,"index.html")
			return HttpResponseRedirect("/")
		else:
			return HttpResponse ("masukkan inputannya!!")
def doputfile(request):
	if request.method == 'POST':
		param_a = request.POST['namadokumen']
		param_b = request.POST['destination']
		if(param_a != ''):
			with open('temp/'+request.session['name']+ '_execute.py', 'r') as file:
				data = file.readlines()
			data[request.session['counter']] = ("execute (putfile, '"+param_a+"', '"+param_b+"' , '"+request.session['name']+"')\n ")
			with open('temp/'+request.session['name']+ '_execute.py', 'w') as file:
				file.writelines(data)
			file.close()
			#return TemplateResponse (request,"index.html")
			return HttpResponseRedirect("/")
		else:
			return HttpResponse ("masukkan inputannya!!")



def add(request):
	try:
		request.session['counter']=request.session['counter']+1
	#return TemplateResponse (request, "index.html")
		return HttpResponseRedirect("/")
	except IndexError:
		return HttpResponse("index error coy")
def execpy(request):
	try:
		execfile('blog/dobackup.py')
		execfile('temp/'+request.session['name']+ '_execute.py')
		refreshscript(request)
		#return HttpResponse ("perintah berhasil dilaksanakan")
	except:
		execfile('blog/dodelproject.py')
		execfile('blog/docopyfromtemp.py')
		#execfile('blog/dodelbackup.py')
		refreshscript(request)
		return HttpResponse ("gagal melakukan perintah")
	else:
		#execfile('blog/dodelbackup.py')
		return HttpResponse ("perintah berhasil dilaksanakan")
def revert(request):
	execfile ('blog/dodelproject.py')
	execfile ('blog/docopyfromtemp.py')
	return HttpResponse ()
def dorefresh(request):
	refreshscript(request)
	#return TemplateResponse (request, "index.html")
	return HttpResponseRedirect("/home/")
def script(request):
	try:
		fp = open('temp/'+request.session['name']+ '_execute.py')
		return HttpResponse(fp, content_type="text/plain")
	except KeyError:
		return HttpResponse("Script does not exist")

#khusus untuk execute -------------------------------------	
def refresh(request):
	request.session['counter'] = 3
def refreshscript(request):
	refresh(request)
	with open ('temp/'+request.session['name']+ '_execute.py', 'r') as file:
		lines = file.readlines()
	lines[request.session['counter']] = ''
	with open ('temp/'+request.session['name']+ '_execute.py', 'w') as file:
		while(request.session['counter'] > 3):
			file.writelines(lines)
			request.session['counter']=request.session['counter']-1
		file.writelines("from fabric.api import execute\nfrom fabfile import *\nexecute (preset, '%(host)s','%(pass)s','%(basedir)s','%(domain)s','%(baselocal)s')\n\n" % {'host': request.session['setting_env.host'], 'pass':request.session['setting_env.password'], 'basedir':request.session['setting_env.base_dir'], 'domain':request.session['setting_env.domain'], 'baselocal':request.session['setting_env.base_local']})
	file.close()
# sampai sini --------------------------------------------------
#def exemkdir(request):
#	execute(mkdir)
#baris untuk ngetes ngetes
def createscript(request):
	open('temp/'+request.session['name']+ '_execute.py', 'w')#terpakai
def initscript(request):
	createscript(request)
	refresh(request)
	with open ('temp/'+request.session['name']+ '_execute.py', 'r') as file:
		lines = file.readlines()
	with open ('temp/'+request.session['name']+ '_execute.py', 'w') as file:
		file.writelines("from fabric.api import execute\nfrom fabfile import *\nexecute (preset, '%(host)s','%(pass)s','%(basedir)s','%(domain)s','%(baselocal)s')\n\n" % {'host': request.session['setting_env.host'], 'pass':request.session['setting_env.password'], 'basedir':request.session['setting_env.base_dir'], 'domain':request.session['setting_env.domain'], 'baselocal':request.session['setting_env.base_local']})
	file.close()#terpakai

def deletescript(request):
	namauser = request.session['name']
	os.remove ('temp/'+request.session['name']+ '_execute.py')
	
#def logincheck(request):
#	request.session['name'] = request.POST['namex']
#	request.session['password'] = request.POST['passwordx']
#	request.session['counter']= 3
	#if (request.session['name'] == user.username)and (request.session['password']== user.password) :
	#if (request.session['name'] == 'irfan'):
#		initscript(request)
#		return HttpResponseRedirect("/home/")
#	elif(request.session['name'] == "") :
#		return HttpResponse ('harus diisi!')
#	else:
#		return HttpResponse ('anda bukan user terdaftar')
def logincheck(request):
	request.session['name'] = request.POST['namex']
	request.session['password'] = request.POST['passwordx']
	request.session['counter']= 3
	user=auth.authenticate(username=request.session['name'], password=request.session['password'])
	if user is not None and user.is_staff:
	#if (request.session['name'] == 'irfan'):
		#initscript(request)
		#return HttpResponseRedirect("/home/")
		return TemplateResponse (request, "setting.html")
	elif(request.session['name'] == "")and (request.session['password'] =="") :
		return HttpResponse ('harus diisi!')
	else:
		return HttpResponse ('anda bukan user terdaftar atau user aktif')
def login (request):
	return TemplateResponse (request, "login.html")
def logout(request):
	deletescript(request)
	request.session.clear()
	return HttpResponseRedirect('/')
def tesuseragent(request):
	global pather
	q = request.session['name']
	if ( request.META.get('HTTP_USER_AGENT').find ("Linux")!= -1):
		pather = '/'
	elif ( request.META.get('HTTP_USER_AGENT').find ("Windows")!= -1):
		pather = '\\'
	return HttpResponse(pather)
#coba coba register---------------------------------
def registration(request):
	return TemplateResponse (request, "register.html")
def registrationhandle(request):
	if(request.POST['username'] != "") and(request.POST['email'] != "")and (request.POST['password'] != ""):
		try:
			user = User.objects.create_user(username = request.POST['username'],email = request.POST['email'], password = request.POST['password'])
		#usercheck = auth.authenticate(username=request.POST['username'])
		#if usercheck is None:
			user.save()
			return HttpResponseRedirect("/")
		except:
			return HttpResponse("username telah terdaftar")
	else:
		return HttpResponse("masukkan inputannya")
#coba coba setting luar--------------------	
def submit_setting(request):
	request.session['setting_env.host'] = request.POST['env.host']
	request.session['setting_env.password'] = request.POST['env.password']
	request.session['setting_env.base_dir'] = request.POST['base_dir']
	request.session['setting_env.domain'] = request.POST ['domain']
	request.session['setting_env.base_local'] = request.POST ['base_local']
#	initsettingfile(request)
	initscript(request)
	return HttpResponseRedirect ('/home')
def customcommand(request):
	if request.method == 'POST':
		param_a = request.POST['perintahnya']
		if(param_a != ''):
			with open('temp/'+request.session['name']+ '_execute.py', 'r') as file:
				data = file.readlines()
			data[request.session['counter']] = ("execute (docommand, '"+param_a+"' , '"+request.session['name']+"')\n ")
			with open('temp/'+request.session['name']+ '_execute.py', 'w') as file:
				file.writelines(data)
			file.close()
			#return TemplateResponse (request,"index.html")
			return HttpResponseRedirect("/")
		else:
			return HttpResponse ("masukkan inputannya!!")
