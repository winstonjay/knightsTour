#!/bin/bash
set -e

dt=$(date '+%d%m%y-%H%M%S');
SRT=5
END=50
FILENAME=testlogs/t$dt-TEST-$SRT-$END.json

echo "[" > $FILENAME
for ((i=SRT;i<=END;i++)); do
    python tests.py $i 
done >> $FILENAME
echo "]" >> $FILENAME