import sys
import os.path
import hashlib
import subprocess
import time

APP_DATA_DIR = './Data/'
WWDR_FILENAME = './Cert/AppleWWDRCA.pem'    
PASS_KEY_FILENAME = './Cert/private.key'  
PASS_CERT_FILENAME = './Cert/cert.pem' 

files = ('pass.json', 'logo.png', 'logo@2x.png', 'icon.png', 'icon@2x.png', 'thumbnail.png', 'thumbnail@2x.png')


file_data = {}
file_hashes = {}
manifest = '{\n'
for file in files:
    f = open(APP_DATA_DIR + file, 'r')
    data = f.read()
    f.close()
    filename = os.path.basename(file)
    file_data[filename] = data
    file_hashes[filename] = hashlib.sha1(data).hexdigest()
    manifest += '   "%s":"%s",\n' % (filename, file_hashes[filename])

manifest += '}\n'


f = open(APP_DATA_DIR + 'manifest.json', 'w')
f.write(manifest)
f.close()

cmd = 'openssl smime -sign -binary -in %smanifest.json -signer %s -inkey %s -certfile %s -md sha1 -out %ssignature -outform DER' % (APP_DATA_DIR, PASS_CERT_FILENAME, PASS_KEY_FILENAME, WWDR_FILENAME, APP_DATA_DIR)
print cmd
subprocess.call(cmd, shell=True)

CURRENT_PASS = './Pass/' + time.strftime("%Y%m%d") + '.pkpass'

cmd2 = 'zip -r -j %s %smanifest.json %spass.json %ssignature %slogo.png %slogo@2x.png %sicon.png %sicon@2x.png %sthumbnail@2x.png %sthumbnail.png' % (CURRENT_PASS, APP_DATA_DIR, APP_DATA_DIR, APP_DATA_DIR, APP_DATA_DIR, APP_DATA_DIR, APP_DATA_DIR, APP_DATA_DIR, APP_DATA_DIR, APP_DATA_DIR)
print cmd2
subprocess.call(cmd2, shell=True)

