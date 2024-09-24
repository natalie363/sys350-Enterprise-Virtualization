import getpass
import ssl
from pyVim.connect import SmartConnect


def auth():
    """authenticate to vcenter server"""
    passwd = getpass.getpass()
    s = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    s.verify_mode = ssl.CERT_NONE
    si = SmartConnect(host="vcenter.eckles.local", user="eckles-adm", pwd=passwd, sslContext=s)
    return si

def basic_info(auth):
    """gets basic connection info after connecting"""
    about_info = auth.content.about
    print(about_info)
    print(about_info.fullName)


auth_object = auth()
basic_info(auth_object)