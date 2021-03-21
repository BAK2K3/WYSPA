function initMap(map_data) {

    // Starting point
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
        // Custom Map ID
        mapId: '65f95462d95daa3',
        // https://stackoverflow.com/questions/9099345/google-maps-api-3-limit-pan-map-bounds
        restriction: { latLngBounds: { north: 83.8, south: -57, west: -180, east: 180 } }
    });

    for (const message in map_data) {

        // Add a cirlce for each wyspa
        const wyspaCircle = new google.maps.Circle({
            strokeColor: "#FF0000",
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: "#FF0000",
            fillOpacity: 0.35,
            map,
            radius: 100000,
            center: map_data[message]["location"],
            message_id: map_data[message]["_id"],

        });

        // Onclick event to redirect to the message clicked on
        google.maps.event.addListener(wyspaCircle, 'click', function (event) {
            document.location.href = '/view_message/' + wyspaCircle.message_id;
        });
    }
}