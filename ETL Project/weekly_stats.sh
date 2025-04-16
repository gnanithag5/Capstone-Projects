#!/bin/bash

echo "Processing last 7 days of forecast accuracy data..."
echo

# Step 1: Extract last 7 forecast accuracy values into scratch.txt
tail -7 synthetic_historical_fc_accuracy.tsv | cut -f6 > scratch.txt

# Step 2: Load into array
week_fc=($(cat scratch.txt))

echo "Raw forecast errors (may include negatives):"
for i in {0..6}; do
    echo "Day $((i+1)): ${week_fc[$i]}"
done

echo
echo "Converting to absolute errors..."

# Step 3: Convert to absolute values
for i in {0..6}; do
    if [[ ${week_fc[$i]} -lt 0 ]]; then
        week_fc[$i]=$(( -1 * ${week_fc[$i]} ))
    fi
    echo "Day $((i+1)) absolute error: ${week_fc[$i]}"
done

# Step 4: Calculate min and max
minimum=${week_fc[0]}
maximum=${week_fc[0]}
for item in "${week_fc[@]}"; do
    if [[ $item -lt $minimum ]]; then
        minimum=$item
    fi
    if [[ $item -gt $maximum ]]; then
        maximum=$item
    fi
done

echo
echo "===== Weekly Forecast Accuracy Summary ====="
echo "Minimum absolute error over the last 7 days: $minimum"
echo "Maximum absolute error over the last 7 days: $maximum"
echo "============================================"
