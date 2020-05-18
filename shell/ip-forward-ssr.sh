#/usr/bin/bash

bwh=167.179.103.95
ten=10.139.131.156

remotePort=10185
localPort=10167

# detele all existing rules
sudo iptables -t nat -F

# add new rules
sudo iptables -t nat -A PREROUTING -p tcp -m tcp --dport $localPort -j DNAT --to-destination $bwh:$remotePort
sudo iptables -t nat -A PREROUTING -p udp -m udp --dport $localPort -j DNAT --to-destination $bwh:$remotePort
sudo iptables -t nat -A POSTROUTING -d $bwh -p tcp -m tcp --dport $remotePort -j SNAT --to-source $ten
sudo iptables -t nat -A POSTROUTING -d $bwh -p udp -m udp --dport $remotePort -j SNAT --to-source $ten

# view current rules
sudo iptables -t nat -vnL

