FROM nginx:1.15.8

RUN apt update &&  apt install openssl
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY project.conf /etc/nginx/conf.d/
COPY sel-ssl.sh /
RUN chmod +x /sel-ssl.sh && /sel-ssl.sh

