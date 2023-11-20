## Development

```
git clone https://github.com/Resend1298/bookdb-midterm-backend.git
cd bookdb-midterm-backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

## Deployment

```
docker run -d --name bookdb-midterm-backend -p 10001:10001 --restart=unless-stopped ghcr.io/resend1298/bookdb-midterm-backend
```

Nginx config template:

```
server {
        listen 80;
        server_name example.com;

        location / {
                proxy_pass http://192.168.0.51:10002;
        }

        location /api/ {
                proxy_pass http://192.168.0.51:10001/;
        }
}
```
