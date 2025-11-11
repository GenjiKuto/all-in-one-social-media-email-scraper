thonimport json

def export_data(data):
    # Save the extracted data to a file
    with open("extracted_emails.json", "w") as f:
        json.dump(data, f, indent=4)