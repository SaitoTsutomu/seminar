Like tmpnb for seminar.  [![](https://badge.imagelayers.io/tsutomu7/seminar:latest.svg)](https://imagelayers.io/?images=tsutomu7/seminar:latest)
========

## Step 1. Making volume for python

```bash:bash
docker volume rm python
docker run -it --rm -v python:/usr/local tsutomu7/py3flask sh -c "\
    cp /usr/bin/python3.5 /usr/local/bin/python && \
    cp /lib/ld-musl-x86_64.so.1 /usr/local/lib && \
    ln -s /usr/local/lib/ld-musl-x86_64.so.1 /usr/local/lib/libc.musl-x86_64.so.1 && \
    cp /usr/lib/libpython3.5m.so.1.0 /usr/local/lib/ && \
    cp -r /usr/lib/python3.5/ /usr/local/lib/"
docker volume ls
```

## Step 2. Start server

```bash:bash
docker run -it --rm \
   -v /lib/x86_64-linux-gnu/:/lib/x86_64-linux-gnu/:ro \
   -v /lib64:/lib64:ro \
   -v /usr/bin:/usr/bin:ro \
   -v /usr/lib:/usr/lib:ro \
   -v /var/run/docker.sock:/var/run/docker.sock:ro \
   -v python:/usr/local \
   -p 5000:5000 \
   -e IMAGE=tsutomu7/jupyter \
   -e PORT=8888 \
   tsutomu7/seminar
```

if there is no "/lib/x86_64-linux-gnu" then omit it.

### Docker environment
- IMAGE: A docker image name for auto starting.
- PORT: A port number for an IMAGE.

## Step 3. Access
Open "http://[your host]:5000"
