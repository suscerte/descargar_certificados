#!/usr/lib/python3
import urllib

direccion = "http://acraiz.suscerte.gob.ve/sites/default/files/certificados/"
certificados = []

certificados.append("CERTIFICADO-RAIZ-SHA384.crt")
certificados.append("CERTIFICADO-RAIZ-SHA1.crt")
certificados.append("PSCFII-SHA256.crt")
certificados.append("PSC-PROCERT-SHA256.crt") 
certificados.append("CERTIFICADO-SHA384-AC-IDYSEG-1-2013.crt")

for certificado in certificados:
    print(certificado)
    urllib.urlretrieve("%s%s" % (direccion, certificado), filename="%s" % (certificado))
