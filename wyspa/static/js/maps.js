// Dictionary for color coded moods
const moodMap = {
    1: "#FF0000",
    2: "#FF8000",
    3: "#FFE747",
    4: "#9EFAFA",
    5: "#0FE000"
};

// Main function for initialising Google Maps
function initMap(map_data) {

    // Starting point
    const myLatLng = {
        lat: 56.218923,
        lng: -26.847590
    };

    // Creation of the map
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 3,
        minZoom: 3,
        center: myLatLng,
        fullscreenControl: false,
        zoomControl: true,
        mapTypeControl: false,
        streetViewControl: false,
        // Custom Map ID
        mapId: '65f95462d95daa3',
        // https://stackoverflow.com/questions/9099345/google-maps-api-3-limit-pan-map-bounds
        restriction: { latLngBounds: { north: 83.8, south: -57, west: -180, east: 180 } }
    });

    // Circle Generation
    for (const message in map_data) {

        // Define colour of Circle
        let wyspaColor = moodMap[map_data[message]["mood"]];

        // Add a cirlce for each wyspa
        const wyspaCircle = new google.maps.Circle({
            strokeColor: wyspaColor,
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: wyspaColor,
            fillOpacity: 0.35,
            map,
            radius: 50000,
            center: map_data[message]["location"],
            message_id: map_data[message]["_id"],
        });

        // Onclick event to redirect to the message clicked on
        google.maps.event.addListener(wyspaCircle, 'click', function (event) {
            document.location.href = '/view_message/' + wyspaCircle.message_id;
        });
    }
}
