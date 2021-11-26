#!/bin/bash

curl "https://mercury.picoctf.net/static/659efd595171e4c40378be6a2e9b7298/Addadshashanammu.zip" -o Addadshashanammu.zip 2>/dev/null
unzip -o -qq Addadshashanammu.zip
cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
./fang-of-haynekhtnamet | cut -d " " -f2
