#!/bin/sh
i=1
while [ "$i" -le 25 ]; do
  day_file="day$i.py"
  if [ "$i" -lt 10 ]; then
    day_file="day0$i.py"
  fi
  python "$day_file"
  i=$(( i + 1 ))
done