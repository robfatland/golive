# utility functions

import os
import requests
import shutil

from PIL import Image

def dirnou(obj):
    # dir() listing without attributes that start with the underscore
    return [x for x in dir(obj) if not x.startswith('_')]  

def lsal(path=''): 
    return os.popen('ls -al ' + path).readlines()

def SetDataDirectory(dd):
    from pathlib import Path
    return str(Path.home()) + '/data/' + dd + '/'

def ShowGitHubImage(username, repo, folder, source, localpath, localname, width, height):
    global home_d
    outf = os.path.join(localpath, localname)
    f = 'https://raw.githubusercontent.com/' + username + '/' + repo + '/master/' + folder + '/' + source
    a = requests.get(f, stream = True)
    if a.status_code == 200:
        with open(outf, 'wb') as f:
            a.raw.decode_content = True
            shutil.copyfileobj(a.raw, f)
    return Image.open(outf).resize((width,height),Image.ANTIALIAS)

def ShowLocalImage(path, filename, width, height):
    f = path + '/' + filename 
    return Image.open(f).resize((width,height),Image.ANTIALIAS)

def GetGoliveMeridian(ds):       # This method is hard-coded to work for golive NetCDF files
    pstring = ds.input_image_details.attrs['image1_proj_WKT']
    locale = pstring.find('central_meridian')
    return int(pstring[locale+18:locale+22])

# Test either of the 'Show Image' functions
# ShowGitHubImage('robfatland', 'othermathclub', 'images/cellular', 'conus_textile_shell_2.png', home_d, 'ctextile.jpg', 450, 250)
# ShowLocalImage(home_d, 'ctextile.jpg', 450, 250)