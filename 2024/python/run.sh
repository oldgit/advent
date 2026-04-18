#!/bin/sh
days="${1:-25}"
i=1
while [ "$i" -le $days ]; do
  day_file="day$i.py"
  if [ "$i" -lt 10 ]; then
    day_file="day0$i.py"
  fi
  if [ -f "$day_file" ]; then
    python "$day_file"
  fi
  i=$((i + 1))
done
