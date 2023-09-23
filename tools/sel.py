import random

COUNT   = 385
LOW     = 1
HIGH    = 1560

SRC_FOLD = "Wet"
DST_FOLD = "Wet_sml"

opf = open("sml.sh", 'w')
s = set()
i = 0
opf.write("#!/bin/bash\n")
while(i < COUNT):
    n = random.randint(LOW,HIGH)
    if n not in s:
        s.add(n)
        opf.write(f"cp \"{SRC_FOLD}/img{n:03}.jpg\" \"{DST_FOLD}/\"\n")
        i += 1