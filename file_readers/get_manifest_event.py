from xml.etree.ElementTree import ElementTree, tostring

namespaces = {"me": "http://www.hermes.co.uk/v2.0.0/manifestEvents",
               "common": "http://www.hermes.co.uk/v2.0.0/common",
               "xsi":"http://www.w3.org/2001/XMLSchema-instance"}


class ManifestEvents:
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.children = []

    def get_xml_nodes_with_route_ids(self, route_ids):
        tree = ElementTree(file=self.xml_file)
        root = tree.getroot()

        for child in root:
            routeid = self.get_route_id_node(child)
            if int(routeid.text) in route_ids:
                self.children += child

        if self.children is None:
            raise Exception("No element found with route id " + str(route_ids))

    def get_xml_nodes_without_route_ids(self, route_ids):
        tree = ElementTree(file=self.xml_file)
        root = tree.getroot()

        for child in root:
            routeid = self.get_route_id_node(child)
            if int(routeid.text) not in route_ids:
                self.children += child

    def get_route_id_node(self, manifest_node):
        header = manifest_node.find("me:manifestHeader", namespaces)
        routes = header.find("me:route", namespaces)
        return routes.find("common:routeId", namespaces)

    def get_required_manifest_events_as_string(self):
        return_string = ""
        for child in self.children:
            node_text = str(tostring(child), 'utf-8')
            node_text = node_text.replace("ns0", "me")\
                .replace("ns1", "common")\
                .replace(' xmlns:me="http://www.hermes.co.uk/v2.0.0/manifestEvents" xmlns:common="http://www.hermes.co.uk/v2.0.0/common','')\
                .replace("\"", '')
            return_string += node_text
        return return_string

