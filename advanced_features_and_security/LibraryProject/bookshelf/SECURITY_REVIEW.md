# Security Review

## Implemented Measures
- SECURE_SSL_REDIRECT: Forces HTTPS by redirecting HTTP requests.
- HSTS (SECURE_HSTS_SECONDS / INCLUDE_SUBDOMAINS / PRELOAD): Instructs browsers to always use HTTPS for the site.
- Secure cookies (SESSION_COOKIE_SECURE / CSRF_COOKIE_SECURE): Prevents cookies from being sent over HTTP.
- X_FRAME_OPTIONS = DENY: Protects against clickjacking by preventing framing.
- SECURE_CONTENT_TYPE_NOSNIFF: Prevents MIME-sniffing attacks.
- SECURE_BROWSER_XSS_FILTER: Enables browser XSS filtering protections.

## How this improves security
- Reduces man-in-the-middle risk by enforcing encrypted traffic.
- Limits cookie exposure on insecure channels.
- Adds browser-side protections against common web attacks (XSS, clickjacking, content-type sniffing).

## Potential Improvements
- Use environment variables to disable HTTPS redirects in local development.
- Configure SECURE_PROXY_SSL_HEADER when behind a reverse proxy.
- Add Content Security Policy (CSP) for stronger XSS mitigation.
