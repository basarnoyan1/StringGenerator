import itertools as it
import gc

chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'ı', 'o', 'p',
         'ğ', 'ü', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ş', 'i',
         'z', 'x', 'c', 'v', 'b', 'n', 'm', 'ö', 'ç',
         'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Ğ', 'Ü',
         'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ş', 'İ',
         'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Ö', 'Ç',
         '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
         '!', '.', ',', '#', '%', '&', '_', '-', '/', '*', ':', '?', '@']
savtxt = False
svname = "text"
chrs = input("Chars: ")
if input("Save ?  [y/n] ") == "y":
    savtxt = True
    svname = input("File name : [*.txt] ")
if chrs == "default":
    chrs = chars
if input("Length range is greater than 1 ?  [y/n] ") == "y":
    rn1 = int(input("Min: "))
    rn2 = int(input("Max: "))+1
else:
    rn1 = int(input("Length: "))
if input("Repetition check ?  [Experimental] ") == "y":
    repcheck = True
else:
    repcheck = False
chlist = []
for i in range(len(chrs)):
    chlist.append(chrs[i])

keywords = []


def funclist(lst, a):
    k = []
    for i in it.product(lst, repeat=a):
        st = ""
        if repcheck:
            chres = True
            for e in range(len(i)):
                if i[e-1] == i[e]:
                    chres = False
            if chres == True:
                for e in range(len(i)):
                    st += i[e]
                if savtxt:
                    f = open(svname + '.txt', 'a')
                    f.write('\n' + str(st))
                    ''.join(i)
                gc.collect()
                print(i)
        else:
            for e in range(len(i)):
                st += i[e]
            if savtxt:
                f = open(svname + '.txt', 'a')
                f.write('\n' + str(st))
                ''.join(i)
            gc.collect()
            # k.append(i)
            print(i)
    return k

try:
    for i2 in range(rn1, rn2):
        keys = funclist(chlist, i2)
        # keys = [''.join(i) for i in it.product(chlist, repeat = i2)]
        keywords += keys
except:
    keys = funclist(chlist, rn1)


input("Press Enter to exit.")
