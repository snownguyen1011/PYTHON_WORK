#!/bin/bash
CSV_FILE=$1

input="./csv2htmlfile.csv"
#output= "artifactStatus.html"

#while IFS= read -r line
#do
#  #sed -e "s/,Exist/,<font color=green>Exist<\/font>/g" "$line"
#  #sed -e "s/,Not Exist/,<font color=red>Exist<\/font>/g" "$line"
#  sed -e "s/,Not Exist/,<font color=red>Not Exist<\/font>/g"  -e "s/,Exist/,<font color=green>Exist<\/font>/g" -e 's/^/<tr><td>/g' -e 's/$/<\/td><\/tr>/g' -e 's/,/<\/td><td>/g' "$line"
#  echo "$line"
#done < "$input"

#printf '<html><head>ARTIFACT STATUS LIST ON NEXUS</head><body><table><thead><tr><th>Name</th><th>Version</th><th>Status</th></tr></thead><tbody>'
echo """<html><head>ARTIFACT STATUS LIST ON NEXUS</head>
<body><table><thead>
<tr><th>Name</th><th>Version</th><th>Status</th></tr></thead><tbody>""" > artifactStatus.html
sed -e "s/,Not Exist/,<font color=red>Not Exist<\/font>/g"  -e "s/,Exist/,<font color=green>Exist<\/font>/g" -e 's/^/<tr><td>/g' -e 's/$/<\/td><\/tr>/g' -e 's/,/<\/td><td>/g' "$input" >> artifactStatus.html

echo  "<\tbody><\table><\body><\html>" >> artifactStatus.html




#sed -e "s/<\/tbody><\/table><\/body><\/html>/$/g" "$input" >> artifactStatus.html
#sed -e "s/,Not Exist/,<font color=red>Not Exist<\/font>/g"  -e "s/,Exist/,<font color=green>Exist<\/font>/g" -e 's/^/<tr><td>/g' -e 's/$/<\/td><\/tr>/g' -e 's/,/<\/td><td>/g' "$CSV_FILE"
#sed -e "s/,Exist/,<font color=green>Exist<\/font>/g" "$CSV_FILE"

#sed  -e 's/^/<tr><td>/g' -e 's/$/<\/td><\/tr>/g' -e 's/,/<\/td><td>/g' "$CSV_FILE"
#printf '</tbody></table></body></html>'
#sed -e "s/^/<html><head>ARTIFACT STATUS LIST ON NEXUS<\/head><body><table><thead><tr><th>Name<\/th><th>Version<\/th><th>Status<\/th><\/tr><\/thead><tbody>'/g" "$CSV_FILE"

#sed -e "s/$/<\/tbody><\/table><\/body><\/html>/g" "$CSV_FILE"







