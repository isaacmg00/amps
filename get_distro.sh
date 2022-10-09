#!/bin/sh

distribution_json=$(distro -j)
echo $distribution_json
out=$distribution_json | jq -r '.id'
echo $out