import sublime
import sublime_plugin
import xml.etree.ElementTree as ET
from xml.dom import minidom


class SvgFormatterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get the entire content of the file
        all_content_region = sublime.Region(0, self.view.size())
        svg_content = self.view.substr(all_content_region)
        
        try:
            # Parse SVG content
            root = ET.fromstring(svg_content)
            rough_string = ET.tostring(root, 'utf-8')
            reparsed = minidom.parseString(rough_string)
            
            # Prettify SVG content
            pretty_svg = reparsed.toprettyxml(indent="    ")
            pretty_svg = pretty_svg.replace('ns0:', '').replace(':ns0', '')
            pretty_svg = '\n'.join([line for line in pretty_svg.split('\n') if line.strip()])
            
            # Replace the original content
            self.view.replace(edit, all_content_region, pretty_svg)
        except Exception as e:
            sublime.error_message("Error formatting SVG: " + str(e))
