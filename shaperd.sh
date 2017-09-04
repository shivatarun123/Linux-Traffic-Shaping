#!/bin/bash
echo "atslabb00" | sudo -S sudo tc qdisc show > fil1.txt
while true
do 
        echo "atslabb00" | sudo -S sudo tc qdisc show > fil2.txt
        sleep 3
        if  diff fil2.txt fil1.txt 
           then
              echo "same"
           else
              echo $(date)  $(comm -2 -3 fil2.txt fil1.txt) >> /home/ats/project/his.txt
              printf '\n' >> /home/ats/project/his.txt
              cp fil2.txt fil1.txt
        fi
done

