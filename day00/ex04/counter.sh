#!/usr/bin/env sh

if [ $# -eq 0 ]
then my_path="../ex03/hh_positions.csv"
else
  my_path=$1
fi
echo '"name","count"' > hh_uniq_positions.csv
cat ${my_path} \
  | awk 'BEGIN{FS=OFS=",";} NR>1 {print $3;}' \
  | sort \
  | uniq -c \
  | sort -t ',' -r -k 2 \
  | awk 'BEGIN{OFS=","} {print $2, $1;}' \
  >>  hh_uniq_positions.csv