import re  # Import the "re" module to work with regular expressions
from collections import defaultdict  # Import "defaultdict" to handle default values for a dictionary

# Function to check for suspicious activity in a log file
def detect_suspicious_activity(log_file_path, threshold=10):
    # Create a dictionary to count failed login attempts for each IP address
    failed_logins = defaultdict(int)

    # Define a pattern to look for failed login attempts (HTTP status code 401)
    failed_login_pattern = r'401'

    # Open the log file and read it line by line
    with open(log_file_path, 'r') as file:
        for line in file:  # Loop through each line in the file
            # Check if the line contains a failed login attempt (status code 401)
            if re.search(failed_login_pattern, line):
                print(f"Failed login detected: {line.strip()}")  # Debug: Print the line for reference
                
                # Split the line into parts (words separated by spaces)
                parts = line.split(' ')
                
                # Extract the IP address (it's the first part of the line)
                ip_address = parts[0]
                
                # Add 1 to the failed login count for this IP address
                failed_logins[ip_address] += 1

    # Check if any IP addresses exceed the threshold of failed login attempts
    suspicious_activity = {ip: count for ip, count in failed_logins.items() if count > threshold}

    # Print the results
    if suspicious_activity:
        print("Suspicious Activity Detected:")
        print(f"{'IP Address':<20} {'Failed Login Attempts'}")
        print("-" * 40)
        for ip, count in suspicious_activity.items():
            print(f"{ip:<20} {count}")
    else:
        print("No suspicious activity detected.")

# How to use the function:
log_file_path = 'logfile.log'  # Path to the log file (replace with your actual file path)
detect_suspicious_activity(log_file_path, threshold=3)  # Set the threshold for testing (e.g., 3 attempts)
