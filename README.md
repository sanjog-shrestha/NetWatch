\# 🌐 NetWatch - Network Monitoring System



\[!\[Docker](https://img.shields.io/badge/Docker-Containerized-blue)](https://www.docker.com/)

\[!\[Python](https://img.shields.io/badge/Python-3.11-green)](https://www.python.org/)

\[!\[License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)



A lightweight, containerized network monitoring solution that tracks latency and packet loss to critical infrastructure targets. Built with DevOps principles, it's designed to evolve from a simple ping monitor to a full-featured observability platform.



\## 🚀 Quick Start



```bash

\# Clone repository

git clone https://github.com/yourusername/netwatch.git

cd netwatch



\# Build and run

docker build -t netwatch:v1 .

docker run -d --name netwatch -v $(pwd)/logs:/logs netwatch:v1



\# View logs

tail -f logs/netwatch.log

