# MAaaS Deployment Guide

**Multi-Agent as a Service Enterprise Platform - Containerization & CI/CD**

This guide explains how to deploy the MAaaS platform using Docker and how the CI/CD pipeline works.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Local Docker Deployment](#local-docker-deployment)
4. [CI/CD Pipeline (GitHub Actions)](#cicd-pipeline-github-actions)
5. [Production Deployment](#production-deployment)
6. [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

The MAaaS platform is containerized using Docker and includes:

- **Backend API Service** (`maaas-backend`): FastAPI REST API server (port 8000)
- **Frontend Dashboard** (`maaas-frontend`): Streamlit command center (port 8501)
- **Factory Pipeline**: Interactive CLI for agent fabrication

### Architecture

```
┌─────────────────────────────────────────┐
│         Docker Compose Network          │
│                                         │
│  ┌──────────────┐    ┌──────────────┐  │
│  │ maaas-backend│    │maaas-frontend│  │
│  │  (FastAPI)   │◄───┤  (Streamlit) │  │
│  │   :8000      │    │    :8501     │  │
│  └──────────────┘    └──────────────┘  │
│         │                    │          │
│         └────────┬───────────┘          │
│                  │                      │
│         Shared Volumes:                 │
│         - clients/                      │
│         - factory_logs/                 │
│         - archives/                     │
│         - catalogue/                    │
└─────────────────────────────────────────┘
```

---

## 🔧 Prerequisites

### Local Development

- **Docker Desktop** (Windows/Mac) or **Docker Engine** (Linux)
- **Docker Compose** (usually included with Docker Desktop)
- **Git** (for cloning the repository)

### For CI/CD

- GitHub repository with Actions enabled
- No additional setup required (GitHub Actions runs in the cloud)

---

## 🐳 Local Docker Deployment

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aiwork400/MAaaS.git
   cd MAaaS
   ```

2. **Build and start services:**
   ```bash
   docker-compose up --build
   ```

   This will:
   - Build the Docker image from `Dockerfile`
   - Start both `maaas-backend` and `maaas-frontend` services
   - Mount local directories as volumes for data persistence

3. **Access the services:**
   - **API Server:** http://localhost:8000
   - **API Docs:** http://localhost:8000/docs
   - **Dashboard:** http://localhost:8501

### Running Individual Services

**Backend only:**
```bash
docker-compose up maaas-backend
```

**Frontend only:**
```bash
docker-compose up maaas-frontend
```

**In detached mode (background):**
```bash
docker-compose up -d
```

### Stopping Services

```bash
docker-compose down
```

**Remove volumes (⚠️ deletes data):**
```bash
docker-compose down -v
```

### Building Without Cache

```bash
docker-compose build --no-cache
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

### Workflow Overview

The CI/CD pipeline is defined in `.github/workflows/docker-build.yml` and automatically:

1. **Triggers:**
   - On push to `main` branch
   - On pull requests to `main`
   - Manual trigger via GitHub Actions UI

2. **Steps:**
   - ✅ Checkout code
   - ✅ Set up Docker Buildx (for advanced build features)
   - ✅ Build Docker image
   - ✅ Verify image exists
   - ✅ Test Python version in container
   - ✅ Test Python imports (verify dependencies)
   - ✅ Verify application files exist
   - ✅ Test FastAPI server import (dry run)

### Viewing Workflow Results

1. Go to your GitHub repository
2. Click on **Actions** tab
3. Select the workflow run
4. View logs for each step

### Workflow Status Badge

Add this to your `README.md`:

```markdown
![Docker Build](https://github.com/aiwork400/MAaaS/workflows/Docker%20Build%20%26%20Verify/badge.svg)
```

---

## 🚀 Production Deployment

### Environment Variables

Create a `.env` file (or set in `docker-compose.yml`):

```env
ENVIRONMENT=production
PYTHONUNBUFFERED=1
```

### Production Docker Compose

For production, consider:

1. **Remove `--reload` flag** in `docker-compose.yml`:
   ```yaml
   command: uvicorn api_server:app --host 0.0.0.0 --port 8000
   ```

2. **Use named volumes** instead of bind mounts:
   ```yaml
   volumes:
     - clients-data:/app/clients
     - factory-logs-data:/app/factory_logs
   ```

3. **Add reverse proxy** (nginx/traefik) for SSL/TLS

4. **Set resource limits:**
   ```yaml
   deploy:
     resources:
       limits:
         cpus: '2'
         memory: 2G
   ```

### Docker Image Registry

To push to a registry (Docker Hub, GitHub Container Registry, etc.):

```bash
# Tag the image
docker tag maaas-platform:latest your-registry/maaas-platform:latest

# Push
docker push your-registry/maaas-platform:latest
```

---

## 🔍 Troubleshooting

### Common Issues

#### 1. **Port Already in Use**

**Error:** `Bind for 0.0.0.0:8000 failed: port is already allocated`

**Solution:**
```bash
# Find process using port
netstat -ano | findstr :8000  # Windows
lsof -i :8000                  # Linux/Mac

# Stop the process or change port in docker-compose.yml
```

#### 2. **Permission Denied (Linux/Mac)**

**Error:** `Permission denied` when accessing volumes

**Solution:**
```bash
# Fix permissions
sudo chown -R $USER:$USER clients/ factory_logs/ archives/
```

#### 3. **Docker Build Fails**

**Error:** `ERROR: failed to solve: process "/bin/sh -c pip install..."`

**Solution:**
- Check `requirements.txt` for invalid packages
- Verify internet connection
- Try building without cache: `docker-compose build --no-cache`

#### 4. **Container Exits Immediately**

**Error:** Container starts then stops

**Solution:**
```bash
# Check logs
docker-compose logs maaas-backend
docker-compose logs maaas-frontend

# Run container interactively
docker run -it --rm maaas-platform:latest /bin/bash
```

#### 5. **GitHub Actions Fails**

**Error:** Workflow fails at build step

**Solution:**
- Check workflow logs in GitHub Actions tab
- Verify `Dockerfile` syntax
- Ensure all files are committed (not in `.gitignore`)

---

## 📝 Development Workflow

### Making Changes

1. **Edit code locally**
2. **Test locally:**
   ```bash
   docker-compose up --build
   ```
3. **Commit and push:**
   ```bash
   git add .
   git commit -m "Your changes"
   git push origin main
   ```
4. **GitHub Actions automatically verifies the build**

### Hot Reload

The `docker-compose.yml` includes `--reload` flags for development:

- **FastAPI:** Auto-reloads on code changes
- **Streamlit:** Auto-reloads on code changes

Changes to files in mounted volumes are reflected immediately.

---

## 🔐 Security Considerations

1. **Never commit secrets** (API keys, passwords) to the repository
2. **Use environment variables** for sensitive configuration
3. **Keep dependencies updated:** Regularly update `requirements.txt`
4. **Scan images:** Use tools like `trivy` or `snyk` to scan Docker images

---

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Streamlit Deployment](https://docs.streamlit.io/deploy)

---

## ✅ Verification Checklist

After deployment, verify:

- [ ] Docker image builds successfully
- [ ] Both services start without errors
- [ ] API server responds at http://localhost:8000/health
- [ ] Dashboard loads at http://localhost:8501
- [ ] GitHub Actions workflow passes
- [ ] Volumes persist data correctly
- [ ] Logs are accessible via `docker-compose logs`

---

**Last Updated:** 2025-12-22  
**Maintained by:** Swarm Agency Prime Orchestrator

