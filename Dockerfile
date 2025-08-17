FROM python:3.10.0-slim

WORKDIR /app

# In the Dockerfile, requirements.txt is copied first so Docker can cache
# the dependency installation layer. This way, unless requirements.txt changes
# Docker reuses the cached layer, speeding up builds by avoiding reinstalling
#  dependencies each time.
COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
# Behind a TLS Termination Proxy
# If you are running your container 
# behind a TLS Termination Proxy (load balancer) like Nginx or Traefik,
# add the option --proxy-headers, this will tell Uvicorn (through the FastAPI CLI)
# to trust the headers sent by that proxy telling it that the application is
# running behind HTTPS, etc.

RUN ls

CMD ["fastapi", "run", "app/main.py", "--proxy-headers", "--port", "80"]