#!/usr/bin/python

#recode tak jotos cok

#bjnXploit

import os, httplib

def banner():
    print '''

      ____________________________________
      |     			         |
      |     D E S T R O Y   S Q U A D    |
      |__________________________________|
          |                         |
         _| Indonesian Admin finder |_ 
     	|  https://destroy-squad.ga   |
        |     .coded by Crusher.      | 
        |_____________________________|
         '''

admpagelist = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','/redaktur','adminweb','administratorlogin.php','administrator/','redakturweb/','adminweb/index.php','adminsekolah/','webmaster','operator','moderator','sika','redaktur/index.php','login@web','ketua',
'dinkesadmin','retel','reaksi','cp-admin','master','master/index.php','master/login.php','operator/index.php','sika/index.php','develop/index.php','ketua/index.php','redaksi/index.php','operator/login.php','sika/login.php','terasadmin/index.php','terasadmin/login.php','rahasia/','rahasia/index.php','rahasia/admin.php',
'rahasia/login.php','dinkesadmin/','adminpmb/','adminpmb/index.php','system/','adminkec/','adminkec/index.php','adminkec/login.php','admindesa/','admindesa/index.php','admindesa/login.php','adminkota/','adminkota/index.php','adminkota/login.php','admin123/','admin123/index.php','portaladmin/',]
try:
    banner()
    user = raw_input('Website : ')
    site = user.replace('http://','')
    conn = httplib.HTTPConnection(site)
    conn.connect()
    print '\n Loaded %s admin-pages \n' %str(len(admpagelist))
except:
    print '\n Invalid URL / Offline Server \n'
    raw_input('Press enter to exit ')
    exit()
for adminpage in admpagelist:
    try:
        adminpage.replace('/','')
        adminpage = '/%s' %adminpage
        host = site+adminpage
        print '> Checking --- %s' %host
        conn = httplib.HTTPConnection(site)
        request = conn.request('GET',adminpage)
        response = conn.getresponse()
        if response.status == 200:
            print '\n\tPage found --- %s\n' %host
            raw_input('Press enter to continue scanning ... ')
        else:
            pass
    except:
        print 'Error Occured!'
        raw_input('Press enter to exit ')
        exit()
raw_input('\nPress enter to exit ... ')
