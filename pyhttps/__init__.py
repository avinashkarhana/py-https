__version__ = "0.0.2.1"
__usage__ = """
    USAGE:
        1.) As a module from any location
            python3 -m pyhttps [-option value] [port]
        
        2.) In script
            from pyhttps import startserver
            
            startServer(host,port,cert,key)

            ##cert : certificate file location
            ##key  : key file location

    OPTIONS:
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
        
        >>> openssl must be installed and included in PATH for -gencert]
"""