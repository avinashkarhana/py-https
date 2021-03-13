import http.server, ssl, os, sys, codecs

def getcurrentPath():
    return os.path.abspath(os.getcwd())+'/'

# generate self signed certificate using openssl command
def generate_selfsigned_cert():
    # absolute path of pyServer.py
    currentPath=getcurrentPath()
    try:
        cmd = 'openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -nodes -out '+currentPath+'cert.pem -keyout '+currentPath+'key.pem -subj "/C=IN/ST=x/L=x/O=x/OU=x Department/CN=x"'
        os.system(cmd)
        print('####Certificate Generated####')
    except:
        print('Error while generating certificate')

# starts server on provided host and port
def startServer(host,port,cert,key):
    currentPath=getcurrentPath()
    if cert=="":
        cert=currentPath+"cert.pem"
    if key=="":
        key=currentPath+"key.pem"
    if not os.path.exists(cert):
        print("##################################\nUnable to Start Server!\nCert File Not Found\nSpecify cert file with -c option, or use --help for help")
        exit()
    if not os.path.exists(key):
        print("##################################\nUnable to Start Server!\nKey File Not Found\nSpecify key file with -k option, or use --help for help")
        exit()


    server_address = (host, port)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket (httpd.socket, certfile = cert,keyfile = key, server_side=True)
    print("Server started at https://" + server_address[0]+":"+str(server_address[1]))
    httpd.serve_forever()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def getVersion():
    for line in read("./__init__.py").splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
        raise RuntimeError("Unable to find version string.")

def initstart():
    usage="""
        USAGE:
            pysrvhttps.py [-option value] [port]
        OPTIONS:
            --v             Version Info
            --help          Help and usage Info
            -p              Port Number [Port 443,80 requires sudo]
            -h              Host address
            -c              ssl cert file location
            -k              ssl key file location
            -gencert        Auto Generate SSL Cert and Key [openssl must be installed and included in PATH]
    """
    
    try:
        h='0.0.0.0'
        p=4443
        c=""
        k=""
        if "--help" in sys.argv:
            print(usage)
            exit()
        if "--v" in sys.argv:
            print("pyhttps version: ",getVersion())
            exit()
        if len(sys.argv)>1:
            if "-gencert" in sys.argv:
                generate_selfsigned_cert()
            if "-p" in sys.argv:
                try:
                    p=int(sys.argv[sys.argv.index('-p')+1])
                except:
                    print("Invalid port!\n",usage)
                    exit()
            if "-h" in sys.argv:
                try:
                    h=sys.argv[sys.argv.index('-h')+1]
                except:
                    print("Invalid host!\n",usage)
                    exit()
            if "-c" in sys.argv:
                try:
                    c=sys.argv[sys.argv.index('-c')+1]
                except:
                    print("Invalid cert!\n",usage)
                    exit()
            if "-k" in sys.argv:
                try:
                    k=sys.argv[sys.argv.index('-k')+1]
                except:
                    print("Invalid key!\n",usage)
                    exit()
            if len(sys.argv)==2 and sys.argv[1]!="-gencert":
                try:
                    p=int(sys.argv[1])
                except:
                    print("Invalid option or port number!\n",usage)
                    exit()
            try:
                p=int(sys.argv[-1])
            except:
                pass
        # you can change the host and port
        startServer(h,p,c,k)
    except KeyboardInterrupt:
        print("\nServer Stopped!")

# entry point of script
if __name__ == '__main__':
    initstart()

'''
Command reference for self signed certificate generation: 
1) openssl req -newkey rsa:4096 \
            -x509 \
            -sha256 \
            -days 3650 \
            -nodes \
            -out cert.pem \
            -keyout key.pem \
            -subj "/C=IN/ST=x/L=x/O=x/OU=x Department/CN=x"
            
2) openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -nodes -out cert.pem -keyout key.pem -subj "/C=IN/ST=x/L=x/O=x/OU=x Department/CN=x"
'''