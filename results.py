import re
import csv
from collections import Counter, defaultdict

# Function to count requests per IP address
def count_requests_per_ip(log_file_path):
    ip_counter = Counter()
    with open(log_file_path, 'r') as file:
        for line in file:
            ip_address = line.split(' ')[0]  # Extract the IP address (first part of the line)
            ip_counter[ip_address] += 1
    return ip_counter

# Function to find the most frequently accessed endpoint
def most_frequented_endpoint(log_file_path):
    endpoints = []
    with open(log_file_path, 'r') as file:
        for line in file:
            match = re.search(r'"(?:GET|POST|PUT|DELETE)\s+([^\s]+)', line)
            if match:
                endpoints.append(match.group(1))  # Extract the endpoint
    endpoint_counter = Counter(endpoints)
    return endpoint_counter.most_common(1)[0] if endpoint_counter else ("None", 0)

# Function to detect suspicious activity based on failed login attempts
def detect_suspicious_activity(log_file_path, threshold=10):
    failed_logins = defaultdict(int)
    with open(log_file_path, 'r') as file:
        for line in file:
            if '401' in line:  # Look for "401" status code
                ip_address = line.split(' ')[0]
                failed_logins[ip_address] += 1
    return {ip: count for ip, count in failed_logins.items() if count > threshold}

# Function to save results to a CSV file
def save_to_csv(ip_requests, most_accessed_endpoint, suspicious_ips, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write "Requests per IP" section
        writer.writerow(["Requests per IP"])
        writer.writerow(["IP Address", "Request Count"])
        for ip, count in ip_requests.items():
            writer.writerow([ip, count])
        writer.writerow([])  # Blank row for separation

        # Write "Most Accessed Endpoint" section
        writer.writerow(["Most Accessed Endpoint"])
        writer.writerow(["Endpoint", "Access Count"])
        writer.writerow(most_accessed_endpoint)
        writer.writerow([])  # Blank row for separation

        # Write "Suspicious Activity" section
        writer.writerow(["Suspicious Activity"])
        writer.writerow(["IP Address", "Failed Login Count"])
        for ip, count in suspicious_ips.items():
            writer.writerow([ip, count])

# Main function to analyze the log file
def analyze_log_file(log_file_path, output_file):
    # Count requests per IP
    ip_requests = count_requests_per_ip(log_file_path)

    # Find the most accessed endpoint
    most_accessed_endpoint = most_frequented_endpoint(log_file_path)

    # Detect suspicious activity
    suspicious_ips = detect_suspicious_activity(log_file_path, threshold=3)  # Set threshold to 3 for testing

    # Print the results to the terminal
    print("Requests per IP:")
    for ip, count in ip_requests.items():
        print(f"{ip}: {count}")
    print("\nMost Accessed Endpoint:")
    print(f"{most_accessed_endpoint[0]} (Accessed {most_accessed_endpoint[1]} times)")
    print("\nSuspicious Activity:")
    for ip, count in suspicious_ips.items():
        print(f"{ip}: {count} failed login attempts")

    # Save the results to a CSV file
    save_to_csv(ip_requests, most_accessed_endpoint, suspicious_ips, output_file)
    print(f"\nResults saved to {output_file}")

# Example usage:
log_file_path = 'logfile.log'  # Replace with your log file path
output_file = 'log_analysis_results.csv'  # Output CSV file name
analyze_log_file(log_file_path, output_file)
