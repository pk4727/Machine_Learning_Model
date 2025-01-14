import csv

# Default Threshold for suspicious activity (Given in description)
FAILED_LOGIN_THRESHOLD = 10

# Reads the log file and returns the lines.
def parse_log_file(file_path): 
    with open(file_path, 'r') as file:  # Open the file in read mode.
        return file.readlines()         # Read all lines from the file and return them as a list.

# Counts requests for each IP address.
def count_requests_per_ip(logs):
    ip_counts = {}                      # Dictionary to store IP addresses and their request counts.
    for log in logs:                    # Iterate through each log entry.
        ip = log.split(' ')[0]          # The IP address is the first part of the log.
        if ip in ip_counts:
            ip_counts[ip] += 1          # Increment the count if the IP address already exists in the dictionary.
        else:
            ip_counts[ip] = 1           # Add the IP address to the dictionary with an initial count of 1.
    return ip_counts

# Finds the most frequently accessed endpoint.
def most_frequently_accessed_endpoint(logs):
    endpoint_counts = {}                        # Dictionary to store endpoints and their access counts.
    for log in logs:
        parts = log.split('"')                  # Split the log entry to isolate the request section.
        if len(parts) > 1:                      # Check if the request section exists.
            request = parts[1].split(' ')       # Split the request section to extract the endpoint.
            if len(request) > 1:                # Check if the endpoint is present in the request.
                endpoint = request[1]           # Extract the endpoint.
                if endpoint in endpoint_counts:
                    endpoint_counts[endpoint] += 1                      # Increment the count if the endpoint already exists in the dictionary.
                else:
                    endpoint_counts[endpoint] = 1                       # Add the endpoint to the dictionary with an initial count of 1.

    most_accessed = max(endpoint_counts, key=endpoint_counts.get, default=None) # Find the endpoint with the highest access count.
    return most_accessed, endpoint_counts[most_accessed]                # Return the most accessed endpoint and its count.

# Finds IPs with many failed login attempts.
def detect_suspicious_activity(logs):
    failed_attempts = {}                            # Dictionary to store the count of failed login attempts for each IP address.
    for log in logs:  
        if ' 401 ' or "Invalid credentials" in log: # Check if the log contains a "401" or "Invalid credentials" HTTP status code indicating a failed login.
            ip = log.split(' ')[0]                  # Extract the IP address (the first part of the log entry).
            if ip in failed_attempts:
                failed_attempts[ip] += 1            # Increment the count if the IP already exists in the dictionary.
            else:
                failed_attempts[ip] = 1             # Add the IP address to the dictionary with an initial count of 1.

    suspicious_IP_Addresses = {}                    # Initialize an empty dictionary to store suspicious IP addresses.
    for ip, count in failed_attempts.items():       # Iterate through the failed_attempts dictionary to check each IP and its failed login count.
        if count > FAILED_LOGIN_THRESHOLD:          # Check if the count of failed attempts exceeds the FAILED_LOGIN_THRESHOLD.
            suspicious_IP_Addresses[ip] = count     # Add the IP and its count to the suspicious_ips dictionary.
    return suspicious_IP_Addresses                  # Return the dictionary of suspicious IP addresses.

# Saves results to a CSV file.
def save_result_to_csv(ip_counts, most_accessed, suspicious_IP_Addresses):
    """     Saves the analysis results to a CSV file named 'log_analysis_results.csv'.
            Args:
                ip_counts (dict): A dictionary with IP addresses as keys and their request counts as values.
                most_accessed (tuple): A tuple containing the most accessed endpoint and its access count.
                suspicious_ips (dict): A dictionary with suspicious IP addresses as keys and their failed login attempts as values. 
    """
    with open('log_analysis_results.csv', 'w', newline='') as csvfile:  # Open the file in write mode.
        writer = csv.writer(csvfile)                                    # Create a CSV writer object.

        # Section 1: Write Requests per IP Address
        writer.writerow(['Requests per IP Address:-'])                  # Write a header for the section.
        writer.writerow(['IP Address', 'Request Count'])                # Write column headers.
        for ip, count in ip_counts.items():                             # Iterate through the IP counts dictionary.
            writer.writerow([ip, count])                                # Write each IP and its request count as a row.

        # Section 2: Write Most Accessed Endpoint
        writer.writerow([])                                             # Write an empty row for separation.
        writer.writerow(['Most Accessed Endpoint:-'])                   # Write a header for this section.
        writer.writerow(['Endpoint', 'Access Count'])                   # Write column headers for the endpoint section.
        writer.writerow([most_accessed[0], most_accessed[1]])           # Convert the most_accessed tuple to a list and write it.

        # Section 3: Write Detect Suspicious Activity
        writer.writerow([])
        writer.writerow(['Suspicious Activity:-'])                      # Write a header for the suspicious activity section.
        writer.writerow(['IP Address', 'Failed Login Count'])           # Write column headers for this section.
        for ip, count in suspicious_IP_Addresses.items():               # Iterate through the suspicious IPs dictionary.
            writer.writerow([ip, count])                                # Write each suspicious IP and its failed login count as a row.

def main():
    log_file = 'sample data.log'                                                                     # Define the log file name
    logs = parse_log_file(log_file)                                                             # Call function to read the log file and store the lines in `logs`
    
    # Analyze logs
    ip_counts = count_requests_per_ip(logs)                                                     # Call function to count requests per IP address
    sorted_ip_counts = dict(sorted(ip_counts.items(), key=lambda item: item[1], reverse=True))  # Sort the IP counts in descending order based on the request count
    most_accessed = most_frequently_accessed_endpoint(logs)                                     # Call function to get the most accessed endpoint and its count
    suspicious_IP_Addresses = detect_suspicious_activity(logs)                                  # Call function to find suspicious IP addresses based on failed logins
    save_result_to_csv(sorted_ip_counts, most_accessed, suspicious_IP_Addresses)                # save result to the file
    
    # Display results
    print("Requests per IP Address:")                                   # Print the section title
    print('IP Address          Request Count')                          # Print the header for the IP address and request count
    for ip, count in sorted_ip_counts.items():                          # Iterate over each IP and its request count
        print(f"{ip:<20}{count}")                                       # Print the IP address and its count, left-aligned with 20 characters for the IP
    
    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")    # Print the most accessed endpoint and its count
    
    print("\nSuspicious Activity Detected:")
    if suspicious_IP_Addresses:                                         # Check if any suspicious IP addresses are found
        print("IP Address          Failed Login Attempts")              # Print the header for suspicious activity
        for ip, count in suspicious_IP_Addresses.items():               # Iterate over each suspicious IP and its failed login attempts
            print(f"{ip:<20}{count}")                                   # Print the suspicious IP and the count of failed login attempts
    else:
        print("No suspicious activity detected.")                       # Print this if no suspicious activity is found

if __name__ == '__main__':
    main()                                                              # Call the main function to run the script
