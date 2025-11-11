thonimport json

class Exporter:
    def export_to_file(self, data, file_name):
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)