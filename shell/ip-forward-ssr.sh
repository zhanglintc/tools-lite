#/usr/bin/bash

bwh=97.64.107.246
ten=10.139.131.156

remotePort=10285
localPort=10000


sudo iptables -t nat -A PREROUTING -p tcp -m tcp --dport $localPort -j DNAT --to-destination $bwh:$remotePort
sudo iptables -t nat -A PREROUTING -p udp -m udp --dport $localPort -j DNAT --to-destination $bwh:$remotePort
sudo iptables -t nat -A POSTROUTING -d $bwh -p tcp -m tcp --dport $remotePort -j SNAT --to-source $ten
sudo iptables -t nat -A POSTROUTING -d $bwh -p udp -m udp --dport $remotePort -j SNAT --to-source $ten
