from xml.etree.ElementTree import ElementTree, dump


class NodeLocator(object):

    def __init__(self, xml):
        self._xml = xml

    def locate_node(self, node_name):
        self.return_node = node_name


    def with_namespaces(self, namespaces):
        self.namespaces = namespaces
        return self

    def under_child(self, node_name):
        self._xml = self._xml.find