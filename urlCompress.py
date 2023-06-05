# NOTES 
# 1. To generate a shortened URL, you can import from python library:
#   - pyshorteners
#   - shortuuid *** (universally unique identifier)


from typing import Dict, Optional
from url_shortener_app.models import URLMapping
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

        # create a new URLMapping object with the generatedshort code and long URL
        url_mapping = URLMapping(short_code=short_code, long_url=long_url)

        # save the URLMapping object to the database 
        url_mapping.save()


        # Return the generated short code
        return short_code
    
    def remove_mapping(self, short_code: str) -> None:
        # find the URLMapping object with the given short code and delete it from the database
        URLMapping.objects.filter(short_code=short_code).delete()

    def get_long_url(self, short_code: str) -> Optional[str]:
        try:
            # Try to retrieve the URLMapping object with the given shortcode from the database
            url_mapping = URLMapping.objects.get(short_code=short_code)
        
        # Retrieve long URL associated w the URLMapping object
            return url_mapping.long_url
        
        except URLMapping.DoesNotExist:
        # if the URLMapping object doesn't exist, return None
            return None

    

