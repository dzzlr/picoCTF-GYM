#!/bin/bash

curl "https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings" -o strings 2>/dev/null
strings strings | grep 'picoCTF'
