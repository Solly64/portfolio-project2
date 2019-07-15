[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=nyfl_djangoline
Group=www-data
WorkingDirectory=/home/nyfl_djangoline/sportsproject/portfolio-project/my_app1/first_app
ExecStart=/home/nyfl_djangoline/sportsproject/sports_app/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/nyfl_djangoline/sportsproject/portfolio-project/my_app1/first_app/first_app.sock first_app.wsgi:application

[Install]
WantedBy=multi-user.target

----------------------------------------------------------------------

server {
    listen 80;
    server_name 167.99.155.124;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/nyfl_djangoline/sportsproject/portfolio-project/my_app1/first_app;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/nyfl_djangoline/sportsproject/portfolio-project/my_app1/first_app/first_app1.sock;
    }
}
