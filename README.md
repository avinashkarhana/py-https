[![Build and Publish to PyPI](https://github.com/avinashkarhana/py-https/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/avinashkarhana/py-https/actions/workflows/publish-to-pypi.yml)
# py-https
<p align="center"><img src="https://repository-images.githubusercontent.com/347398533/7a4af700-931d-11eb-956c-db8b5473f5fa" height="50%" width="50%" /></p>

> A simple python https server

## INSTALLATION:
    pip install py-https

## USAGE:
>> As a module from any location
>>
>>      python3 -m pyhttps [-option value] [port]

>> In script
>>
>>      from pyhttps import startserver
>>
>>      startServer(host,port,cert,key)
>>      ##cert : certificate file location
>>      ##key  : key file location
    

## OPTIONS:

    --v             Version Info(**)
    --help          Help and usage Info(**)
    -p              Port Number [Port 443,80 may require sudo or elivated permissions]
    -h              Host address
    -c              ssl cert file location
    -k              ssl key file location
    -gencert        Auto Generate SSL Cert and Key(#)
    (-gencert [Value]: Target Path for generating certificates)
    
    ** [No value needed for these type of options]
    #  [Optional value for this type of option]
    
    >>> openssl must be installed and included in PATH for -gencert otpion to work

### Wanna help me to work more on Open-Source Projects like this?
<a href="https://www.buymeacoffee.com/avinashkarhana" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a> so that I can get one more sleepless night to work on this kind of stuff.

Or use other sponsoring methods if you like.
