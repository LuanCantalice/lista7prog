l = int(input("Digite o número final da sequência: "))

if(l != 0 and l>1):
    prinum = 1
    segnum = 1
    proxnum = 0
    
    print(prinum, segnum, end=' ')
    
    while(l>=proxnum):
        proxnum = prinum+segnum
        if(proxnum>=l):
            break
        else:
            print(proxnum, end=' ')
            proxnum = prinum+segnum
            prinum = segnum
            segnum = proxnum
    
    
    
    
    
    
