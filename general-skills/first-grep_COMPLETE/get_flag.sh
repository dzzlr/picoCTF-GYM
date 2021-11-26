#!/bin/bash

curl "https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file" -o file 2>/dev/null
grep 'picoCTF' file
