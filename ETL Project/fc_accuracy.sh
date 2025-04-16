#!/bin/bash

# Extract yesterday's forecasted temperature (line before last)
yesterday_fc=$(tail -2 rx_poc.log | head -1 | cut -d " " -f5)

# Extract today's observed temperature (last line)
today_temp=$(tail -1 rx_poc.log | cut -d " " -f4)

# Remove '°C' or any non-digit characters
yesterday_fc=$(echo "$yesterday_fc" | tr -d -c 0-9)
today_temp=$(echo "$today_temp" | tr -d -c 0-9)

# Calculate the accuracy (difference between forecast and actual)
accuracy=$((yesterday_fc - today_temp))

echo "Accuracy is $accuracy"

# Determine accuracy range
if [ "$accuracy" -ge -1 ] && [ "$accuracy" -le 1 ]; then
    accuracy_range="excellent"
elif [ "$accuracy" -ge -2 ] && [ "$accuracy" -le 2 ]; then
    accuracy_range="good"
elif [ "$accuracy" -ge -3 ] && [ "$accuracy" -le 3 ]; then
    accuracy_range="fair"
else
    accuracy_range="poor"
fi

echo "Forecast accuracy is $accuracy_range"

# Extract date from last log entry
row=$(tail -1 rx_poc.log)
year=$(echo "$row" | cut -d " " -f1)
month=$(echo "$row" | cut -d " " -f2)
day=$(echo "$row" | cut -d " " -f3)

# Save results to TSV file
echo -e "$year\t$month\t$day\t$today_temp\t$yesterday_fc\t$accuracy\t$accuracy_range" >> historical_fc_accuracy.tsv
