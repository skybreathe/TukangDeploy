from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.network import disconnect_all
from fabric.context_managers import settings


import os
import shutil
import time
#--------------preset--------------
#env.hosts = ['root@192.168.0.69']
#env.password = 'rahasiakita'
#base_dir = "root"
#domain = "Ipan"
#base_domain = "/%(basedir)s/%(domain_name)s" % {'basedir': base_dir, 'domain_name':domain}
#base_local = "blog/project"
#----------------------------------
#env.hosts = ['root@192.168.0.69']
#env.password = 'rahasiakita'
#base_dir = "root"
#domain = "Ipan"
#base_local = "blog/project"
def touchfile(namafile, user):
	try:
		with cd(env.base_domain):
			run('touch '+namafile)
			cmd= user+" run touch newfile named as "+namafile+ " in "+env.base_domain
			write_log(cmd)
	except:
		cmd= user+" Failed run touch newfile "+namafile+" in "+env.base_domain+">> Do rollback"
		write_log(cmd)
		return run().failed
def copy(sourcefile, destination, user):
	try:
		run('cp '+env.base_domain+'/'+sourcefile+ ' '+env.base_domain+'/'+destination)
		cmd= user+" run copy from "+sourcefile+ " to "+env.base_domain+'/'+destination
		write_log(cmd)
	except:
		cmd= user+" Failed run copy from "+sourcefile+" in "+env.base_domain+'/'+destination+">> Do rollback"
		write_log(cmd)
		return run().failed
def deldir(namadir, user):
	try:
		with cd(env.base_domain):
			run('rm -r '+namadir)
			cmd= user+" run delete directory "+namadir+ " in "+env.base_domain
			write_log(cmd)
	except:
		cmd= user+" Failed run delete directory "+namadir+" in "+env.base_domain+">> Do rollback"
		write_log(cmd)
		return run().failed
def removefile(namafile, user):
	try:
		with cd(env.base_domain):
			run('rm '+namafile)
			cmd= user+" run remove file "+namafile+ " in "+env.base_domain
			write_log(cmd)
	except:
		cmd= user+" Failed run remove file "+namafile+" in "+env.base_domain+">> Do rollback"
		write_log(cmd)
		return run().failed		
def mkdir(namadir, user):
	try:
		with cd(env.base_domain):
			run('mkdir '+namadir)
			cmd= user+" run make directory "+namadir+" in "+env.base_domain
			write_log(cmd)
	except:
		cmd= user+" Failed run make directory "+namadir+" in "+env.base_domain+">> Do rollback"
		write_log(cmd)
		return run().failed	
def putfile(namadokumen, destination, user):
	try:
		put(env.base_local+'/'+namadokumen ,env.base_domain+'/'+destination)
		cmd= user+" upload file "+namadokumen+" to "+env.base_domain+'/'+destination
		write_log(cmd)
	except:
		cmd= user+" Failed run upload file "+namadokumen+" in "+env.base_domain+">> Do rollback"
		write_log(cmd)
		return run().failed		
def write_log(command):
	times = time.strftime("%c")
	log_write = command+' '+times+'\n'
	file = open('log/log.dj','a')
	file.write(log_write)
	file.close()
def write_errorlog():
	times = time.strftime("%c")
	log_write = 'an error has occurred, do rollback on '+times+'\n'
	file = open('log/log.dj','a')
	file.write(log_write)
	file.close()

#Alpha
def backup():
	with cd (env.base_dir):
		run ('mkdir -p temp')
		run ('cp -avr '+env.base_domain+' temp')
	
def delbackup():
	with cd (env.base_dir):
		run('rm -r temp')
def delproject():
	with cd(env.base_dir):
		run('rm -r '+env.base_domain)
def copyfromtemp():
	with cd(env.base_dir):
		with cd('temp'):
			run('cp -avr '+env.domain+' '+env.base_dir)
def preset(host, password, base_dir, domain, base_local):
	env.hosts = [host]
	env.password = password
	env.base_dir = "/%(basedir)s" % {'basedir':base_dir}
	env.domain = domain
	env.base_domain = "/%(basedir)s/%(domain_name)s" % {'basedir': base_dir, 'domain_name':domain}
	env.base_local = base_local
def list():
	preset()
	run ('ls '+env.base_domain)
def docommand(command, user):
	run (command)
	cmd= user+" do custom command: '"+command+"'"
	write_log(cmd)

#ini tahap coba coba
#def removefile (namafile, user):
#	with settings(warn_only = True): 
		#with cd(base_dir): 
		#run('rm '+namafile)
#		result=run('rm '+namafile)
#		if result.failed: 
			#cmd= user+" Success run remove file "+namafile+ " in "+base_dir
#			cmd= user+" Failed run remove file "+namadokumen+" to "+base_dir+'/'+destination 
#		else : 
			#cmd= user+" Failed run remove file "+namadokumen+" to "+base_dir+'/'+destination
#			cmd= user+" Success run remove file "+namafile++ " in "+base_dir			
#		write_log(cmd)

#def removefile (namafile, user):
#	try:
#		with cd(base_dir):
#			run('rm '+namafile)
#			cmd= user+" Success run remove file "+namafile+ " in "+base_dir
#			write_log(cmd)
#	except:
#		cmd= user+" Failed run remove file "+namafile+" in "+base_dir+">> Do rollback"
#		write_log(cmd)
#		return run().failed
			
#def removefile (namafile, user):
#	command = 
#	if run ('rm '+namafile).failed:
#		cmd =user+" Failed run remove file "+namafile
#		
#	else:
#		cmd =user+" Success run remove file "+namafile
#	write_log(cmd)	

