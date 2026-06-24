# NetWatch v1

A lightweight Dockerized network monitoring service that continuously checks internet connectivity by pinging multiple public endpoints and logging latency/packet-loss information.

## Features

- Monitors network connectivity using ICMP ping
- Pings multiple targets every 30 seconds
- Records latency measurements
- Detects packet loss
- Writes logs to persistent storage
- Runs inside a Docker container
- Simple and resource-efficient design

---

## Architecture

```text
+----------------------+
|  NetWatch Container  |
+----------+-----------+
           |
           v
    +-------------+
    |  ping3 ICMP |
    +-------------+
           |
           v
+-----------------------+
| Targets              |
| - 8.8.8.8 (Google)   |
| - 1.1.1.1 (Cloudflare)|
+-----------------------+
           |
           v
+-----------------------+
| Logging System        |
| /logs/netwatch.log    |
+-----------------------+
```

## Project Structure

```text
netwatch/
├── Dockerfile
├── requirements.txt
├── src/
│   └── monitor.py
├── logs/
└── docker-compose.yml
```

## Build

```bash
docker build -t netwatch:v1 .
```

## Run

```bash
mkdir -p logs

docker run -d \
  --name netwatch \
  -v $(pwd)/logs:/logs \
  netwatch:v1
```

## View Logs

```bash
tail -f logs/netwatch.log
```

## Stop

```bash
docker stop netwatch
docker rm netwatch
```

## Roadmap

- Phase 2: Environment variables and health checks
- Phase 3: Prometheus and Grafana integration
- Phase 4: Alerting and dashboard

## License

MIT
