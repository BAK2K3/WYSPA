
function initMap() {
    const myLatLng = {
        lat: 56.218923,
        lng: -26.847590
    };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 3,
        minZoom: 3,
        center: myLatLng,
        fullscreenControl: false,
        zoomControl: true,
        mapTypeControl: false,
        streetViewControl: false,
        mapId: '65f95462d95daa3',
        // https://stackoverflow.com/questions/9099345/google-maps-api-3-limit-pan-map-bounds
        restriction: { latLngBounds: { north: 83.8, south: -57, west: -180, east: 180 } }
    });

}