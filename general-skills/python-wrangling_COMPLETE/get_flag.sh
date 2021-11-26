#!/bin/bash

curl "https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py" -o ende.py 2>/dev/null
curl "https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/pw.txt" -o pw.txt 2>/dev/null
curl "https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/flag.txt.en" -o flag.txt.en 2>/dev/null
cat pw.txt | python3 ende.py -d flag.txt.en | cut -d : -f2
