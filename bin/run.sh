#!/bin/bash
rand_mod=$(expr $RANDOM % 5)
if [ $rand_mod -eq 0 ]; then
    echo "Starting divisible by five app"
else
    echo "Crashing non-divisible by five app";
    exit 1
fi
# Set environment options to exit immediately if a non-zero status code
# appears from a command or within a pipe
set -o errexit
set -o pipefail

# Send out Slack notifications (off for now)
# invoke notify

cd fec
# Run migrations
./manage.py makemigrations
./manage.py migrate --noinput

# Run application
gunicorn -k gevent -w 2 fec.wsgi:application
