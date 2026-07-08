info_count=0
error_count=0
warn_count=0

#Function to analyze the log line
analyze_log(){
file=$1

if echo "$line" | grep -q "INFO"
then
((info_count++))
elif echo "$line" | grep -q "WARNING"
then
((warn_count++))
else
((error_count++))
fi
}

#Function to determine the system status
check_status(){
status=""
if [[ $error_count -gt 10 ]]
then
	status="Critical"
elif [[ $error_count -gt 0 ]]
then
	status="Warning"
else
	status="Healthy"
fi
}

#Read input line
echo "Enter log file: "
read logfile

if [[ -f logfile ]]
then
	echo "File doesnot exist"
	exit
fi

#Loop through the file
while read line
do
analyze_log "$line"
done < $logfile

#Determine status
check_status

#Generate Report
{
echo "System Log Analyzer report"
echo "==========================="
echo "INFO Count: $info_count"
echo "WARNING Count: $warn_count"
echo "ERROR Count: $error_count"
echo
echo "System Status: $status"
} > report.txt

echo "Report generated: report.txt"
