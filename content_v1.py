import argparse
from argparse import RawTextHelpFormatter

xor_key = [0x61, 0x23, 0x21, 0x73, 0x43, 0x30, 0x2c, 0x2e]

description = ('Decrypt or encrypt content_v1 of Fall Guys: Ultimate Knockout\n'
'content_v1 is usually found inside %UserProfile%\AppData\LocalLow\Mediatonic\FallGuys_client')

argument_parser = argparse.ArgumentParser(description=description, formatter_class=RawTextHelpFormatter)

argument_parser.add_argument('input_file', help='content_v1 or a valid JSON file')
argument_parser.add_argument('output_file')

arguments = argument_parser.parse_args()

content = bytearray()
content_idx = 0

try:
  with open(arguments.input_file, 'rb') as input_file:
    while (byte := input_file.read(1)):
      content += bytes([ord(byte) ^ xor_key[content_idx % (len(xor_key))]])
      content_idx += 1
except (IOError, OSError) as exception:
  print('Error: could not read input file')
  exit()

try:
  with open(arguments.output_file, 'wb') as output_file:
    output_file.write(content)
except (IOError, OSError) as exception:
  print('Error: could not create output file')
  exit()
