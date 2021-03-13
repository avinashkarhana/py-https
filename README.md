# py-https

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

    --v         Version Info
    --help      Help and usage Info
    -p          Port Number [Port 443,80 requires sudo]
    -h          Host address
    -c          ssl cert file location
    -k          ssl key file location
    -gencert    Auto Generate SSL Cert and Key* 
            
    *[openssl must be installed and included in PATH for -gencert]
