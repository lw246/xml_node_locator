

class DetailLines:
    def __init__(self, file_path):
        self.file_path = file_path
        self.output = ""
        self.modified = ""

    def get_detail_line_for(self, route_ids):
        for route_id in route_ids:
            locator = self.get_locator(route_id)
            with open(self.file_path, 'r') as file:
                for line in file.readlines():
                    if locator in line:
                        self.output += line
                    else:
                        self.modified += line

    def get_locator(self, route_id):
        depot_number = str(route_id)[0:2]
        van_number = str(route_id)[2:4]
        location_string = depot_number + "|VAN|" + van_number
        return location_string

    def create_opening_tags(self):
        self.output += "<file>\n"

    def create_closing_tags(self):
        self.output += "\n</file>"

    def create_required_file(self, file_path):
        with open(file_path, "w") as file:
            file.write(self.output)

    def create_unrequired_file(self, file_path):
        with open(file_path, "w") as file:
            file.write(self.modified)
