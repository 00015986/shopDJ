# ShopDJ — Django E-Commerce Platform

A full-stack e-commerce application built with Django 4.2, containerized with Docker,
and deployed with automated CI/CD using GitHub Actions.

**Live Project:** https://dscc-cw1-project-shopdj-00015986.uaenorth.cloudapp.azure.com/
---
**User:** Create your own user to test the platform
---

##  Features

### Customer Features
- Browse products by category
- Session-based shopping cart (no login required)
- User registration and authentication
- Secure checkout with order creation
- Order history and tracking
- Product search and filtering

### Admin Features
- Product management (CRUD operations)
- Category and tag management
- Order management with status updates
- User management
- Inline order item editing

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django 4.2, Python 3.11 |
| **Database** | PostgreSQL 15 |
| **Web Server** | Gunicorn (WSGI), Nginx (reverse proxy) |
| **Frontend** | HTML5, CSS3, Bootstrap 5, Django Templates |
| **Containerization** | Docker, Docker Compose |
| **CI/CD** | GitHub Actions (Phase 5) |
| **Media Storage** | Local file system (Pillow) |
| **Security** | HTTPS with Let's Encrypt (Phase 5) |

---

##  Database Schema

```
Category (1) ──< Product (many)     # Many-to-One
Product (many) >──< Tag (many)      # Many-to-Many
User (1) ──< Order (many)           # Many-to-One
Order (1) ──< OrderItem (many)      # One-to-Many
```

### Models

1. **Category** — Product categories (Electronics, Clothing, etc.)
2. **Tag** — Product tags (new, sale, bestseller)
3. **Product** — Main product model with images, pricing, stock
4. **Order** — Customer orders with status tracking
5. **OrderItem** — Line items linking orders to products

---

##  Quick Start

### Prerequisites

- Docker Desktop (Windows/Mac/Linux)
- Git
- A code editor (VS Code recommended)

### Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/00015986/shopDJ.git
   cd shopDJ
   ```

2. **Create .env file:**
   ```bash
   # Copy the example (create .env.example first based on this)
   cp .env.example .env
   ```

   Edit `.env` with your values:
   ```
   SECRET_KEY=your-secret-key-here-make-it-long-and-random
   DEBUG=True [or False for Production]
   ALLOWED_HOSTS=localhost,127.0.0.1
   DB_NAME=shopdb
   DB_USER=shopuser
   DB_PASSWORD=yourpassword
   DB_HOST=db
   DB_PORT=5432
   ```

3. **Build and start containers:**
   ```bash
   docker compose up --build -d
   ```

4. **Run migrations:**
   ```bash
   docker compose exec web python manage.py migrate
   ```

5. **Create superuser:**
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

6. **Collect static files:**
   ```bash
   docker compose exec web python manage.py collectstatic --noinput
   ```

7. **Visit the site:**
   - Homepage: http://localhost
   - Admin: http://localhost/admin/

---

##  Running Tests

```bash
# Run all tests
docker compose exec web pytest -v

# Run with coverage
docker compose exec web pytest --cov=. --cov-report=html

# Run specific test file
docker compose exec web pytest tests/test_shop.py -v
```

---

##  Docker Configuration

### Services

- **db** — PostgreSQL 15 database with healthcheck
- **web** — Django/Gunicorn application (3 workers)
- **nginx** — Reverse proxy serving static files

### Multi-Stage Build
The Dockerfile uses a 2-stage build:
1. **Builder stage** — Installs build tools, compiles Python packages
2. **Production stage** — Copies only compiled packages, runs as non-root user

**Result:** Image size 194MB which is less than 200MB (vs 800MB+ without multi-stage)

---

##  Project Structure

```
shopDJ/
├── config/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shop/                # Product catalog app
│   ├── models.py        # Category, Product, Tag
│   ├── views.py
│   ├── admin.py
│   └── urls.py
├── cart/                # Shopping cart app
│   ├── cart.py          # Session-based cart logic
│   └── views.py
├── orders/              # Order management app
│   ├── models.py        # Order, OrderItem
│   └── views.py
├── accounts/            # User authentication app
├── templates/           # HTML templates
├── nginx/              
│   └── nginx.conf       # Nginx configuration
├── tests/               # Pytest test suite
├── Dockerfile           # Multi-stage Docker build
├── docker-compose.yml   # Container orchestration
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

##  Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key (50+ random chars) | `django-insecure-abc123...` |
| `DEBUG` | Enable debug mode (False in production) | `True` / `False` |
| `ALLOWED_HOSTS` | Comma-separated allowed hostnames | `localhost,yourdomain.uz` |
| `DB_NAME` | PostgreSQL database name | `shopdb` |
| `DB_USER` | PostgreSQL username | `shopuser` |
| `DB_PASSWORD` | PostgreSQL password | `yourpassword` |
| `DB_HOST` | Database hostname | `db` (Docker service name) |
| `DB_PORT` | Database port | `5432` |

---

##  Assignment Requirements Met

 **Django Models:** 5 models (Category, Tag, Product, Order, OrderItem)
 **Relationships:** Many-to-One (Product→Category), Many-to-Many (Product↔Tag)
 **CRUD Operations:** Full admin panel and customer-facing views
 **Authentication:** User registration, login, logout
 **Admin Panel:** Customized with list_display, list_editable, search
 **Docker:** Multi-stage Dockerfile, docker-compose with 3 services
 **Image Size:** < 194 MB
 **Testing:** 6 plus pytest tests
 **Git:** 15 plus commits, feature branch
 **Documentation:** This README

---

##  Contributing

This is a student project for DSCC coursework. Not accepting external contributions.

---
##  Working Website Screenshots
<img width="1891" height="854" alt="image" src="https://github.com/user-attachments/assets/947bb352-3186-4325-a907-77f5e07597ba" />
<img width="1900" height="675" alt="image" src="https://github.com/user-attachments/assets/661b03cc-2476-4ab9-bae0-86b8b364658a" />
<img width="1895" height="518" alt="image" src="https://github.com/user-attachments/assets/164b902f-9ce3-4f70-8234-91b5352e72e8" />
<img width="1904" height="467" alt="image" src="https://github.com/user-attachments/assets/a9fd601e-bfff-432f-a5b4-fb4d70d434f1" />
<img width="1894" height="768" alt="image" src="https://github.com/user-attachments/assets/d786d1c2-f883-49cb-9c2e-25ba4f32077f" />

---
##  License

This project is for educational purposes only.

---

##  Author

**Student ID:** 00015986
**Course:** DSCC Coursework 1
**Year:** 2026
