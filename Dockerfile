FROM python:3.11-slim
WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y git
RUN pip install aiodns>=3.2.0 aiofiles>=23.2.1 alive_progress>=3.1.4 art>=6.1 \
    colorama>=0.4.6 requests>=2.31.0 urllib3>=1.26.18 uvloop>=0.21.0
RUN pip install --no-deps --force-reinstall --break-system-packages git+https://github.com/RevoltSecurities/Dnsbruter.git

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["dnsbruter"]
