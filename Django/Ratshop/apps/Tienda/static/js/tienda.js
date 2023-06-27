let map;

function initMap() {
  const duoc = { lat: -33.5000852, lng: -70.6162928 };
  const map = new google.maps.Map(document.getElementById("map"), {
    scaleControl: true,
    center: duoc,
    zoom: 16,
  });
  const infowindow = new google.maps.InfoWindow();
  const marker = new google.maps.Marker({ map, position: duoc });

  marker.addListener("click", () => {
    infowindow.open(map, marker);
  });
}y