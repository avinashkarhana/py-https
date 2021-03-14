import http.server, ssl, os, sys, codecs

def getcurrentPath():
    return os.path.abspath(os.getcwd())+'/'


def generate_selfsigned_cert(certpath=""):

    if certpath=="":
        currentPath=getcurrentPath()
    else:
        currentPath=certpath
    
    try:
        cmd = 'openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -nodes -out '+currentPath+'cert.pem -keyout '+currentPath+'key.pem -subj "/C=IN/ST=x/L=x/O=x/OU=x Department/CN=x" >/dev/null 2>&1'
        os.system(cmd)
        cert=currentPath+"cert.pem"
        key=currentPath+"key.pem"
        if not os.path.exists(cert):
            raise ValueError('Unable to create cert.pem')
        if not os.path.exists(key):
            raise ValueError("Unable to create cert.pem")
        print('####Certificate Generated####')
    except ValueError as err:
        print(err.args[0],"\nPossible causes may include low privilage and no write access in current directory")
        exit()
    except:
        print('Error while generating certificate')
        exit()


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
    try:
        httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    except PermissionError:
        print("##################################\nUnable to Start Server!\nPermission Error\nTry with elevated privilages with sudo or 'Run as Administrator'")
        exit()
    try:
        httpd.socket = ssl.wrap_socket (httpd.socket, certfile = cert,keyfile = key, server_side=True)
    except ssl.SSLError as e:
        print("##################################\nUnable to Start Server!\nSSL Error: ",e,"\nProbable causes may include mismatch of cert and key file (using wrong key file for certain cert file or vice-versa)")
        exit()
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

def getUsage():
    st=False
    usage=""
    for line in read("./__init__.py").splitlines():
        if st and not line.startswith('"""'):
           usage+=line+"\n"
        if line.startswith('__usage__'):
            st=True
        if st and line.startswith('"""'):
            break
    if not st:
        raise RuntimeError("Unable to find usage string.")
    else:
        return usage


def initstart():
    usage=getUsage()
    
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
                tmpi=sys.argv.index('-gencert')
                if (len(sys.argv)-1)!=tmpi:
                    if sys.argv[tmpi+1] not in ['-p','-k','-c','-h','--v','--help']:
                        certspath=sys.argv[tmpi+1]
                        if certspath[-1]!="/":certspath+="/"
                        generate_selfsigned_cert(certpath=certspath)
                        c=certspath+"cert.pem"
                        k=certspath+"key.pem"
                    else:
                        generate_selfsigned_cert()
                else:       
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

        startServer(h,p,c,k)
    except KeyboardInterrupt:
        print("\nServer Stopped!")


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