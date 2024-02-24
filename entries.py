import time

def write_entries(filename):
    while True:
        # Get current date and time
        current_datetime = time.strftime("%Y-%m-%d %H:%M:%S")

        # Write current date and time to the file
        with open(filename, 'a') as file:
            file.write("Event registered successfuly at: " + current_datetime + '\n')

        # Wait for 2 seconds
        time.sleep(2)

# File path
filename = 'entries.txt'

# Write current date and time every 2 seconds
write_entries(filename)
