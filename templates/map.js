//script used to display autocomplete predictions
function initService() {
    const displaySuggestions = function (predictions, status) {
      if (status != google.maps.places.PlacesServiceStatus.OK || !predictions) {
        alert(status);
        return;
      }

      const windsor = new google.maps.LatLng(42.314, 83.036); //map centered on windsor coordinates
      
      //create a list element for each auto complete suggestion
      predictions.forEach((prediction) => {
        const li = document.createElement("li");
  
        li.appendChild(document.createTextNode(prediction.description));
        document.getElementById("results").appendChild(li);
      });
    };
  
    const service = new google.maps.places.AutocompleteService();
  }
  
  window.initService = initService;