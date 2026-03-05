echo "----- System Report -----" > /home/$USER/system_report.txt

echo "Date:" >> /home/$USER/system_report.txt
date >> /home/$USER/system_report.txt

echo "-------------------------" >> /home/$USER/system_report.txt

echo "System Uptime:" >> /home/$USER/system_report.txt
uptime >> /home/$USER/system_report.txt

echo "-------------------------" >> /home/$USER/system_report.txt

echo "Disk Usage:" >> /home/$USER/system_report.txt
df -h >> /home/$USER/system_report.txt

echo "-------------------------" >> /home/$USER/system_report.txt

echo "Memory Usage:" >> /home/$USER/system_report.txt
free -h >> /home/$USER/system_report.txt

echo "-------------------------" >> /home/$USER/system_report.txt

echo "Logged in Users:" >> /home/$USER/system_report.txt
who >> /home/$USER/system_report.txt

echo "-------------------------" >> /home/$USER/system_report.txt

echo "Running Processes:" >> /home/$USER/system_report.txt
ps aux >> /home/$USER/system_report.txt

echo "System report generated successfully."
