# Redis Cache Project

This project implements a Cache class that interfaces with a Redis database to store data with randomly generated keys.

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- Redis

## Installation

1. Install Redis on Ubuntu 18.04:
   ```bash
   sudo apt-get -y install redis-server
   pip3 install redis
   sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
