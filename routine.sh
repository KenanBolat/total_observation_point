#!/usr/bin/bash
while getopts d:f: flag; do
  case "${flag}" in
  d) date_=${OPTARG} ;;
  f) file=${OPTARG} ;;
  *) file="" ;;
  esac
done


if [[ -z "$file" ]];
 then
  echo "NO file provided"
else
  start=$(date +%s)

# ignore overlap
export SKIP_SAME_TIME=1

cdo mergetime test1.nc test2.nc merged.nc
cdo mergetime test1.nc test2.nc merged_skipped.nc
cdo showtimestamp merged_skipped.nc


end=$(date +%s)
runtime=$((end - start))
echo "$file has been exhausted within $runtime "