#!/bin/bash

mkdir -p data

wget https://raw.githubusercontent.com/mhjabreel/CharCNN/master/data/ag_news_csv/train.csv

mv train.csv data
