# Log File Analysis Tool

# Overview
The Log File Analysis Tool is a Python-based solution for analyzing server log files. This project is designed to detect suspicious activity, track request counts per IP address, and identify the most frequently accessed endpoints, providing actionable insights from log data. Results are displayed in the terminal and saved to a CSV file for further analysis.

# Features

# Requests per IP Address:
* Analyze how many requests each IP address made.
* Identify potentially malicious actors or high traffic sources.

 # Suspicious Activity Detection:
* Detect brute force login attempts based on failed login thresholds.
* Flag IP addresses exceeding a specified limit for failed login attempts.

# Most Accessed Endpoint:
Determine the most frequently accessed URLs in the log data.

# CSV Export:
Results are saved in log_analysis_results.csv with organized data for easy access.
# File Structure
log_analysis.py: Main script containing all analysis functions.
logfile.log: Sample log file for testing and demonstration.
log_analysis_results.csv: Output file with analysis results.
README.md: Documentation for the project.

# Installation
Clone the repository:
git clone https://github.com/JAGADISHTIDKE-24/VRV_Python-assignment.git

Navigate to the project directory:

cd VRV_Python-assignment

Install dependencies (if any) using pip:
pip install -r requirements.txt
cd VRV_Python-assignment

Install dependencies (if any) using pip:
pip install -r requirements.txt

# Usage
Place your log file (e.g., logfile.log) in the project directory.
Run the script:
python log_analysis.py
View results in the terminal and check the generated log_analysis_results.csv file.

# CSV File Structure
The CSV file contains three sections:

#1.Requests per IP Address:

IP Address
Request Count

#2.Most Accessed Endpoint:

Endpoint
Access Count

# 3.Suspicious Activity:

IP Address
Failed Login Count

# Example Output
Terminal Output:

Requests per IP Address:
192.168.1.1   15 requests
203.0.113.5   8 requests

Most Accessed Endpoint:
/home accessed 10 times

Suspicious Activity Detected:
203.0.113.5   8 failed login attempts
CSV File Content:

mathematica
Copy code
Requests per IP Address:

IP Address,Request Count
192.168.1.1,15
203.0.113.5,8

Most Accessed Endpoint:
Endpoint,Access Count
/home,10

Suspicious Activity:
IP Address,Failed Login Count
203.0.113.5,8

# License
This project is licensed under the MIT License. See the LICENSE file for details.
