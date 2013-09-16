#! /usr/bin/env bash
dataset=$1
func=$2
echo $dataset >> proj1d.txt
echo $func >> proj1d.txt
python readered.py $dataset "both" >> proj1d.txt
