# -*- coding: UTF-8 -*-
#---------------------------------------------------------------------
# File: tvvn.py
# By:   Binh Nguyen <binh@vnoss.org>
# Date: 25-03-2012
#---------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#---------------------------------------------------------------------

import os, re, sys, urllib, urllib2, xbmcaddon, xbmcplugin, xbmcgui

addon = xbmcaddon.Addon('plugin.video.tvvn')
profile = xbmc.translatePath(addon.getAddonInfo('profile'))
mysettings = xbmcaddon.Addon(id='plugin.video.tvvn')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))

#---------------------------------------------------------------------
# CONFIGURATION STARTS
#---------------------------------------------------------------------
# src_name = [stream url, swf player url, referrer url]

# vtc.com.vn
# See here for more IP's http://www.vtc.com.vn/XMLStart.aspx
VTCURLList=['rtmp://66.160.142.201/live',
			'rtmp://66.160.142.198/live',
			'rtmp://66.160.142.197/live']
from random import choice
VTCURL=choice(VTCURLList)

src_vtc =  [VTCURL,
			'http://vtc.com.vn/player.swf',
			'http://vtc.com.vn/#']

# tv24.vn
TV24URLList=['rtmp://112.197.2.16/live',
			 'rtmp://112.197.2.11/live']
TV24URL=choice(TV24URLList)
src_tv24=  [TV24URL,
			'http://tv24.vn/jwplayer/player.swf',
			'http://www.tv24.vn']

# xunghe.vn
src_trt  =  ['rtmp://118.69.176.149/live/',
			'http://tv.xunghe.vn/player.swf',
			'http://tv.xunghe.vn/?tab=Truyen-Hinh&xem=trt1-hue']

#---------------------------------------------------------------------
# CONFIGURATION ENDS
#---------------------------------------------------------------------

mode=None

def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]=splitparams[1]
							
	return param

params=get_params()

try:
	stream_name=urllib.unquote_plus(params["stream_name"])
except:
	pass
try:
	ref=urllib.unquote_plus(params["ref"])
except:
	pass
try:
	src=urllib.unquote_plus(params["src"])
except:
	pass
try:
	mode=int(params["mode"])
except:
	pass

def add_link(name,src,stream_name,ref,iconimage):
	ok = True
	give_url = sys.argv[0]+"?mode=1&stream_name="+stream_name+"&ref="+ref+"&src="+src
	liz = xbmcgui.ListItem( name, iconImage=xbmc.translatePath(os.path.join(home, iconimage)), thumbnailImage=xbmc.translatePath(os.path.join(home, iconimage)))
	liz.setInfo(type="Video", infoLabels={"Title": name})
	liz.setProperty("Fanart_Image",fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=give_url,listitem=liz)

def add_directory_link(name, lmode, iconimage):
	li = xbmcgui.ListItem( name, iconImage=xbmc.translatePath(os.path.join(home, iconimage)), thumbnailImage=xbmc.translatePath(os.path.join(home, iconimage)))
	li.setInfo(type="Video", infoLabels={"Title": name})
	li.setProperty("Fanart_Image",fanart)
	url = sys.argv[0]+'?mode='+lmode
	return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)

