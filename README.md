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