// Dictionary for color coded moods
const moodMap = {
  1: "#FF0000",
  2: "#FFFFFF",
  3: "#0FE000",
};

// Main function for initialising Google Maps
function initMap(map_data) {
  // Starting point
  const myLatLng = {
    lat: 56.218923,
    lng: -26.84759,
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
    mapId: "65f95462d95daa3",
    // https://stackoverflow.com/questions/9099345/google-maps-api-3-limit-pan-map-bounds
    restriction: {
      latLngBounds: { north: 83.8, south: -57, west: -180, east: 180 },
    },
  });

  // Circle Generation
  for (const message in map_data) {
    // https://stackoverflow.com/questions/4166551/javascript-jslint-error-the-body-of-a-for-in-should-be-wrapped-in-an-if-statem
    if (map_data.hasOwnProperty(message)) {
      // Define colour of Circle
      let wyspaColor = moodMap[map_data[message].mood];

      // https://developers.google.com/maps/documentation/javascript/examples/circle-simple
      // Add a cirlce for each wyspa
      const wyspaCircle = new google.maps.Circle({
        strokeColor: wyspaColor,
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: wyspaColor,
        fillOpacity: 0.35,
        map,
        // https://stackoverflow.com/questions/5842747/how-can-i-use-javascript-to-limit-a-number-between-a-min-max-value
        radius: Math.min(
          1000000,
          Math.max(10000, 10000 + map_data[message].listens * 5000)
        ),
        center: map_data[message].location,
        message_id: map_data[message]._id,
      });

      // Onclick event to redirect to the message clicked on
      google.maps.event.addListener(wyspaCircle, "click", function (event) {
        document.location.href = "/view_message/" + wyspaCircle.message_id;
      });
    }
  }
}

// Catch any Gmaps Auth Fails
function gm_authFailure() {
  // Replace Gmaps with Static Map
  document.getElementById("map").children[0].id = "staticMap";
  // Remove the alert
  document.getElementById("map").children[0].children[0].remove();
  // Unhide the error container
  document
    .getElementsByClassName("hidden-error")[0]
    .classList.remove("hidden-error");
}
