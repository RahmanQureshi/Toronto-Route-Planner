var map;
var currentPath = new google.maps.Polyline({
    path: [],
    geodesic: true,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 2
});

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: { lat: 43.7000, lng: -79.4000},
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });
  drawBoundary();
}

function appendTextDirections(textDirections) {
    $textDirectionsBox = $('#text-directions-box');
    $textDirectionsBox.empty();
    for(var i = 0; i < textDirections.length; i++){
        var classes = ""
        if(i%2 == 0) {
          classes = "text-directions one";
        } else {
          classes = "text-directions two"
        }
        var $div = $("<div>", {class: classes});
        $div.text(textDirections[i]);
        $textDirectionsBox.append($div);
    }
}

function drawBoundary() {
  $.get( "/former-municipalities", function( data ) {
    data = data['toronto'];
    setPolyLine(data, '#00ffff' , 2);
  });
}

function setPolyLine(latLngList, color) {
  currentPath = new google.maps.Polyline({
    path: latLngList,
    geodesic: true,
    strokeColor: color,
    strokeOpacity: 1.0,
    strokeWeight: 2
  });
  currentPath.setMap(map);
  return currentPath;
}

var currentDisplayedRoute = null;
$('#route-calculator-form').submit(function (e){
  e.preventDefault();
  $.ajax({
    url: $(this).attr('action'),
    data: $(this).serialize(),
    success: function(data)
    {
      if (data['error'] != undefined)
      {
        $('#loading').css('display', 'none');
        $('#error').css('display', 'block');
      }
      else
      {
        if(currentDisplayedRoute != null) {
          currentDisplayedRoute.setMap(null);
        }
        $('#loading').css('display', 'none');
        $('#error').css('display', 'none');
        $('#distance-box').html(data['length'].toFixed(2) + 'km')
        width = $(window).width();
        if (width < 798)
        {
          $('#text-directions-box').css('height', 'auto')
        }
        appendTextDirections(data['pretty-driving-directions']);
        currentDisplayedRoute = setPolyLine(data['latLngList'], '#FF0000');
        latLng1 = {'lat':data['latLngList'][0]['lat'], 'lng':data['latLngList'][0]['lng']};
        latLng2 = {'lat': data['latLngList'][data['latLngList'].length-1]['lat'], 
                  'lng': data['latLngList'][data['latLngList'].length-1]['lng']}
        bounds = new google.maps.LatLngBounds(latLng1, latLng2);
        map.fitBounds(bounds);
      }
    },
    error: function(data)
    {
      $('#loading').css('display', 'none');
      $('#error').css('display', 'block');
    }
  });
  appendTextDirections([]);
  $('#error').css('display', 'none');
  $('#loading').css('display', 'block');
});

$(window).resize(function () {
  $('#map').css('height', $(window).height() - $('#header').outerHeight() + 'px');
  width = $(window).width();
  if(width<798) {
    $('#text-directions-box').css('height', 'auto');
  } else {
    $('#text-directions-box').css('height', '325px');
  }
});

$('#collapseButton').click(function () {
  $('#side-bar').collapse('toggle');
});

/** INITIALIZATION **/
(function init() {
  $('#side-bar').collapse('show');
  $('#map').css('height', $(window).height() - $('#header').outerHeight() + 'px');
  width = $(window).width();
  if (width<798)
  {
    $('#text-directions-box').css('height', 'auto');
  }
  google.maps.event.addDomListener(window, 'load', initMap);
})();
