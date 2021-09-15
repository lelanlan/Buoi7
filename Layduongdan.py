import re

def  ApacheLog(file):
    f = open(file)
    # Logfile = '''10.254.254.28 - - \[06/Aug/2007:00:07:21 -0700\] "GET .*jpg HTTP/1.0" 302 306 "-" "Mozilla/5.0 \(Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.1; Google-TR-3\) Gecko/20060111 Firefox/1.5.0.1"'''
    test1 = ".*jpg.*Firefox"
    l = f.readlines()
    s = set()
    for i in l:
        if re.findall(test1, i):
            tachchuoii = i.split(" ")
            linkjpg = ""
            for j in tachchuoii:
                a = ".jpg"
                if re.search(a, j):
                    linkjpg = j
            property1 = "http//" + tachchuoii[-1].replace('"', '') + linkjpg
            property1 = re.sub("\n", '', property1)
            s.add(property1)
    for i in s:
       print(i)


ApacheLog("place_code.txt")
print("=======================================================================================")
ApacheLog("animal_code.txt")

