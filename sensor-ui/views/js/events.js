function getSensor(propTag) {
  var request = new XMLHttpRequest();
  request.open("GET", "/sensor", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);
    document.getElementById(propTag).innerHTML = response.moisture

    if(response.moisture < 400) {
      document.body.className = "warning"
    } else {
      document.body.className = "normal"
    }

    getSensor(propTag)
  };

  request.send();
}
