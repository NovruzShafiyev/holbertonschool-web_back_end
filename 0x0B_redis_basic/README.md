# Redis Cache Project

This project implements a Cache class that interfaces with a Redis database to store and retrieve data with randomly generated keys, as well as counting method calls, storing call history, and replaying call history.

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
