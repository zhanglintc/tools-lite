# This is the script try to renew the ssl certificate
# Written by zhanglintc at 2017.07.13

# issue the certificate in folder "mmrz.zhanglintc.co"
# `/home/lane/.acme.sh/acme.sh --issue --dns dns_dp -d mmrz.zhanglintc.co`
# puts "issue the certificate => not enabled"

domains = [
    "mmrz.zhanglintc.co",
    "navi.zhanglintc.co",
    "zncx.zhanglintc.co",
    "sxcx.zhanglintc.co",
    "bing.zhanglintc.co",
]

domains = domains.map{ |e| e="-d #{e}"}
domain_str = domains.join(" ")
issue_str = "/home/lane/.acme.sh/acme.sh --issue --dns dns_dp #{domain_str}"

puts "1. issue the certificate\n"
puts "copy and execute the command below in other terminal, then press [ENTER]:\n\n"
puts issue_str + "\n\n"

puts "waiting for [ENTER]..."
gets

puts "issue: done\n\n"

# renew the certificatea
# puts "renew the certificate => not enabled"
# `/home/lane/.acme.sh/acme.sh --renew -d mmrz.zhanglintc.co`
# puts "renew: done\n\n"

# copy the certificate to specific folder
puts "2. copy the certificate"
`sudo cp -r /home/lane/.acme.sh/mmrz.zhanglintc.co /home/lane/ssl`
puts "copy: done\n\n"

# force reload configuration of Nginx
puts "3. reload Nginx"
`sudo service nginx force-reload`
puts "reload: done\n\n"

