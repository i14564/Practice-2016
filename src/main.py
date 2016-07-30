from main_check import main_check
import argparse



parser = argparse.ArgumentParser(description='Check website for fake')
parser.add_argument('url', help='site url without protocol')

url = args = parser.parse_args().url

main_check(url)
