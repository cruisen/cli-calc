#! /bin/ksh

cloc_sink="./dev_tools/meters"
ext="json"
shield="shields"
dirs="cli_calc tests"

cloc_cmd="cloc --include-lang Python --quiet --json --report-file"

for dir in $dirs
do
  cloc_in=./$dir
  cloc_out=$cloc_sink/$dir.$ext
  shield_out=$cloc_sink/${dir}_$shield.$ext

  cmd="$cloc_cmd=$cloc_out $cloc_in"
  $cmd1

  old=$(jq .message $shield_out | tr -d '"')
  new=$(jq .Python.code $cloc_out)

  sed -i .bak "s/$old/$new/g" $shield_out

done

echo "DONE"



