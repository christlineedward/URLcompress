# NOTES 
# 1. To generate a shortened URL, you can import from python library:
#   - pyshorteners
#   - shortuuid

import pyshorteners

def shortenUrl(longUrl):
    '''takes a long URL as a parameter and returns a shortened URL'''
   
    s = pyshorteners.Shortener()

    return s.tinyurl.short(longUrl)
    
    
