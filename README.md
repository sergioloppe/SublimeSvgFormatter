# SVG Formatter for Sublime Text

A simple Sublime Text plugin to format SVG files.


Note: This plugin relies solely on Python's standard library, available in Sublime Text's embedded Python environment, ensuring no additional Python packages are necessary for its operation.


## Installation

This plugin is available through Package Control:

1. Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on macOS).
2. Type "Package Control: Install Package" and hit Enter.
3. Search for "SVG Formatter" and hit Enter to install.

### Manual Installation

1. Open Sublime Text.
2. Navigate to `Preferences > Browse Packages...` to open the Sublime Text Packages directory.
3. Clone the SVG Formatter repository into this directory:

   ```bash
   git clone https://github.com/sergioloppe/svg-formatter.git SublimeSvgFormatter


## Usage

### Prettify SVG
To format an SVG file for better readability:

1. Open the SVG file you wish to format in Sublime Text.
2. Access the Command Palette by pressing Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (macOS).
3. Type SVG Formatter: Prettify and press Enter.

The plugin will reformat your SVG, applying consistent indentation and spacing for improved readability.

### Minify SVG
To compress an SVG file by removing unnecessary whitespace and comments:

1. With the SVG file open in Sublime Text, open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P).
2. Type SVG Formatter: Minify and press Enter.

Your SVG will be compressed, stripping out all non-essential spaces and comments to minimize file size.

## No Additional Python Requirements
This plugin operates within Sublime Text's embedded Python environment and does not require any external Python packages. It uses Python's built-in xml.etree.ElementTree and xml.dom.minidom modules, ensuring compatibility and ease of use across all platforms supported by Sublime Text.

## Contributing

Contributions are welcome! Please submit pull requests or report issues on GitHub.

## License

SVG Formatter is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file in the repository.
