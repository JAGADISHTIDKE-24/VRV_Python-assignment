import re  # Import "re" for working with regular expressions
from collections import Counter  # Import "Counter" to count occurrences of items

# Function to find the most frequently accessed endpoint
def most_frequented_endpoint(log_file_path):
    endpoints = []  # List to store all the endpoints (URLs) from the log file
    
    # Open the log file and read it line by line
    with open(log_file_path, 'r') as file:
        for line in file:  # Loop through each line in the file
            # Use a regular expression to find the endpoint (part of the URL)
            match = re.search(r'"(?:GET|POST|PUT|DELETE)\s+([^\s]+)', line)
            if match:
                endpoint = match.group(1)  # Extract the endpoint (URL path) from the match
                endpoints.append(endpoint)  # Add the endpoint to the list

    # Count how many times each endpoint appears in the list
    endpoint_count = Counter(endpoints)

    # Find the endpoint with the highest count
    most_common_endpoint, count = endpoint_count.most_common(1)[0]

    # Print the most frequently accessed endpoint
    print("Most Frequently Accessed Endpoint:")
    print(f"{most_common_endpoint} (Accessed {count} times)")

# Example usage:
log_file_path = 'logfile.log'  # Path to your log file
most_frequented_endpoint(log_file_path)  # Call the function
