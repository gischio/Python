import geocoder
import socket
import googlemaps
import webbrowser

ip = socket.gethostbyname(socket.gethostname())
g = geocoder.ip(ip)
g = geocoder.ip('me')

place = geocoder.google('Gattinara, via Aosta, 16')
work = geocoder.google('Km. 0.600 Strada Provinciale 33, Vernate, MI 20080,Italia')
nonna_nina = geocoder.google('via piazza, 16, Marziai, Vas, BL')
prova = geocoder.google('C.DA CARAMITIA, SN - 94011 - AGIRA (EN)')

print prova.latlng
#webbrowser.open('http://maps.google.com/maps?q=' + str(place.lat) + ',' + str(place.lng))
#webbrowser.open('http://maps.google.com/maps?q=' + str(work.lat) + ',' + str(work.lng))
#webbrowser.open('http://maps.google.com/maps?q=' + str(nonna_nina.lat) + ',' + str(nonna_nina.lng))
webbrowser.open('http://maps.google.com/maps?q=' + str(prova.lat) + ',' + str(prova.lng))