
import random
import time

main_list=[]


def initializeword():
    w=""
    with open ("words_alpha.txt","r") as f:
        allText = f.read()
        words=list(map(str,allText.split()))
        word2=[x for x in words if len(x)==5]
        global main_list
        main_list=word2
        return main_list
        

def gameplay():
    global main_list
    word=main_list.copy()
    w=(random.choice(word))
    print(w)
    n=6
    x=[0]*n
    while(n):
        a=(random.choice(word))
        green_index=[]
        print("The word is: " + a )
        if(w==a):
            for i in range(len(x)):
                x[i]="Green"
            print(x)
            print("Wow, you guessed it right.")
            break

        for i in range(0,len(w)):
            if(w[i]==a[i]):
                x[i]="Green"
                green_index.append(a[i])
            elif(a[i] in w):
                if(a[i] in green_index and w.count(a[i])==1):
                    x[i]="Grey"
                else:
                    x[i]="Orange"
            elif(a[i] not in w):
                x[i]="Grey"
            
                if(n==1 and i==len(a)-1):
                    print(x)
                    print("Better Luck next time")
                    break
        print(x)
        time.sleep(1)
        
        g_alpha=[]
        if("Green" in x):
            alpha=[]
            
            for j in range(len(x)):
                if(x[j]=="Green"):
                    alpha.append(j)
                    g_alpha.append(a[j])
                for k in alpha:
                    word=[y for y in word if a[k] in y and (k==y.index(a[k]) or k==y.rindex(a[k]))]
                #print(word)
        if("Orange" in x):
            alpha=[]
            for j in range(len(x)):
                if(x[j]=="Orange"):
                    alpha.append(j)
                for k in alpha:
                    word=[y for y in word if a[k] in y and k!=y.index(a[k])]
                #print(word)
        if("Grey" in x):
            alpha=[]
            for j in range(len(x)):
                if(x[j]=="Grey"):
                    alpha.append(j)
            for k in alpha:
                if(a[k] in g_alpha):
                    word=[y for y in word if y[k]!=a[k]]
                else:
                    word=[y for y in word if a[k] not in y]
                  
                #word=[y for y in word if (a[k] not in g_alpha and y)]
            #print(word)
        
        
            
            
            
        n=n-1

    
    print("\nGame Over")
    print("The word is :", w )
    
    s1=input("Press 1 to restart\nPress 2 to exit\n")
    if(s1=='1'):
        initializeword()
        gameplay()
    else:
        exit()
        

s=input("Press 1 to Start Game")
if(s=="1"):
    initializeword()
    gameplay()

