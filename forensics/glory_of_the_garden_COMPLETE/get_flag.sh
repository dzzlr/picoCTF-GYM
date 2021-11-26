#!/bin/bash

strings garden.jpg | tail -n 1 | cut -d '"' -f2
