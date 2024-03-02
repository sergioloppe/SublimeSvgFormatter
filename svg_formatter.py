import sublime
import sublime_plugin
import xml.etree.ElementTree as ET
from xml.dom import minidom
import re


class BaseSvgFormatterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        all_content_region = sublime.Region(0, self.view.size())
        svg_content = self.view.substr(all_content_region)
        
        try:
            processed_svg = self.process_svg(svg_content)
            self.view.replace(edit, all_content_region, processed_svg)
        except Exception as e:
            sublime.error_message(f"Error processing SVG: " + str(e))
    
    def process_svg(self, svg_content):
        raise NotImplementedError


class SvgFormatterPrettifyCommand(BaseSvgFormatterCommand):
    def process_svg(self, svg_content):
        root = ET.fromstring(svg_content)
        rough_string = ET.tostring(root, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        
        pretty_svg = reparsed.toprettyxml(indent="    ")
        pretty_svg = pretty_svg.replace('ns0:', '').replace(':ns0', '')
        return '\n'.join([line for line in pretty_svg.split('\n') if line.strip()])


class SvgFormatterMinifyCommand(BaseSvgFormatterCommand):
    def process_svg(self, svg_content):
        minified_svg = re.sub(r'<!--.*?-->', '', svg_content, flags=re.DOTALL)
        minified_svg = re.sub(r'>\s+<', '><', minified_svg)
        minified_svg = re.sub(r'\s+', ' ', minified_svg)
        return minified_svg


