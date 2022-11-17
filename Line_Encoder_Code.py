import numpy as np
import matplotlib.pyplot as plt
from random import *

randBinList = lambda n: [randint(0,1) for b in range(1,n+1)]
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

print("\n-----------------------Line Encoder-----------------------")
print("--------------------------------------By Bhagat Snehankit.")

print("\nEnter \"1\" for User Input Type")
print("Enter \"2\" for Random Binary Input Type")
x=int(input("Type : "))
if(x==1):
    s=input("\nEnter The Binary Signal : ")
else:
    bla = int(input("\nEnter \"1\" for Fixed Subsequence(size must be greater than 8) Otherwise Enter \"2\" : "))
    size = int(input("\nEnter Size of Binary Signal : "))
    kla = randint(0,9)
    if(bla==1):
        size = size - 8
    kla = kla%size
    #print(kla)
    s=[]
    s=randBinList(size)
    ankit = "00000000"
    #print(*s)
    s="".join(str(i) for i in s)
    if(bla==1):
        s=s[:kla]+ankit+s[kla:]
    print("Input is: ")
    print(s)


print("\nCoding Schemes Are...")
print("\n1. NRZ-L \n2. NRZ-I \n3. Manchester \n4. Diff. Manchester \n5. AMI\n")
n=int(input("Type : "))

if(n==1):
    # Perform NRZ-L ...
    ls=list()
    for i in range(len(s)):
        if(s[i]=='0' or s[i]==0):
            ls.append(-1)
        else:
            ls.append(1)
    xs = np.repeat(range(len(s)), 2)
    ys = np.repeat(ls, 2)
    xs=xs[1:]
    xs=np.append(xs,(xs[len(xs)-1]+1))
    ys=ys[:-1]
    ys=np.append(ys,(ys[len(ys)-1]))
    
    plt.step(xs,ys)
    plt.ylim(-2, 2)
    plt.title('The Binary Signal : {}\n'.format(s), size=16)
    plt.show()

elif(n==2):
    # NRZ-I ...
    Is=list()
    if(s[0]=='0' or s[0]==0):
        Is.append(-1)
    else:
        Is.append(1)
    k=len(s)
    i=1
    while(i<k):
        if(int(s[i])==0):
            Is.append(Is[i-1])
        else:
            Is.append(-Is[i-1])
        i=i+1
    xs = np.repeat(range(len(s)), 2)
    ys = np.repeat(Is, 2)
    xs=xs[1:]
    xs=np.append(xs,(xs[len(xs)-1]+1))
    ys=ys[:-1]
    ys=np.append(ys,(ys[len(ys)-1]))

    plt.step(xs,ys)
    plt.ylim(-2, 2)
    plt.title('The Binary Signal : {}\n'.format(s), size=16)
    plt.show()

elif(n==3):
    # Manchester ...
    pm=list()
    for j in range(len(s)):
        if(s[j]=='0' or s[j]==0):
            pm.append(-1)
            pm.append(1)
        else:
            pm.append(1)
            pm.append(-1)
    xs=[x*0.5 for x in range(0,(2*len(s)))]
    xs=np.repeat(xs,2)
    ys = np.repeat(pm, 2)
    xs=xs[1:]
    xs=np.append(xs,(xs[len(xs)-1]+0.5))
    ys=ys[:-1]
    ys=np.append(ys,(ys[len(ys)-1]))
	
    plt.step(xs,ys)
    plt.ylim(-2, 2)
    plt.title('The Binary Signal : {}\n'.format(s), size=16)
    plt.show()

elif(n==4):
    # Differential Manchester ...
    pdm=list()
    pdm.append(1)
    pdm.append(-1)
    i=1
    k=len(s)
    while(i<k):
        if(int(s[i])==1):
            pdm.append(pdm[len(pdm)-1])
            pdm.append(-pdm[len(pdm)-1])
        else:
            pdm.append(-pdm[len(pdm)-1])
            pdm.append(-pdm[len(pdm)-1])
        i=i+1
    print(pdm)
    xs=[x*0.5 for x in range(0,(2*len(s)))]
    xs=np.repeat(xs,2)
    ys = np.repeat(pdm, 2)
    xs=xs[1:]
    xs=np.append(xs,(xs[len(xs)-1]+0.5))
    ys=ys[:-1]
    ys=np.append(ys,(ys[len(ys)-1]))

    plt.step(xs,ys)
    plt.ylim(-2, 2)
    plt.title('The Binary Signal : {}\n'.format(s), size=16)
    plt.show()
    

