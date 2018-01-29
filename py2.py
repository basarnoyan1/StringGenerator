import itertools as it
import gc

chars = ['q','w','e','r','t','y','u','ı','o','p',
        'ğ','ü','a','s','d','f','g','h','j','k','l','ş','i',
        'z','x','c','v','b','n','m','ö','ç',
        'Q','W','E','R','T','Y','U','I','O','P','Ğ','Ü',
        'A','S','D','F','G','H','J','K','L','Ş','İ',
        'Z','X','C','V','B','N','M','Ö','Ç',
        '1','2','3','4','5','6','7','8','9','0',
        '!','.',',','#','%','&','_','-','/','*',':','?','@']

f = open('text.txt','a')
chrs = input("Chars: ")
chlist = []
for i in range(len(chrs)):
    chlist.append(chrs[i])

keywords = []

def funclist(lst,a):
    k = []
    for i in it.product(lst, repeat = a):
        st = ""
        for e in range(len(i)):
            st += i[e]
        f.write('\n' + str(st))
        ''.join(i)
        gc.collect()
        #k.append(i)
        print(i)
    return k

for i2 in range(6,11):
    keys = funclist(chlist,i2)
    #keys = [''.join(i) for i in it.product(chlist, repeat = i2)]
    keywords += keys

print(len(keywords))
input("Press Enter to exit.")