#!/usr/bin/env sh

if [ $# -ne 1 ]
then
    echo "Please enter input file from ex03 or any other with extension .csv"
else
{
    awk ' BEGIN { FS = "\",\"|T" }
        {
            if (NR == 1)
                START = $0
            else
            {
                if (!($2 in files))
                {
                    file = $2".csv"
                    files[$2]
                    print START > file
                }
                print >> file
            }
        }
        ' $1
}
fi