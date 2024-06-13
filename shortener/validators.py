from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()
    
    if "http" not in value:
        raise ValidationError("Please insert 'http' before you proceed")
    elif "www" not in value:
        raise ValidationError("Please insert 'www' before you proceed")
    elif  "com" not in value:
        raise ValidationError("Please insert '.com' before you proceed")
    
    try:
        url_validator(value)
    except ValidationError:
        raise ValidationError("Invalid URL for this field")
    

    return value

#def validate_dot_com(value):
 #   if "com" not in value:
  #      raise ValidationError("This is not valid because of missing '.com'")
   # 
    #return value
