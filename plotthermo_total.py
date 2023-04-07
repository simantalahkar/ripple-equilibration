import numpy as np
from numpy import polyfit
import matplotlib.pyplot as plt
import matplotlib as mpl

#mpl.rcParams['mathtext.default'] = 'regular'
mpl.rcParams['mathtext.fontset'] = 'stixsans'
mpl.rcParams['mathtext.default'] = 'it'
mpl.rcParams['font.family'] = 'sans serif'
mpl.rcParams['font.size'] = 11
mpl.rcParams['legend.fontsize'] = 'medium'		#relative size to font.size
mpl.rcParams['figure.titlesize'] = 'medium'     #relative size to font.size

##################################################################################################

#####################################
f1 = open("hBN_thermoeqlbm_prec1.def0.txt","r")

for _ in range(1):
	next(f1)
	
etotal=[]
pe=[]

pressure=[]

step=[]
dts=50
i=0
for line in f1:
	c = line.split(" ")
	c1 = np.array(c[:])
	n1 = c1.astype(np.float)
	
#	if n1[5] > 0.65:
#		break
	
	etotal.append(n1[3])
	pe.append(n1[4])

	pressure.append(n1[7]/10000)
#	steps.append(n1[12])
	
	step.append(i*50)
	i=i+1	
laststep=step[-1]	
laststep1=step[-1]	
###############################
f2 = open("hBN_thermo_c1.def0.txt","r")

for _ in range(1):
	next(f2)
	

dts=50
j=0
for line in f2:
	c = line.split(" ")
	c1 = np.array(c[:])
	n1 = c1.astype(np.float)
	
#	if n1[5] > 0.65:
#		break
	
	etotal.append(n1[3])
	pe.append(n1[4])

	pressure.append(n1[7]/10000)
#	steps.append(n1[12])

	step.append(laststep+n1[9])
	j=j+1
	if n1[9]==2500:
		break
laststep=step[-1]
laststep2=step[-1]	
######################
f3 = open("hBN_thermoeqlbm_postc1.def0.txt","r")

for _ in range(1):
	next(f3)
	

dts=50
j=0
for line in f3:
	c = line.split(" ")
	c1 = np.array(c[:])
	n1 = c1.astype(np.float)
	
#	if n1[5] > 0.65:
#		break
	
	etotal.append(n1[3])
	pe.append(n1[4])

	pressure.append(n1[7]/10000)
#	steps.append(n1[12])

	step.append(laststep+n1[12])
	j=j+1	
laststep=step[-1]
laststep3=step[-1]	


###########################
f4 = open("hBN_thermoeqlbm_prec2.def0.txt","r")

for _ in range(1):
	next(f4)
	

dts=50
j=0
for line in f4:
	c = line.split(" ")
	c1 = np.array(c[:])
	n1 = c1.astype(np.float)
	
#	if n1[5] > 0.65:
#		break
	
	etotal.append(n1[3])
	pe.append(n1[4])

	pressure.append(n1[7]/10000)
#	steps.append(n1[12])
		
	step.append(laststep+j*50)
	j=j+1
laststep=step[-1]
laststep4=step[-1]	


############################
f5 = open("hBN_thermo_c2.def0.txt","r")

for _ in range(1):
	next(f5)
	

dts=50
j=0
for line in f5:
	c = line.split(" ")
	c1 = np.array(c[:])
	n1 = c1.astype(np.float)
	
#	if n1[5] > 0.65:
#		break
	
	etotal.append(n1[3])
	pe.append(n1[4])

	pressure.append(n1[7]/10000)
#	steps.append(n1[12])

	step.append(laststep+n1[9])
	j=j+1	
	if n1[9]==1500:
		break
laststep=step[-1]
laststep5=step[-1]	


###########################
f6 = open("hBN_thermoeqlbm_finaleqlbm.def0.txt","r")

for _ in range(1):
	next(f6)
	

dts=50
j=0
for line in f6:
	c = line.split(" ")
	c1 = np.array(c[:])
	n1 = c1.astype(np.float)
	
#	if n1[5] > 0.65:
#		break
	
	etotal.append(n1[3])
	pe.append(n1[4])

	pressure.append(n1[7]/10000)
#	steps.append(n1[12])

	step.append(laststep+n1[12])
	j=j+1	
laststep=step[-1]
laststep6=step[-1]	

######################### PLOT ######################	############################
###########################################################################################################
#fig = plt.figure(figsize=(13.28,21.36))
fig, axs = plt.subplots(2, 1, sharex=True, figsize=(9,9))
fig.subplots_adjust(hspace=0)

#axes1 = fig.add_subplot(231, aspect='auto', adjustable='datalim')

axs[0].plot(step,pressure,color='black', linestyle='-',
  label="Hydrostatic pressure")
axs[1].plot(step,pe,color='black', linestyle='-',
  label="Total potential energy")
#axes1.plot(steps,ly,color='blue', linestyle='-',
#  label="ly")
#axes1.plot(steps,lz,color='green', linestyle='-', 
# label="lz")



axs[1].set_xlabel('Time-step', fontsize = 14)
axs[0].set_ylabel('Pressure (GPa)', fontsize = 14)
axs[1].set_ylabel('Potential energy (eV)',fontsize = 14)
#axes.set_title(r'$[26\overline{1}]$')
#axes.set_title(r'$[26\bar{1}]$')
#axes1.set_title('dimensions')
#axes.set_title(r'NVT-Tensile test $[261]$')

axs[0].axhline(y=0,xmin=0.05,linewidth=1, linestyle=':', color='black')
axs[0].axvspan(0, laststep1, facecolor='orange')
axs[1].axvspan(0, laststep1, facecolor='orange')
axs[0].axvspan(laststep1, laststep2, facecolor='silver')
axs[1].axvspan(laststep1, laststep2, facecolor='silver')
axs[0].axvspan(laststep2, laststep3, facecolor='yellow')
axs[1].axvspan(laststep2, laststep3, facecolor='yellow')
axs[0].axvspan(laststep3, laststep4, facecolor='palegreen')
axs[1].axvspan(laststep3, laststep4, facecolor='palegreen')
axs[0].axvspan(laststep4, laststep5, facecolor='cyan')
axs[1].axvspan(laststep4, laststep5, facecolor='cyan')
axs[0].axvspan(laststep5, laststep6, facecolor='pink')
axs[1].axvspan(laststep5, laststep6, facecolor='pink')

axs[0].legend(loc=1,fontsize = 14)

axs[1].legend(loc=1,fontsize = 14)

plt.ticklabel_format(style='sci', axis='y', scilimits=(-2,2))

plt.show()
fig.savefig('hBN_thermo_total.pdf', bbox_inches='tight')
fig.savefig('hBN_thermo_total.png', bbox_inches='tight')
plt.close(fig)
