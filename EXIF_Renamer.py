import os.path, time
import datetime
import pytz
from win32com.propsys import propsys, pscon
# VARS
GPS_NO_OPLOCK = 0x00000080 

folder = "C:\\foo\\"

a = 0

ext = input('ext:  ')
# LOGIC
for path, dirs, filenames in os.walk(folder):
    for filename in filenames:
        if (ext in filename.lower()):  # include '.' toavoid 'mp4' in filename
            fullpath = os.path.join(path, filename)
            print(f'filename {filename}  fullpath {fullpath}')
            properties = propsys.SHGetPropertyStoreFromParsingName(fullpath, None, GPS_NO_OPLOCK, propsys.IID_IPropertyStore)
            dt = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
            print(dt)
            dt_creation = dt.date()
            days = dt_creation
            print(days)
            a += 1
            print(a)
            new_name = "".join([str(days), '-' + str(a) + ext])
            os.rename(os.path.join(path, filename), os.path.join(path, new_name))



















































# import os
# import pathlib

# from collections import Counter
# from PIL import Image
# from PIL.ExifTags import TAGS
# # import datetime
# from win32com.propsys import propsys, pscon
# import time
# from datetime import datetime


# # for p in pathlib.Path.cwd().iterdir():
# #     ext = p.suffix
# #     tl = ext.lower()
    
# #     if p.suffix == '.m4v':
# #         vid = p.stem + p.suffix
# #         # properties = propsys.SHGetPropertyStoreFromParsingName(str(p))
# #         # dt = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
# #         # t = datetime.strftime(dt, '%Y%m%d')
# #         # mov_name = p.stem
# #         # print(dt)

# #         os.rename(vid , 'okay' + p.suffix)
# for p in pathlib.Path.cwd().iterdir():
#     print(p)
#     with open(p) as f:
#         if(p.suffix == '.m4v'):
#             properties = propsys.SHGetPropertyStoreFromParsingName(str(p))
#             dt = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
#             t = datetime.strftime(dt, '%Y%m%d')
#             new_file = p.with_stem(t)
#             print(new_file)
                  
#             p.rename(new_file)
#     f.close()  
            
# # new_file = vid.with_stem("okay")
# # # with_stem was introduced with Python 3.9.
# # print(new_file)
 
