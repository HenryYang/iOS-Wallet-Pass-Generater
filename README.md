# iOS-Wallet-Pass-Generater

### Using Openssl to sign your own iOS Wallet Pass

***The MOST important is USING SHA1 to sign the signature file***

Please rember modify **teamIdentifier** & **passTypeIdentifier** in pass.json


![](https://raw.githubusercontent.com/HenryYang/blog_md_backup/master/%E5%B7%B2%E5%AE%8C%E6%88%90/PIC/IMG_2635.jpg)


Tips:

* Convert pass.cer to cert.pem

`openssl x509 -inform der -in pass.cer -out cert.pem`

*  First, Import pass.cer to keychain first. Then, Export as Certificates.p12 and convert to private.key

`openssl pkcs12 -in cert.p12 -nodes -out private.key -nocerts`

* The Officeal Apple WWDR certificate and convert to pem

`https://developer.apple.com/certificationauthority/AppleWWDRCA.cer`

`openssl x509 -inform der -in AppleWWDRCA.cer -out AppleWWDRCA.pem`

## reference:

https://gist.github.com/dschuetz/2da732c5fba5fc9005de

https://blog.krishan711.com/generating-ios-push-certificates



