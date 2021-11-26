#!/bin/bash

curl "https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm" -o warm 2>/dev/null
chmod +x warm
./warm -h | cut -d : -f2 | cut -d " " -f2
