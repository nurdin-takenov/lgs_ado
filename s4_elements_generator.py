# -*- coding: cp1251 -*-
#removing zero elements in an array
def removezero(lest):
    lest = list(filter(lambda x: x!= '', lest))
    return lest

#converting list to braid format
def braid(lest):
    lest = list(filter(lambda x: x!= '', lest))
    stroka = '{'
    for i in range(len(lest)):
        stroka = stroka+str(lest[i])
        if (i<len(lest)-1):
            stroka = stroka + ','
    stroka = stroka+'}'
    return stroka

#elements of S_2
s2 = [[''],['1'], ['-1']]

#elements of S_3
s3=[]
s3=s3+s2
for i in range(len(s2)):
    for j in range(len(s2)):
        s3.append(s2[i]+['2']+s2[j])
for i in range(len(s2)):
    for j in range(len(s2)):
        s3.append(s2[i]+['-2']+s2[j])
for i in range(len(s2)):
    s3.append(s2[i]+['2','-1','2'])
    
#elements of S_4
s4right = [[''], ['-3','2','-1','2','-3'], ['3','-2','1','-2','3'],['3'],['-3']]
s4right = s4right + [['-3','-2'],['-3','2'],['3','-2'],['3','2']]
s4right = s4right + [['-3','-2','-1'],['-3','2','-1'],['3','-2','-1'],['3','2','-1']]
s4right = s4right + [['-3','-2','1'],['-3','2','1'],['3','-2','1'],['3','2','1']]
s4right = s4right + [['-3','-2','1','-2'],['3','-2','1','-2'],['3','-2','3']]
s4right = s4right + [['3','-2','3','-1'],['3','-2','3','1'],['3','-2','3','1','-2','1']]
s4right = s4right + [['3','-2','3','-1','-2'],['3','-2','3','-1','2']]
s4right = s4right + [['3','-2','3','1','-2'],['3','-2','3','1','2']]
s4=[]
for i in range(len(s3)):
    for j in range(len(s4right)):
        s4.append(s3[i]+s4right[j])
print(str(s3))

#printing elements of S_4 in a form recognizable by Mathematica program
#there are 648 elements
#for better visualisation they are broken into groups of 27 elements
g=open('s4elements.txt', 'w')
for i in range(len(s4)):
    if i%27==0:
        g.write(str((27+i)//27)+'-th group of 27 elements of S_4')
        g.write('\n')
        g.write('{')
    g.write('{4,'+braid(s4[i])+'}')
    if i%27!=26:
        g.write(',')
    else:
        g.write('}')
        g.write('\n\n')
g.close()

        


