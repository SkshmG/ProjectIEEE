import csv
import re
D_main={'A1':'A1','B1':'B1','C1':'C1','D1':'D1','E1':'E1','F1':'F1','G1':'G1','A2':'A2','B2':'B2','C2':'C2','D2':'D2','E2':'E2','F2':'F2','G2':'G2'}
D_chosen={}
L_Preffrnce=['G2','F2','E2','D2','C2','B2','A2','G1','F1','E1','D1','C1','B1','A1']
lab1='L05L06L11L12L17L18L23L24L29L30'
lab2='L03L04L09L10L15L16L21L22L27L28'
y,z,q=0,0,None

D_sub={}
def mainallot(v,end=None):
    allot(v)
    L_temp.remove('BCSE102P ')
    L_temp.remove('BECE101P ')
    L_temp.remove('BPHY101P ')
    L_temp.remove('BENG101P ')
    if 'BSTS102P 'in L_temp:
        L_temp.remove('BSTS102P ')
        if 'F2'not in D_chosen:
            D_chosen['F2']='BSTS'
            D_main['F2']='BSTS'
        else:
            D_chosen['F1']='BSTS'
            D_main['F1']='BSTS'
    for i in L_temp:
        autochoose('%s.csv'%(i[:4]))
    
def allot(c):
    if c==16:
        L_temp.remove('BMAT102L')
        L_temp.remove('BSTS102P ')
    elif c==17.5:
        L_temp.remove('BMAT102L')
    elif c==18.5:
        L_temp.remove('BHUM101N ')
        L_temp.remove('BSTS102P ')
    elif c==19.5:
        L_temp.remove('BHUM101N ')
    elif c==20:
        L_temp.remove('BSTS102P ')
    elif c==21.5:
        ww=0
    if 'BHUM101N ' in L_temp:
        L_temp.remove('BHUM101N ')
        
def autochoose(a):
    L1,S1,z,c=[],'',0,0
    filenow=open(a,'r',newline='\r\n')
    info=csv.reader(filenow)
    for i in info:
        if i[3] not in S1:
            S1+=i[3]
            L1.append(i[3])
            if len(i[3])>8:
                c=1
    for i in L_Preffrnce:
        if i in S1 and D_main[i]==i and i not in D_chosen:
            slot=i
            if a[:4]=='BMAT':
                D_main[slot]='%sP'%(a[:4])
                D_chosen[slot]='%sP'%(a[:4])
                break
            if c==1:
                if re.match('[A-H]1',slot):
                    for i in range(60,30,-2):
                        for j in L1:
                            if 'L%s+L%s'%(i-1,i) in j and j[:3] and j[4:7] and j[8:11] and j[12:] not in D_chosen :
                                D_chosen[j[:3]]='%sL'%(a[:4])
                                D_chosen[j[4:7]]='%sL'%(a[:4])
                                D_chosen[j[8:11]]='%sL'%(a[:4])
                                D_chosen[j[12:]]='%sL'%(a[:4])
                                z=1
                                break
                        if z==1:
                            break
                elif re.match('[A-H]2',slot):
                    for j in L1:
                        if j[:3] and j[4:7] and j[8:11] and j[12:] not in D_chosen and j[:3] and j[4:7] and j[8:11] and j[12:] in lab1 :
                            D_chosen[j[:3]]='%sL'%(a[:4])
                            D_chosen[j[4:7]]='%sL'%(a[:4])
                            D_chosen[j[8:11]]='%sL'%(a[:4])
                            D_chosen[j[12:]]='%sL'%(a[:4])
                            z=1
                            break
                    else :
                        if z!=1:
                            for j in L1:
                                if j[:3] and j[4:7] and j[8:11] and j[12:] not in D_chosen and j[:3] and j[4:7] and j[8:11] and j[12:] in lab2 :
                                    D_chosen[j[:3]]='%sL'%(a[:4])
                                    D_chosen[j[4:7]]='%sL'%(a[:4])
                                    D_chosen[j[8:11]]='%sL'%(a[:4])
                                    D_chosen[j[12:]]='%sL'%(a[:4])
                                    z=1
                                    break
            else:
                if re.match('[A-H]1',slot):
                    st,en,j=60,30,-2
                elif re.match('[A-H]2',slot):
                    st,en,j=30,0,-6
                for i in range(st,en,j):
                    for j in L1:
                        if 'L%s+L%s'%(i-1,i) in j and 'L%s'%(i) and 'L%s'%(i-1) not in D_chosen:
                            D_chosen[j[:int(len(j)/2)]]='%sL'%(a[:4])
                            D_chosen[j[int(len(j)/2)+1:]]='%sL'%(a[:4])
                            z=1
                            break
                    if z==1:
                        break
        if z==1:        
            D_main[slot]='%sP'%(a[:4])
            D_chosen[slot]='%sP'%(a[:4])
            break
    filenow.close()

        
def tableprinttheo(a,b):
    x=['A1','B1','C1','D1','E1','F1','G1']
    print('   \t',end='')
    for i in range(a,25,5):
       print(D_main[x[i%7]],'\t',end='')
    print('----\t',end='')
    x=['A2','B2','C2','D2','E2','F2','G2']
    for i in range(a,25,5):
       print(D_main[x[i%7]],'\t',end='')
    print('----',end='')
    print('\n')
    print(b,'-'*101,)
def tableprintprac(a,b):
    for i in range(a,b):
        if 'L%s'%(i) in D_chosen:
            print(D_chosen['L%s'%(i)],'\t',end='')
        else:
            print('L%s'%(i),'\t',end='')
    


    
print('\t\t','<>'*30,'\n')
print('\t\t\tTHESE ARE THE AVIALABLE COURSES')
print('\t\t','-'*60)
File_main=open('COURSE.csv','r',newline='\r\n')
C_r=csv.reader(File_main)
for i in C_r:
    print('\t\t\t',i[0],'\t\t',i[1],'\t\t\t',i[2])
    print('\t\t','-'*60)
    try:
        D_sub[i[1]]=float(i[2])
    except ValueError:
        continue

cred=eval(input('Enterno of credits out of the following options: 16(min), 17.5 ,18.5 ,19.5 ,20 ,21.5: ' ))
while cred not in[16,17.5,18.5,19.5,20,21.5]:
    cred=eval(input('enter appropriate value'))
    
File_main.close()
L_temp=list(D_sub.keys())
mainallot(cred)
print('\n','-'*48,'TIMETABLE','-'*47)
print('\n','-'*104)
tableprinttheo(0,'MON')
print('    \t',end='')
tableprintprac(1,7)
tableprintprac(31,37)
print('\n','-'*104)
print('\n')
tableprinttheo(1,'TUE')
print('    \t',end='')
tableprintprac(7,13)
tableprintprac(37,43)
print('\n','-'*104)
print('\n')
tableprinttheo(2,'WED')
print('    \t',end='')
tableprintprac(13,19)
tableprintprac(43,49)
print('\n','-'*104)
print('\n')
tableprinttheo(3,'THU')
print('    \t',end='')
tableprintprac(19,25)
tableprintprac(49,55)
print('\n','-'*104)
print('\n')
tableprinttheo(4,'FRI')
print('    \t',end='')
tableprintprac(25,31)
tableprintprac(55,61)
print('\n','-'*104)

print('\n\n\t\tNote: Course BHUM101N will be provided as an online course and hence is not in timetable...')

print('\n\n\t\t','<>'*30,'\n')
    
    


    
    


    
    



    
    

