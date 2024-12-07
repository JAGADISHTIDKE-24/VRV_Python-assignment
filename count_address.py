from collections import Counter  # This helps us count how many times each item appears

# Function to count how many requests each IP address made
def count_requests_per_ip(log_file_path):
    ip_counter = Counter()  # This will store how many times each IP address appears
    
    # Open the log file and read it line by line
    with open(log_file_path, 'r') as file:  # Open the file to read
        for line in file:  # Loop through each line in the file
            parts = line.split(' ')  # Split the line into words, spaces separate them
            ip_address = parts[0]  # The first word is always the IP address
            
            # Count how many times this IP has appeared
            ip_counter[ip_address] += 1
    
    # Now we want to see the IPs sorted by the number of requests, from highest to lowest
    sorted_ips = ip_counter.most_common()  # Get the IPs sorted by the count

    # Print the result in a simple, readable format
    print(f"{'IP Address':<15} {'Request Count'}")  # Print the headers (IP and count)
    print("-" * 30)  # Just a line to separate headers from data
    
    # For each IP in the sorted list, print the IP and how many requests it made
    for ip, count in sorted_ips:
        print(f"{ip:<15} {count}")  # Print each IP and its count

# Path to the log file
log_file_path = 'logfile.log'  # Make sure this points to your log file

# Call the function to count and display IP addresses with their request counts
count_requests_per_ip(log_file_path)
