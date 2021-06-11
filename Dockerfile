FROM python:3.7-alpine3.13

LABEL maintainer="Romain Pfund <romain.pfund@rpinfo.ch>"

ARG version=52.5

RUN apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev cairo cairo-gobject pango gdk-pixbuf py3-lxml py3-cffi py3-pillow msttcorefonts-installer fontconfig

RUN update-ms-fonts && fc-cache -f

RUN pip install pyyaml

RUN pip install weasyprint==$version

WORKDIR /app

COPY . .

RUN chmod +x /app/convert_multiple.py

RUN mkdir /app/output

RUN mkdir /app/logs

ENTRYPOINT ["python", "/app/convert_multiple.py"]
