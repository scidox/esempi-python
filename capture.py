#!/usr/bin/env python3
import subprocess
result=subprocess.run(["host","google.it"],capture_output=True)
print(result.stdout.decode().split())
