# _*_ coding:utf-8 _*_ 

def k():
    d={}

    l=ord('0')
    for i,j in enumerate(range(0,10)):
        d[l+i]=j

    l=ord('a')
    for i,j in enumerate(range(10,36)):
        d[l+i]=j

    l=ord('A')
    for i,j in enumerate(range(10,36)):
        d[l+i]=j

    print d
    return d


def test_k():
    k=k()

    print k.get(47,None)


def n():
    d={}
    t=0
    a='EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443'
    length=len(a)
    
    c=4

    a=a[::-1]

    p=0

    for i in a:
        num=int(i,16)    
    
        if p==0:
            n=num
        else:
            n=n|num<<p*c

        p+=1
        if p==7 or length-t*7-p==0:
            p=0
            d[t]=n
            t+=1

    print d
        


n()     

        






