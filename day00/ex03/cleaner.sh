#!/bin/sh
if [ $# -eq 0 ]
then my_path="../ex02/hh_sorted.csv"
else
  my_path=$1
fi
head -n 1 ${my_path} > hh_positions.csv
tail -n 20 ${my_path} | \
awk \
    'BEGIN{
      FS=OFS="\",";
      Regexes[0] = "[Jj]unior\\+?[/\]?";
      Regexes[2] = "[Mm]iddle\\+?[/\]?";
      Regexes[4] = "[Ss]enior";
    }
    {
      result = "";
      for (i = 0; i < length(Regexes); ++i)
      {
        match($3, Regexes[i]);
        if (RLENGTH > 0) {
          first_char = substr($3, RSTART, 1);
          if (length(result) > 0) {
              result = result "/";
          }
          result = result toupper(first_char) substr($3, RSTART + 1, RLENGTH - 1);
        }
      }
      if (length(result) == 0) {
        $3 = "\"-";
      }
      else {
        $3 = "\"" result;
      }
      print;
    }' \
    >> hh_positions.csv