server {
    listen 80;
    server_name metatrader.chicheongweng.com; 
    large_client_header_buffers 4 1024k;
    keepalive_timeout   15;
#    ssl_certificate /etc/nginx/ssl/fullchain.pem;
#    ssl_certificate_key /etc/nginx/ssl/privkey.pem;
#    ssl_session_cache   shared:SSL:10m;
#    ssl_session_timeout 10m;
#    ssl_ciphers         RC4:HIGH:!aNULL:!MD5;
#    ssl_prefer_server_ciphers on;

    client_max_body_size 16M;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/workspace/trade_reporting;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/workspace/trade_reporting/trade_reporting.sock;
    }

    access_log /home/ubuntu/workspace/trade_reporting/logs/nginx-access.log;
    error_log /home/ubuntu/workspace/trade_reporting/logs/nginx-error.log;
}
