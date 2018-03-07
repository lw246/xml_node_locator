from file_readers.get_manifest_event import ManifestEvents

header_tags = """<?xml version="1.0" encoding="UTF-8" ?>
<me:manifestEvents 
    xmlns:me="http://www.hermes.co.uk/v2.0.0/manifestEvents" 
    xmlns:common="http://www.hermes.co.uk/v2.0.0/common" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
"""

closing_tags = "</me:manifestEvents>"


class CreateManifestEventsXml:

    def __init__(self, base_file):
        self.required_output = ""
        self.unrequired_output = ""
        self.me = ManifestEvents(base_file)
        self.me2 = ManifestEvents(base_file)

    def create_manifest_events(self, route_ids):
        self.me.get_xml_nodes_with_route_ids(route_ids)
        self.required_output += self.me.get_required_manifest_events_as_string()

        self.me2.get_xml_nodes_without_route_ids(route_ids)
        self.unrequired_output += self.me2.get_required_manifest_events_as_string()

    def create_opening_tags(self):
        self.required_output += header_tags
        self.unrequired_output += header_tags

    def create_closing_tags(self):
        self.required_output += closing_tags
        self.unrequired_output += closing_tags

    def create_required_file(self, output_path):
        with open(output_path, "w") as file:
            file.write(self.required_output)

    def create_unrequired_file(self, output_path):
        with open(output_path, "w") as file:
            file.write(self.unrequired_output)