def show_menu_sctv():
	add_link('SCTV 1', 'src_tv24',  'sctv1.stream',  '',   'sctv.png')
	add_link('SCTV 2', 'src_tv24',  'sctv2.stream',  '',   'sctv.png')
	add_link('SCTV 3', 'src_tv24',  'sctv3.stream',  '',   'sctv.png')
	add_link('SCTV 4', 'src_tv24',  'sctv4.stream',  '',   'sctv.png')
	add_link('SCTV 5', 'src_tv24',  'sctv5.stream',  '',   'sctv.png')
	add_link('SCTV 6', 'src_tv24',  'sctv6.stream',  '',   'sctv.png')
	add_link('SCTV 7', 'src_tv24',  'sctv7.stream',  '',   'sctv.png')
	add_link('SCTV 8', 'src_tv24',  'sctv8.stream',  '',   'sctv.png')
	add_link('SCTV 9', 'src_tv24',  'sctv9.stream',  '',   'sctv.png')
	add_link('SCTV 10', 'src_tv24',  'sctv10.stream',  '',   'sctv.png')
	add_link('SCTV 11', 'src_tv24',  'sctv11.stream',  '',   'sctv.png')
	add_link('SCTV 12', 'src_tv24',  'sctv12.stream',  '',   'sctv.png')
	add_link('SCTV 13', 'src_tv24',  'sctv13.stream',  '',   'sctv.png')
	add_link('SCTV 14', 'src_tv24',  'sctv14.stream',  '',   'sctv.png')
	add_link('SCTV 15', 'src_tv24',  'sctv15.stream',  '',   'sctv.png')
	add_link('SCTV 16', 'src_tv24',  'sctv16.stream',  '',   'sctv.png')
	add_link('SCTV 17', 'src_tv24',  'sctv17.stream',  '',   'sctv.png')
	add_link('SCTV HD', 'src_tv24',  'sctv18.stream',  '',   'sctv.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def show_menu_local():
	add_link('Hà Nội', 'src_tv24',  'hn1.stream',  '',   '.png')
	add_link('Thừa Thiên Huế', 'src_trt',  'trt',  '',   '.png')
	add_link('HTV 7', 'src_vtc',  'htv7',   '',  'htv7.png')
	add_link('HTV 9', 'src_vtc',  'htv91',  '',   'htv9.png')
	add_link('Long An', 'src_tv24',  'la34.stream',  '',   '.png')
	add_link('Vĩnh Long', 'src_tv24',  'thvl1.stream',  '',   '.png')
	add_link('Đồng Nai', 'src_tv24',  'dn1.stream',  '',   '.png')
	add_link('Hậu Giang', 'src_tv24',  'thhg.stream',  '',   '.png')
	add_link('Sóc Trăng', 'src_tv24',  'thst.stream',  '',   '.png')
	add_link('Tiền Giang', 'src_tv24',  'thtg.stream',  '',   '.png')
	add_link('Quảng Nam', 'src_tv24',  'qrt.stream',  '',   '.png')
	add_link('Bình Thuận', 'src_tv24',  'bthtv.stream',  '',   '.png')
	add_link('Đồng Tháp', 'src_tv24',  'thdt.stream',  '',   '.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def show_menu_vov():
	add_link('VOV 1', 'src_vtc',  'vov1',   'VOV1/29',  'vov1.png')
	add_link('VOV 2', 'src_vtc',  'vov2',   'VOV2/28',  'vov2.png')
	add_link('VOV 3', 'src_vtc',  'vov3',   'VOV3/27',  'vov3.png')
	add_link('VOV 5', 'src_vtc',  'vov5',   'VOV5/25',  'vov5.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Init():
	add_link('VTV 1', 'src_vtc',  'vtv11',  'VTV1/15',  'vtv1.png')
	add_link('VTV 2', 'src_vtc',  'vtv2',   'VTV2/23',  'vtv2.png')
	add_link('VTV 3', 'src_vtc',  'vtv31',  'VTV3/3',   'vtv3.png')
	add_link('VTV 4', 'src_vtc',  'vtv4',   'VTV4/2',   'vtv4.png')
	add_link('VTV 6', 'src_tv24',  'vtv6.stream',   '',   'vtv6.png')
	add_link('VTV 9', 'src_tv24',  'vtv9.stream',   '',   'vtv9.png')
	add_link('ANTV',  'src_tv24',  'antv.stream',   'antv.html',   'antv.png')
	add_link('VTC 1', 'src_vtc',  'vtc11',  'VTC1/10',  'vtc1.png')
	add_link('VTC 2', 'src_vtc',  'vtc21',  'VTC2/11',  'vtc2.png')
	add_link('VTC 10', 'src_vtc', 'vtc101', 'VTC10/22', 'vtc10.png')
	add_directory_link('SCTV Channels', '10', 'sctv.png')
	add_directory_link('Local Stations', '12', 'vov.png')
	add_directory_link('VOV Radio Stations', '11', 'vov.png')

	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def play_video(src, stream_name, ref):
	prov=globals()[src]
	item = xbmcgui.ListItem("TVVN")

	pageUrl=prov[2]+"/"+ref
	videoUrl=prov[0]+"/"+stream_name
	swfUrl=prov[1]
	flashVer="LNX11,2,202,233"

	fullURL=videoUrl+' swfVfy=1 live=1 playpath='+stream_name+' flashVer='+flashVer+' app=live pageUrl='+pageUrl+'/ tcUrl='+videoUrl+' swfUrl='+swfUrl 
	xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(fullURL, item)

if mode==None:
	Init()
elif mode==1:
	play_video(src, stream_name, ref)
elif mode==10:
	show_menu_sctv()
elif mode==11:
	show_menu_vov()
elif mode==12:
	show_menu_local()
