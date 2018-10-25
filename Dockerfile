FROM tiangolo/uwsgi-nginx:python3.6

# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/
# Copy app
COPY ./app /app
# Install Requirements
RUN \
  apt-get update && \
  apt-get install -y vim git wget && \
  apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev
RUN pip install -r /app/requirements.txt
# Make it possible to mount nginx configuration outside the container
VOLUME ["/etc/nginx/conf.d"]
EXPOSE 5050
