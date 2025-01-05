def check_valid(url_class):
    url = url_class.url_unshortened
    if ".com" not in url:
        return False
    
    if "http://" not in url:
        url_class.url_unshortened = f"http://{url}"
    
    return True