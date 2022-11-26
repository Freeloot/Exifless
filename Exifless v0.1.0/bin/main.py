# Local imports
from utils import Utils

'''Change Console Title (windows only)'''
Utils().set_title()

'''Get Image File'''
input_file = input("Image directory -> ")

'''Remove EXIF'''
print('[+] Clearing exif...')
Utils().remove_exif(input_file)
print('[+] Exifless Complete!')