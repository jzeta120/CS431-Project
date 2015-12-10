// initialize the map on the "map" div with a given center and zoom
window.onload = function () {
        var map = L.map('map').setView([40.9045,-74.1195], 10);
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
    };
