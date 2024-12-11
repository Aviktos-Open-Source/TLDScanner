# Global imports
import whois
import json
import os

# Local imports
from .utils          import convert_dates, format_data, write_log, format_expiration_date, format_status
from .dataParser     import process_data

log_folder = 'log'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Returns number of times the domain appeared to be registered
def tldscan(domain_name, data_path, format='json'):
    """Get selected information about the provided domain"""
    if format not in ['json', 'text']:
        raise ValueError(f"Unsupported format: {format}")
    tlds_list = process_data(data_path)
    log_file = os.path.join(log_folder, domain_name)
    count = 0
    for tld in tlds_list:
        try:
            # Retrieve the domain information using the whois module
            domain_info = whois.whois(f"{domain_name}{tld}")
            
            if domain_info.get('domain_name'):
                count += 1
                
                # Select necessary information to log
                selected_info = {
                    "count": count,
                    "domain_name": domain_info.get("domain_name"),
                    "expiration_date": format_expiration_date(domain_info),
                    "status": format_status(domain_info)
                }
                write_log(log_file, selected_info)
            else:
                print(f"The domain \"{domain_name}{tld}\" doesn't appear to be registered")
        except Exception as e:
            print(f"Error querying \"{domain_name}{tld}\": {str(e)}")
    
    return count
