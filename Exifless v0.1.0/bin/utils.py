import os
from PIL import Image

class Utils:
    def set_title(self):
        try:
            os.system('title Exifless v0.1.0')
            os.system('cls')
        except:
            pass

    def remove_exif(self, file):
        im = Image.open(file)
        if 'exif' in im.info: del im.info['exif']
        file_format_old = os.path.splitext(file)[1].upper()
        file_format = file_format_old.translate({ord('.'):None})
        print(f'[+] Detected file format as {file_format}\n')
        im.save('\output', str(file_format), quality='keep')