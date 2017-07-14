# This is the script try to renew the ssl certificate
# Written by zhanglintc at 2017.07.13

# issue the certificate in folder "zhanglintc.co"
puts "issue the certificate => not enabled"
# `acme.sh  --issue --dns -d zhanglintc.co -d www.zhanglintc.co -d mmrz.zhanglintc.co -d zncx.zhanglintc.co`
puts "issue: done\n\n"

# renew the certificatea
puts "renew the certificate"
puts `/home/lane/.acme.sh/acme.sh --renew --force -d zhanglintc.co -d www.zhanglintc.co -d mmrz.zhanglintc.co -d zncw.zhanglintc.co`
puts "renew: done\n\n"

# copy the certificate to specific folder
puts "copy the certificate"
puts `sudo cp -r /home/lane/.acme.sh/zhanglintc.co /home/lane/ssl`
puts "copy: done\n\n"

# force reload configuration of Nginx
puts "reload Nginx"
puts `sudo service nginx force-reload`
puts "reload: done\n\n"