else:
    # Perform AMI ...
    q=int(input("\nPress \"0\" for Scrambling or \"1\" for Not Scrambling : "))
    if(q==0):
        am=list()
        m=1
        for i in range(len(s)):
            if(int(s[i])==0):
                am.append(0)
            else:
                if(m%2==1):
                    am.append(1)
                else:
                    am.append(-1)
                m=m+1
        xs = np.repeat(range(len(s)), 2)
        ys = np.repeat(am, 2)
        xs=xs[1:]
        xs=np.append(xs,(xs[len(xs)-1]+1))
        ys=ys[:-1]
        ys=np.append(ys,(ys[len(ys)-1]))
        
        plt.step(xs,ys)
        plt.ylim(-2, 2)
        plt.title('The Binary Signal : {}\n'.format(s), size=16)
        plt.show()
        
    else:
        # Scrambling ...
        p=int(input("\nEnter \"1\" for B8ZS ... Enter \"2\" for HDB3..."))
        q=len(s)
        if(p==1):
            # B8ZS...
            bz=list()
            m=1
            s1=s.replace("00000000","000vb0vb")
            for i in range(len(s1)):
                if(s1[i]=='0' or s1[i]==0):
                    bz.append(0)
                elif(s1[i]=='1'):
                    if(m%2==1):
                        bz.append(1)
                    else:
                        bz.append(-1)
                    m=m+1
                elif(s1[i]=='v'):
                    if(m%2==1):
                        bz.append(-1)
                    else:
                        bz.append(1)
                else:
                    if(m%2==1):
                        bz.append(1)
                    else:
                        bz.append(-1)
                    m=m+1
            xs = np.repeat(range(len(s)), 2)
            ys = np.repeat(bz, 2)
            xs=xs[1:]
            xs=np.append(xs,(xs[len(xs)-1]+1))
            ys=ys[:-1]
            ys=np.append(ys,(ys[len(ys)-1]))

            plt.step(xs,ys)
            plt.ylim(-2, 2)
            plt.title('The Binary Signal : {}\n'.format(s), size=16)
            plt.show()


        else:
            # HDB3 ...
            m=0
            hd=list()
			  
            f=s.find("0000")
            if(f==-1):
                f=len(s)
            i=0
            k=len(s)
            d=1
            p=0
            while(i<k):
                if(s[i]=='1' or s[i]==1):
                    m=m+1
                    p=p+1
                    if(m%2==1):
                        hd.append(d)
                        d=1
                    else:
                        hd.append(-d)
                        d=-d
                else:
                    if(i<f):
                        hd.append(0)
                    elif(i==f):
                        i=i+3
                        if(p%2==0):
                            hd.append(-d)
                            hd.append(0)
                            hd.append(0)
                            hd.append(-d)
                            d=-d
                            p=p+2
                            m=m+1
                        else:
                            hd.append(0)
                            hd.append(0)
                            hd.append(0)
                            hd.append(d)
                            p=p+1
                        jk=s[i+1:(i+1)+(k-i-1)]
                        x=jk.find("0000")
                        if(x==-1):
                            f=k
                        else:
                            f=i+1+x
                i=i+1
            xs = np.repeat(range(len(s)), 2)
            ys = np.repeat(hd, 2)
            xs=xs[1:]
            xs=np.append(xs,(xs[len(xs)-1]+1))
            ys=ys[:-1]
            ys=np.append(ys,(ys[len(ys)-1]))
            plt.step(xs,ys)
            plt.ylim(-1.5,1.5)
            plt.title('The Binary Signal : {}\nHDB3...'.format(s), size=16)
            plt.show()
            print(hd)