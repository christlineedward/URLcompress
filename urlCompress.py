# NOTES 
# 1. To generate a shortened URL, you can import from python library:
#   - pyshorteners
#   - shortuuid

import shortuuid

class URLShortener:
    # initialize 'url_map' attr to an empty dict
    def __int__(self):
        '''self = is just conventional naming for 1st parameter, url_map = attribute/instance variable that will store the mappings between short codes and long URLs '''
        # initializing to empty dict - ensures each instance of the 'URLShortener' class 
        # will have its own independent 'url_map' to store the mappings
        self.url_map = {}
        
    def add_url_mapping(self, long_url):
        '''takes a long URL as a parameter and returns a shortened URL'''
    #  create an instance of the Shortener class from the pyshorteners module
    s = pyshorteners.Shortener()

    # # use the tinyurl service to shorten the long URL and return the result
    return s.tinyurl.short(longUrl)
    
        # Return the generated short code
        return short_code
    
    def remove_mapping(self, short_code):
        # Check if short code exists in the url_map dict
        if short_code in self.url_map:
            # Remoce the mapping from the url_map dict
            del self.url_map[short_code]
    
if __name__ == '__main__':
    print(shortenUrl("https://fandm.instructure.com/?login_success=1"))
   