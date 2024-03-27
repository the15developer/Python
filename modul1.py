

def count(metin, n):
    boyut=len(metin)
    
    if(boyut<n):
        print("Metin " + str(n) + " karakterden kucuktur!")
        return None
    
    liste=[0]*26
    for i in range(n):
        if(metin[i]=='a'):
            liste[0]=liste[0]+1;
        elif(metin[i]=='b'):
            liste[1]=liste[1]+1;
        elif(metin[i]=='c'):
            liste[2]=liste[2]+1;
        elif(metin[i]=='d'):
            liste[3]=liste[3]+1;
        elif(metin[i]=='e'):
            liste[4]=liste[4]+1;
        elif(metin[i]=='f'):
            liste[5]=liste[5]+1;
        elif(metin[i]=='g'):
            liste[6]=liste[6]+1;
        elif(metin[i]=='h'):
            liste[7]=liste[7]+1;
        elif(metin[i]=='i'):
            liste[8]=liste[8]+1;
        elif(metin[i]=='j'):
            liste[9]=liste[9]+1;
        elif(metin[i]=='k'):
            liste[10]=liste[10]+1;
        elif(metin[i]=='l'):
            liste[11]=liste[11]+1;
        elif(metin[i]=='m'):
            liste[12]=liste[12]+1;
        elif(metin[i]=='n'):
            liste[13]=liste[13]+1;
        elif(metin[i]=='o'):
            liste[14]=liste[14]+1;
        elif(metin[i]=='p'):
            liste[15]=liste[15]+1;
        elif(metin[i]=='q'):
            liste[16]=liste[16]+1;
        elif(metin[i]=='r'):
            liste[17]=liste[17]+1;
        elif(metin[i]=='s'):
            liste[18]=liste[18]+1;
        elif(metin[i]=='t'):
            liste[19]=liste[19]+1;
        elif(metin[i]=='u'):
            liste[20]=liste[20]+1;
        elif(metin[i]=='v'):
            liste[21]=liste[21]+1;
        elif(metin[i]=='w'):
            liste[22]=liste[22]+1;
        elif(metin[i]=='x'):
            liste[23]=liste[23]+1;
        elif(metin[i]=='y'):
            liste[24]=liste[24]+1;
        elif(metin[i]=='z'):
            liste[25]=liste[25]+1;
        else:
            continue;
            
    dict = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21,'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25}                                                                    
    inv_dict = {v: k for k, v in dict.items()}
    for i in range(26):
        print("{}:number of using: {} using rate:{:.4f}".format(inv_dict[i], liste[i], round(100*liste[i]/n)))
    

def rectangle_area(length, width):
    return length*width


def sphere_volume(radius):
    return (4/3)*(3.14*(radius**3))

def word_count(metin):
    sayac=0
    metin=metin.strip()
    for i in range(0, len(metin)):
        if(metin[i]==' '):
            if(metin[i+1]==' '):
                continue;
            else:
                sayac=sayac+1
    return sayac+1



def me():
    print("Dannya Chami 211213114")
    print("Python eglencelidir! ;))")
    
def hey():
    print(__name__)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
