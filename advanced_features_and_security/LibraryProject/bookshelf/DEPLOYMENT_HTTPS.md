# HTTPS Deployment Configuration (Nginx Example)

## Goal
Serve the Django app over HTTPS using SSL/TLS certificates and redirect all HTTP traffic to HTTPS.

## Nginx (typical setup)
1. Obtain certificates (e.g., Let’s Encrypt).
2. Configure Nginx server blocks:

### HTTP -> HTTPS redirect
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$host$request_uri;
}

### HTTPS server
server {
    listen 443 ssl;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

## Notes
- Django settings enforce HTTPS using SECURE_SSL_REDIRECT and HSTS.
- Cookies are protected using CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE.
