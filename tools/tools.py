# imports section


# functions
def get_site(url=''):
    "returns a response object from the given url parameter or None if not found/error"
    return None

def get_domain_name(url=''):
    "returns a string containing the domain name of the given url"
    return None

def get_links(url=''):
    "returns a list of unqiue url links from the given page"
    return []

def get_internal_links(url=''):
    "returns a list with unqiue url links from the given page within its domain"
    return []

def get_external_links(url=''):
    "returns a list with unqiue url links from the given page outside its domain"
    return []

def get_images(url=''):
    "returns a list of unique image urls from the given page"
    return []

def get_emails(url=''):
    "returns a list of unique email address present at the given url"
    return []

def get_videos(url=''):
    "returns a list of unique video urls from the given page"
    return []

def domain_bfs_crawl(homeurl=''):
    """
    using breath first search, crawls the given url as the home url
    returns a list with unqiue url links within the domain of the url
    """
    return []

def limited_domain_bfs_crawl(homeurl='', limit=5000):
    """
    using breath first search, crawls the given url as the home url \n
    crawling is limited by a limit which will not be exceeded if more links are present\n 
    returns a list with unqiue url links within the domain of the url
    """
    return []

def domain_dfs_crawl(homeurl=''):
    """
    using depth first search, crawls the given url as the home url
    returns a list with unqiue url links within the domain of the url
    """
    return []

def limited_domain_dfs_crawl(homeurl='', limit=5000):
    """
    using depth first search, crawls the given url as the home url \n
    crawling is limited by a limit which will not be exceeded if more links are present\n 
    returns a list with unqiue url links within the domain of the url
    """
    return []

def email_extractor(url='', limit=20):
    """
    crawls the given url plus its links limited by the limit depth \n
    returns a list with unqiue email address present within the domain of the url
    """
    return []

def phone_extractor(url='', limit=20):
    """
    crawls the given url plus its links limited by the limit depth \n
    returns a list with unqiue phone numbers present within the domain of the url
    """
    return []

def socials_extractor(url='', limit=20):
    """
    crawls the given url plus its links limited by the limit depth \n
    returns a list with unqiue social media urls present within the domain of the url
    """
    return []
