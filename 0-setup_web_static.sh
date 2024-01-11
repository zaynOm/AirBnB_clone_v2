#!/usr/bin/env bash
# setup Nginx server for web_static deployment
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello from School!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        add_header Y-Served-By $HOSTNAME;

        location /hbnb_static {
                alias /data/web_static/current/;
                try_files \$uri \$uri/ @404;
        }

        location /redirect_me {
                return 301 /;
        }

        location @404 {
                return 404 \"Ceci n'est pas une page\";
        }
}" > /etc/nginx/sites-available/default

service nginx restart
