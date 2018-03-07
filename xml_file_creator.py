from file_readers.create_manifest_events_xml import CreateManifestEventsXml
from file_readers.get_detail_line import DetailLines

route_ids = [9347, 8308]

xml_source_file = "source xml file.dat"
filtered_xml_file = "filtered out file.dat"
original_with_removed_xml_file = "original xml with removed nodes.dat"

piped_source_file = "piped source file.dat"
filterd_piped_file = "filtered piped file.dat"
original_with_removed_piped_file = "original piped file with removed lines.dat"



#Xml file
eventManifestWriter = CreateManifestEventsXml(xml_source_file)

eventManifestWriter.create_opening_tags()
eventManifestWriter.create_manifest_events(route_ids)
eventManifestWriter.create_closing_tags()
eventManifestWriter.create_required_file(filtered_xml_file)
eventManifestWriter.create_unrequired_file(original_with_removed_xml_file)

# Piped file
details = DetailLines(piped_source_file)

details.create_opening_tags()
details.get_detail_line_for(route_ids)
details.create_closing_tags()
details.create_required_file(filterd_piped_file)
details.create_unrequired_file(original_with_removed_piped_file)

