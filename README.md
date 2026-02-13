# Full Functional Project

A comprehensive deployment solution featuring Docker containers, automated installation scripts, and a Tomcat application server with MySQL database.

## Project Overview

This project provides a containerized setup with automated installation capabilities for deploying applications across different environments (Linux and Windows).

## Project Structure

```
├── docker-compose.yml       # Docker Compose configuration for multi-container setup
├── installer.py             # Python installer script
├── installer.spec           # PyInstaller specification
├── server.properties        # Server configuration file
├── env.template             # Environment variables template
│
├── assets/
│   └── init.sql            # Database initialization script
│
├── docker/
│   ├── mysql/              # MySQL Docker configuration
│   │   ├── Dockerfile
│   │   └── my.cnf          # MySQL configuration
│   └── tomcat/             # Tomcat Docker configuration
│       └── Dockerfile
│
└── scripts/
    ├── install_docker_linux.sh      # Linux Docker installation script
    └── install_docker_windows.ps1   # Windows Docker installation script
```

## Prerequisites

- Docker and Docker Compose
- Python 3.x (for running the installer)
- Administrator/root access (for Docker installation)

## Quick Start

### 1. Environment Setup

Copy the template environment file and configure your settings:

```bash
cp env.template .env
# Edit .env with your configuration
```

### 2. Docker Setup

#### Windows:
```powershell
.\scripts\install_docker_windows.ps1
```

#### Linux:
```bash
bash scripts/install_docker_linux.sh
```

### 3. Deploy with Docker Compose

```bash
docker-compose up -d
```

This will start:
- **MySQL Database** - Initialized with `assets/init.sql`
- **Tomcat Server** - Running on port 8080

### 4. Run Installer

```bash
python installer.py
```

## Configuration

- **`server.properties`** - Configure server settings
- **`docker/mysql/my.cnf`** - MySQL configuration
- **`assets/init.sql`** - Database schema and initialization

## Services

### MySQL
- Container: MySQL database service
- Configuration: `docker/mysql/my.cnf`
- Initialization: `assets/init.sql`

### Tomcat
- Container: Apache Tomcat application server
- Default Port: 8080
- Configuration: `docker/tomcat/Dockerfile`

## Support

For issues or questions, refer to individual component documentation or check container logs:

```bash
docker-compose logs -f
```

## License

[Add your license information here]
