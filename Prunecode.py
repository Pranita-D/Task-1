#!/usr/bin/env python3
import subprocess
import datetime

# 30 minutes ago
minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=30)
date_str = minutes_ago.strftime("%Y-%m-%dT%H:%M:%S")

# Prune Docker images older than 30 minutes
subprocess.run(['docker', 'image', 'prune', '-a', '--filter', 'until=' + date_str, '-f'])

# Prune Docker containers older than 30 minutes
subprocess.run(['docker', 'container', 'prune', '--filter', 'until=' + date_str, '-f'])
