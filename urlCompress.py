# NOTES 
# 1. To generate a shortened URL, you can import from python library:
#   - pyshorteners
#   - shortuuid

import shortuuid

def shortenUrl(longUrl):
    '''takes a long URL as a parameter and returns a shortened URL'''
    #  create an instance of the Shortener class from the pyshorteners module
    s = pyshorteners.Shortener()

    # # use the tinyurl service to shorten the long URL and return the result
    return s.tinyurl.short(longUrl)
    
    
if __name__ == '__main__':
    print(shortenUrl("https://fandm.instructure.com/?login_success=1"))
   