# SECURITY POLICY

## Supported Versions

This project supports the latest development version.

| Version | Supported |
| ------- | --------- |
| 1.0.x   | ✅ |

---

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly.

Contact:
- CyberLab Security Team
- Email: security@cyberlab.local

Please include:
- Vulnerability description
- Steps to reproduce
- Possible impact

---

## Security Measures Implemented

- Authentication system using Django Auth
- Role-based access control (Admin / Analyst)
- Protected routes using @login_required
- PostgreSQL secure database integration
- CSRF protection enabled
- Restricted edit/delete permissions
- Secure password hashing with Django

---

## User Roles

### Admin

Can:
- Create incidents
- Edit incidents
- Delete incidents
- Access dashboard

### Analyst

Can:
- View incidents
- Create incidents
- Access dashboard

Cannot:
- Edit incidents
- Delete incidents