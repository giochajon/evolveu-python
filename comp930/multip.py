


#input
mp = "MULTIPOLYGON (((-114.012893904272 50.932651737422, -114.012546652848 50.931563820252, -114.01178251753 50.929169436405, -114.010856984073 50.926269022016, -114.012802874462 50.921173715604, -114.012712288543 50.921024813696, -114.01343916774 50.920787464815, -114.014109426626 50.920527531066, -114.014782965323 50.920277987196, -114.015204403922 50.920706354268, -114.015390436545 50.920839834777, -114.015603984641 50.920949212922, -114.015826039614 50.921014379769, -114.016011154403 50.92106315544, -114.016228832778 50.921116263934, -114.016455082811 50.921174792638, -114.016686476004 50.921232235983, -114.016861309969 50.921286431799, -114.016941154791 50.921315328242, -114.017104038734 50.92141842432, -114.017286529152 50.921539214832, -114.017889904252 50.921946564363, -114.018035136845 50.922044614891, -114.018170490034 50.921994970432, -114.020817403187 50.921227580183, -114.021258638538 50.921227923214, -114.021850026782 50.920884060013, -114.02342424592 50.921875000946, -114.024458540498 50.922557669717, -114.025728645626 50.92345087632, -114.027309905086 50.924630893713, -114.02838577101 50.925507723255, -114.029189501932 50.926237063192, -114.029734025573 50.926802522795, -114.030146295461 50.927271326587, -114.030692762369 50.927971801538, -114.031048437664 50.928506348462, -114.031365690983 50.92901660305, -114.031634925269 50.929514718086, -114.031884953861 50.930006762322, -114.032106205767 50.930541342465, -114.032326126152 50.931148665258, -114.031375323838 50.931274249307, -114.02813778871 50.931767998135, -114.027760195124 50.931808742667, -114.027382594909 50.931839321989, -114.027133527628 50.931839380124, -114.023019876602 50.931784364219, -114.019827517892 50.931735424465, -114.019276604302 50.931756014592, -114.018817521958 50.931800499614, -114.01833684023 50.931865484114, -114.0174193968 50.932032096981, -114.012963332292 50.932869233328, -114.012911927589 50.932708205528, -114.01289505618 50.93265534854, -114.012893904272 50.932651737422)))"


# expected result {lat: 37.772, lng: -122.214},...
def multip2google (multipoligon):
# filter one only values in parenthesis
	f1 = mp[mp.find("(((")+3:mp.find(")))")]

# filter 2 put them in an array 
	f2 = f1.split(", ")

	f3=[]
	for elements in f2:
		a = elements 
		b=a.split(' ')
		c= "{lat:"+b[1]+", lng:"+b[0]+"}," 
		f3.append (c)  

	f4 = ""

	for elementos in f3:
		f4 = f4+ elementos
	f4 = f4[0:-1] # remove last comma

	return f4 


gm = "{lat:50.932651737422, lng:-114.012893904272},{lat:50.931563820252, lng:-114.012546652848},{lat:50.929169436405, lng:-114.01178251753},{lat:50.926269022016, lng:-114.010856984073},{lat:50.921173715604, lng:-114.012802874462},{lat:50.921024813696, lng:-114.012712288543},{lat:50.920787464815, lng:-114.01343916774},{lat:50.920527531066, lng:-114.014109426626},{lat:50.920277987196, lng:-114.014782965323},{lat:50.920706354268, lng:-114.015204403922},{lat:50.920839834777, lng:-114.015390436545},{lat:50.920949212922, lng:-114.015603984641},{lat:50.921014379769, lng:-114.015826039614},{lat:50.92106315544, lng:-114.016011154403},{lat:50.921116263934, lng:-114.016228832778},{lat:50.921174792638, lng:-114.016455082811},{lat:50.921232235983, lng:-114.016686476004},{lat:50.921286431799, lng:-114.016861309969},{lat:50.921315328242, lng:-114.016941154791},{lat:50.92141842432, lng:-114.017104038734},{lat:50.921539214832, lng:-114.017286529152},{lat:50.921946564363, lng:-114.017889904252},{lat:50.922044614891, lng:-114.018035136845},{lat:50.921994970432, lng:-114.018170490034},{lat:50.921227580183, lng:-114.020817403187},{lat:50.921227923214, lng:-114.021258638538},{lat:50.920884060013, lng:-114.021850026782},{lat:50.921875000946, lng:-114.02342424592},{lat:50.922557669717, lng:-114.024458540498},{lat:50.92345087632, lng:-114.025728645626},{lat:50.924630893713, lng:-114.027309905086},{lat:50.925507723255, lng:-114.02838577101},{lat:50.926237063192, lng:-114.029189501932},{lat:50.926802522795, lng:-114.029734025573},{lat:50.927271326587, lng:-114.030146295461},{lat:50.927971801538, lng:-114.030692762369},{lat:50.928506348462, lng:-114.031048437664},{lat:50.92901660305, lng:-114.031365690983},{lat:50.929514718086, lng:-114.031634925269},{lat:50.930006762322, lng:-114.031884953861},{lat:50.930541342465, lng:-114.032106205767},{lat:50.931148665258, lng:-114.032326126152},{lat:50.931274249307, lng:-114.031375323838},{lat:50.931767998135, lng:-114.02813778871},{lat:50.931808742667, lng:-114.027760195124},{lat:50.931839321989, lng:-114.027382594909},{lat:50.931839380124, lng:-114.027133527628},{lat:50.931784364219, lng:-114.023019876602},{lat:50.931735424465, lng:-114.019827517892},{lat:50.931756014592, lng:-114.019276604302},{lat:50.931800499614, lng:-114.018817521958},{lat:50.931865484114, lng:-114.01833684023},{lat:50.932032096981, lng:-114.0174193968},{lat:50.932869233328, lng:-114.012963332292},{lat:50.932708205528, lng:-114.012911927589},{lat:50.93265534854, lng:-114.01289505618},{lat:50.932651737422, lng:-114.012893904272}"

def getcenter(googmulti):
	f1 = googmulti
	f2 = f1.replace("},{", "")
	f3 = f2.replace("lat:", " ")
	f4 = f3.replace("lng:"," ")
	f5 = f4[1:-1]
	f6 = f5.replace (",","")
	f7 = f6.replace (",","")
	f8 = f7.split()
 	

	c = 0
	latavg = 0
	lngavg = 0
	for elemento in f8:

		c = c+1 
		if (c%2==0):
			latavg = latavg+ float(elemento)	
		else:
			lngavg  = lngavg + float(elemento)

	latavg =(latavg /(c/2))
	lngavg =(lngavg /(c/2))
	return ("{lat:"+str(lngavg)+", lng:"+str(latavg)+"}")


#print(getcenter (multip2google (mp)))



