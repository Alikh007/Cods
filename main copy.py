#begin
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation




V_X_values=[]
V_Y_values=[]
V_Z_values=[]
newlines=[]
facelines=[]
idx=0
file = open('/Users/alikhodadadi/Desktop/readingstuff.txt','r')

All_lines=file.readlines()



textf='f'
textv= 'v'

for line in All_lines:
    if textv in line:
        newlines.insert(idx,line)
        idx+=1





for line in All_lines:
    if textf in line:
        facelines.insert(idx,line)
        idx+=1


all_faces=[]
for b in range(len(facelines)):
    all_faces.append(facelines[b][2:1000])








for i in range(len(newlines)):

    mixed_cordinates=(str(newlines[i])[2:-1])
    seperate_cordinates=mixed_cordinates.split()
    V_X_values.append(seperate_cordinates[0])
    V_Y_values.append(seperate_cordinates[1])
    V_Z_values.append(seperate_cordinates[2])



lol=[]



for i in range(len(facelines)):

    f_mixed_cordinates=(str(facelines[i])[1:10000])
    f_seperate_cordinates=f_mixed_cordinates.split()
    lol.append(f_seperate_cordinates)





lk=[]
a=0


while a<(len(facelines)):

    y = int(lol[a][0])

    y1 = int(lol[a][1])

    y2=int(lol[a][2])

    lk.append([V_X_values[y-1],V_X_values[y1-1],V_X_values[y2-1]])
    a=a+1

lineX_values=lk








a=0
lyk=[]
while a<(len(facelines)):

    y = int(lol[a][0])

    y1 = int(lol[a][1])

    y2=int(lol[a][2])

    lyk.append([V_Y_values[y-1],V_Y_values[y1-1],V_Y_values[y2-1]])
    a=a+1

lineY_values=lyk

a=0
lzk = []
while a < (len(facelines)):
    y = int(lol[a][0])
    y1 = int(lol[a][1])
    y2 = int(lol[a][2])

    lzk.append([V_Z_values[y - 1], V_Z_values[y1 - 1], V_Z_values[y2 - 1]])
    a = a + 1



###########################################################

########################so far we have x , y and z seperated and ready to plot








V_X_values=np.array(V_X_values,dtype=float)
V_Y_values=np.array(V_Y_values,dtype=float)
V_Z_values=np.array(V_Z_values,dtype=float)


fig=plt.figure()
my3dplot=fig.add_subplot(111,projection='3d')



lineX_values=lk
lineY_values=lyk
lineZ_values = lzk
ab=0
while ab<len(lineX_values):
    lineX_values[ab][0]=float(lineX_values[ab][0])
    lineX_values[ab][1]=float(lineX_values[ab][1])
    lineX_values[ab][2]=float(lineX_values[ab][2])
    ab=ab+1
ab=0
while ab<len(lineY_values):
    lineY_values[ab][0]=float(lineY_values[ab][0])
    lineY_values[ab][1]=float(lineY_values[ab][1])
    lineY_values[ab][2]=float(lineY_values[ab][2])
    ab=ab+1
ab=0
while ab<len(lineZ_values):
    lineZ_values[ab][0]=float(lineZ_values[ab][0])
    lineZ_values[ab][1]=float(lineZ_values[ab][1])
    lineZ_values[ab][2]=float(lineZ_values[ab][2])
    ab=ab+1





c=len(facelines)#n of elementsstr(ac)+'
ac=1
text=[]

for i in range(1805):
    textt=('%.15f' %(V_X_values[i])+' '+'%.15f' %(V_Y_values[i])+' '+'%.15f' %(V_Z_values[i]))
    text.insert(1,textt)



text.append(text[0])
text[0]=[]
text=(text[::-1])
for i in range(len(text)):
    outfile = open('//Users//alikhodadadi//Desktop//summer internships//uni(floating obj)//Task1(test).txt', 'a')
    outfile.write(str(text[i])+'\n')

print(text)




for ind in range(len(lineX_values)):
    my3dplot.plot3D(lineX_values[ind],lineY_values[ind],lineZ_values[ind])


my3dplot.scatter3D(V_X_values,V_Y_values,V_Z_values)
plt.show()








write=[]
writee=[]
for i in range(len(all_faces)):
    write=(all_faces[i])
    writee.insert(1,write)


writee.append(writee[0])

del(writee[0])
writee=writee[::-1]


a=0
lykk=[]



for i in range(len(writee)):

    mixed_cordinatess=(str(writee[i][0:-1]))
    lykk.append(mixed_cordinatess.split())

lk=[]
a=0

while a<(len(facelines)):

    yyy = str(int(lykk[a][0])-1)

    yyy1 = str(int(lykk[a][1])-1)

    yyy2=str(int(lykk[a][2])-1)

    lk.append(yyy+' '+yyy1+' '+yyy2+'''
    ''')
    a=a+1

print(lk)



for i in range(len(text)):
    outfile = open('//Users//alikhodadadi//Desktop//summer internships//uni(floating obj)//Task1(test2).txt', 'a')
    outfile.write(str(lk[i])+'\n')






