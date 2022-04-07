const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// const map = L.map('map')
var map = L.map('map').setView([-1.3222615,
36.7740272,], 13);
var marker = L.marker([-1.3222615,
    36.7740272],{
    color:'red',
}).addTo(map);

var popup = L.popup()
    .setLatLng([-1.3222615,
        36.7740272])
    .setContent("St Mary's Hospital")
    .openOn(map);

var map2 = L.map('map2').setView([ -1.3121609,
36.8168874,], 15);
var marker2 = L.marker([-1.3121609,
    36.8168874,],{
            color:'red',
        }).addTo(map2);
        
var popup2 = L.popup()
    .setLatLng([-1.3121609,
        36.8168874,])
    .setContent("The Aga Khan Hospital")
    .openOn(map2);
            
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibWlzaGFlbHJhdGVtbyIsImEiOiJjbDFvemQ3YmQwMnVsM2twdHA1aWhkcXp5In0.ymXuZCHcv6oflX3gSIkCOg'
}).addTo(map);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibWlzaGFlbHJhdGVtbyIsImEiOiJjbDFvemQ3YmQwMnVsM2twdHA1aWhkcXp5In0.ymXuZCHcv6oflX3gSIkCOg'
}).addTo(map2);

// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
// map.fitWorld();
// const markers = JSON.parse(document.getElementById('markers-data').textContent);
// let feature = L.geoJSON(markers).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
// map.fitBounds(feature.getBounds(), { padding: [100, 100] });

// pk.eyJ1IjoibWlzaGFlbHJhdGVtbyIsImEiOiJjbDFvemQ3YmQwMnVsM2twdHA1aWhkcXp5In0.ymXuZCHcv6oflX3gSIkCOg