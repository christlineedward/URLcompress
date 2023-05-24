# NOTES 
# 1. To generate a shortened URL, you can import from python library:
#   - pyshorteners
#   - shortuuid *** (universally unique identifier)
from typing import Dict, Optional
import shortuuid 

class URLShortener:
    # initialize 'url_map' attr to an empty dict
    def __init__(self):
        '''self = is just conventional naming for 1st parameter, url_map = attribute/instance variable that will store the mappings between short codes and long URLs '''
        # initializing to empty dict - ensures each instance of the 'URLShortener' class 
        # will have its own independent 'url_map' to store the mappings
        self.url_map = Dict[str, str] = {}
        print(self.url_map)
        
    def add_mapping(self, long_url: str) -> str:
        '''takes a long URL as a parameter and returns a shortened URL'''
        # Generate a short code using the shortuuid module
        short_code: str = shortuuid.uuid()[:8]

        # Add the mapping of short code to longURL in the url_map dict
        self.url_map[short_code] = long_url

        # Return the generated short code
        return short_code
    
    def remove_mapping(self, short_code: str) -> None:
        # Check if short code exists in the url_map dict
        if short_code in self.url_map:
            # Remoce the mapping from the url_map dict
            del self.url_map[short_code]

    def get_long_url(self, short_code: str) -> Optional[str]:
        # Retrieve long URL associated w the given short code from the url_map dict
        return self.url_map.get(short_code)
    
if __name__ == '__main__':

    # TESTS
    # create an instance of URLShortener
    shortener = URLShortener()

    # add new mappings
    shortcode1 = shortener.add_mapping("https://www.notion.so/tristanwedderburn/May-1st-Sync-Meeting-Notes-d849692fbcfd4bcbaecfc4cb734de894")
    shortcode2 = shortener.add_mapping("https://github.com/christlineedward/URLcompress")

    # print the short codes and their corresponding long URLs 
    print("Short codes and long URLs: ")
    print(f"{shortcode1}: {shortener.get_long_url(shortcode1)}")
    print(f"{shortcode2}: {shortener.get_long_url(shortcode2)}")

    # remove a mapping
    shortener.remove_mapping(shortcode1)

    # print the updated mappings
    print("\nAfter removing a mapping: ")
    print(f"{shortcode1}: {shortener.get_long_url(shortcode1)}")
    print(f"{shortcode2}: {shortener.get_long_url(shortcode2)}")

    # allow user input
    long_url = input("\nEnter a long URL to shorten: ")
    short_code = shortener.add_mapping(long_url)
    print(f"\nShortened URL: {short_code}")
    print(f"Original URL: {shortener.get_long_url(short_code)}")
    
    # this prints out the contents of the current mappings
    print("\nurl_map dictionary: ")
    print(shortener.url_map)



    # print(short_code("https://fandm.instructure.com/?login_success=1"))
   