#! /bin/bash
# Changes all file names in the current directory to lowercase

cnt=0 #여기도?
for filename in *
do
	fname=$(basename 	$filename)
	cname=$(echo $fname | tr A-Z a-z)
	if [ "$fname" !=  "$cname" ] 
	then
		if [ -e  "$cname" ]
		then 
		   echo  	"$cname already exists"
		   exit 1
		fi
		echo "$fname is renamed $cname"
		mv $fname $cname
		cnt=$(( ${cnt}+1 ))
	fi
done
echo "Total count: $cnt"
exit 0
