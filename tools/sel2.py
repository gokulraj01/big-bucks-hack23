import os, random

SRC_FOLD = "/media/ramdisk/Hack/train/Wet"
DST_FOLD = "/media/ramdisk/Hack/val/Wet"

per = int(input("Cut %: "))

f = os.listdir(SRC_FOLD)
count = int(len(f)*per/100)


opf = open("sml.sh", 'w')
s = set()
i = 0
opf.write("#!/bin/bash\n")
while(i < count):
    n = random.choice(f)
    if n not in s:
        s.add(n)
        opf.write(f"cp \"{SRC_FOLD}/{n}\" \"{DST_FOLD}/\"\n")
        i += 1

