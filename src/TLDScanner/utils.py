# Global import
import os

from datetime import datetime

# Convert datetime objects to strings
def convert_dates(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    raise TypeError("Type not serializable")

# Returns a list of unique tld extensions
def remove_duplicates(data):
    """Removes duplicates from a list."""
    return set(data)

def format_data(selected_info, format):
    if format == "json":
        # Return selected_info as JSON format
        return json.dumps(selected_info, default=convert_dates, indent=4)
    else:
        # Return selected_info as TEXT format
        return "\n".join(f"{key}: {value}" for key, value in selected_info.items())

def write_log(log_file, log_data):
    file_exists = os.path.exists(log_file)
    with open(log_file, 'w' if not file_exists else 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {log_data}\n")

def format_expiration_date(data):
    expiration_date = data.get('expiration_date')
    if expiration_date:
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        if isinstance(expiration_date, datetime):
            expiration_date = expiration_date.strftime('%Y-%m-%d %H:%M:%S')
    else:
        expiration_date = 'N/A'
    return expiration_date

def format_status(data):
    status = data.get('status')
    if not status:
        status = ['N/A']
    return status
