FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /usr/wb_api
COPY requirements.txt /usr/wb_api/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /usr/wb_api/

COPY start.sh /usr/wb_api/start.sh
RUN chmod +x /usr/wb_api/start.sh
ENTRYPOINT '/usr/wb_api/start.sh'