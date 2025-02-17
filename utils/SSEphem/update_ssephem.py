import os
import numpy as np

def LeapSecUpdate():
	os.system('wget https://raw.githubusercontent.com/astropy/astropy/main/astropy/utils/iers/data/Leap_Second.dat')
	if os.access('leapsec.tab', os.F_OK):
		os.system('mv leapsec.tab leapsec_old.tab')
	try:
		f = open('Leap_Second.dat','r')
		lines = f.readlines()
		fo = open('leapsec.tab','w')
		for line in lines:
			if not line.startswith("#"):
				cos = line.split()
				if cos[2] == '1':
					date = cos[3]+' January 1 '
				else:
					date = cos[3]+' July 1  '
				jd = float(cos[0])
				leap = float(cos[4])
				leap = int(np.around(leap))
				nline = '    '+str(int(np.around(jd)))+'       '+date+'TAI-UTC = '+str(leap)+'.0\n'
				fo.write(nline)
		f.close()
		fo.close()
		os.system('rm Leap_Second.dat')
	except:
		print 'No luck...'
		os.system('rm Leap_Second.dat')
		os.system('mv leapsec_old.tab leapsec.tab')

def SSEphemDownload():
	if os.access('DEc403',os.F_OK):
		os.system('mv DEc403 DEc403_old')
	if os.access('ascp2000.403', os.F_OK):
		os.system('mv ascp2000.403 ascp2000_old.403')
	os.system('wget ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de403/ascp2000.403')
	if os.access('header.403', os.F_OK):
		os.system('mv header.403 header_old.403')
	os.system('wget ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de403/header.403')
	if os.access('ascp2000.403', os.F_OK) == False or os.access('header.403', os.F_OK) == False:
		print 'No Luck...'
		os.system('mv ascp2000_old.403 ascp2000.403')
		os.system('mv header_old.403 header.403')
	else:
		os.system('cat header.403 ascp2000.403 > asc_cat.403')
		os.system('./asc2bin asc_cat.403 2451544 2484394')
	if os.access('DEc403',os.F_OK) == False:
		print 'No Luck...'
		if os.access('DEc403_old',os.F_OK):
			os.system('mv DEc403_old DEc403')

def IersUpdate():
	if os.access('finals2000A.data',os.F_OK):
		os.system('mv finals2000A.data finals2000A_old.data')
	os.system('wget https://datacenter.iers.org/data/9/finals2000A.all')
	#os.system('wget --no-proxy http://maia.usno.navy.mil/ser7/finals2000A.data')
	if os.access('finals2000A.data',os.F_OK) == False:
		print 'one'
		print 'No Luck...'
		os.system('mv finals2000A_old.data finals2000A.data')
		pass
	else:
		if os.access('iers.tab',os.F_OK):
			os.system('mv iers.tab iers_old.tab')
		try:
			output = open('iers.tab','w')
			finaldata = open('finals2000A.all','r')
			for line in finaldata:
				mj = line[7:15]
				if len(line.split()) > 5:
					c1 = line[18:27]
					c2 = line[37:46]
					c3 = line[58:68]
					l  = ' '+mj+' '+c1+' '+c2+' '+c3+' '+'\n'
					output.write(l)
			finaldata.close()
			output.close()
		except:
			print 'two'
			print 'No Luck...'
			if os.access('iers_old.tab',os.F_OK):
				os.system('mv iers_old.tab iers.tab')
