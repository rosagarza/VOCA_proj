#!/bin/bash
#!/usr/bin/python

echo "Script Usage: $0"
echo "Input File Name: $1"

python /Users/rosagarza/voca_proj/main.py
python /Users/rosagarza/voca_proj/pipeline.py $1

#gpt3=$(ls | grep * .mp3 | ls -tr  | tail -1)

#pwd

#echo "Output: $gpt3"

#cd $gpt3
#pwd

#mp3=$(ls | sort -n -t _ -k 2 | tail -1)
#echo "Mp3 file: $mp3"

#echo "PWD:"
#pwd

# INSERT mp3 TO VOCA

# TAKE VOCA OUTPUT AND PUT IT TO MAIN.PY FILE
# python /Users/rosagarza/voca_proj/main.py


echo "DONE!"