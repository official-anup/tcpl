// MAP

var map, geojson;

//Add Basemap
var map = L.map("map", {}).setView([18.55, 73.85], 10, L.CRS.EPSG4326);

var googleSat = L.tileLayer(
  "http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
  {
    maxZoom: 35,
    subdomains: ["mt0", "mt1", "mt2", "mt3"]
  }
);

var osm = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

var Esri_WorldImagery = L.tileLayer(
  "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
  {
    attribution:
      "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community"
  }
);
console.log("______________________")
// <!-- -----------------layer displayed------------------------ -->
var baseLayers = {
  SImagery: Esri_WorldImagery,
  GoogleImage: googleSat,
  OSM: osm
};

 
var wms_layer = L.tileLayer.wms(
  "http://localhost:8080/geoserver/zone/wms",
  {
    layers: "	zone:pune-admin-wards",
    format: "image/png",
    transparent: true,
    version: "1.1.0",
    attribution: "pune-admin-wards"
  }
);
var wms_layer1 = L.tileLayer.wms(
  "http://localhost:8080/geoserver/zone/wms",
  {
    layers: "	zone:Dhankawdi_Road",
    format: "image/png",
    transparent: true,
    version: "1.1.0",
    attribution: "Dhankawdi_Road"
  }
);
wms_layer.addTo(map)

var WMSlayers = {
  Dhankawdi_Road: wms_layer1,
  // Village_Boundary: wms_layer,
  // revenue1: wms_layer2, 
  

};
var control = new L.control.layers(baseLayers, WMSlayers).addTo(map);






// var overlayGroup1 = L.layerGroup([layer1, layer2, layer3]);

// var baseLayers = {
//   "Base Map": baseLayer
// };

// var overlayLayers = {
//   "Group 1": overlayGroup1
  
// };

// L.control.layers(baseLayers, overlayLayers).addTo(map);


//<!-- googleEarth popup -->

map.on("dblclick", function(e) {
  var lat = e.latlng.lat.toFixed(15);
  var lng = e.latlng.lng.toFixed(15);
  var popupContent =
    '<a href="https://earth.google.com/web/search/' +
    lat +
    "," +
    lng +
    '" target="_blank">Open in Google Earth</a><br>'+'Latitude : ' + lat + '<br>' + 'Longitude : ' + lng + '<hr>' +
    lat +
    "," +
    lng;
  L.popup().setLatLng(e.latlng).setContent(popupContent).openOn(map);
});

//_______________________________Draw control____________________________________
var polyline = L.polyline([], {
  color: "red"
});
var polygon = L.polygon([], {
  color: "red"
});
var circle = L.circle([], {
  color: "red"
});
var coordinates = [];

var editableLayers = new L.FeatureGroup(); // add the polyline to the FeatureGroup
map.addLayer(editableLayers);

var drawPluginOptions = {
  position: "topright",
  draw: {
    polygon: {
      allowIntersection: true, // Restricts shapes to simple polygons
      shapeOptions: {
        dashArray: "2, 5",
        color: "red"
      }
    },

    polyline: {
      allowIntersection: true, // Restricts shapes to simple polylines
      shapeOptions: {
        dashArray: "2, 5",
        color: "red"
      }
    },

    circle: {
      allowIntersection: true, // Restricts shapes to simple polylines
      shapeOptions: {
        dashArray: "2, 5",
        color: "red"
      }
    },
    // disable toolbar item by setting it to false
    // Turns off this drawing tool
    rectangle: false,
    marker: false
  },
  edit: {
    featureGroup: editableLayers, //REQUIRED!!
    remove: true
  }
};

//****************** */ Initialise the draw control and pass it the FeatureGroup of editable layers*************************
var drawControl = new L.Control.Draw(drawPluginOptions);
map.addControl(drawControl);

map.on("draw:created", function(e) {
  var type = e.layerType;
  var layer = e.layer;

  if (type === "polyline") {
    // add the drawn polyline to the FeatureGroup
    editableLayers.addLayer(layer);

    // update the coordinates variable
    var latlngs = layer.getLatLngs();
    coordinates = latlngs.map(function(latlng) {
      return [latlng.lat, latlng.lng];
    });
    polyline.setLatLngs(coordinates);
  } else if (type === "polygon") {
    // add the drawn polygon to the FeatureGroup
    editableLayers.addLayer(layer);

    // update the coordinates variable
    var latlngs = layer.getLatLngs();
    coordinates = latlngs.map(function(latlng) {
      return [latlng.lat, latlng.lng];
    });
    polygon.setLatLngs(coordinates);
  } else if (type === "circle") {
    // add the drawn polyline to the FeatureGroup
    editableLayers.addLayer(layer);

    // update the coordinates variable
    var latlngs = layer.getLatLngs();
    coordinates = latlngs.map(function(latlng) {
      return [latlng.lat, latlng.lng];
    });
    circle.setLatLngs(coordinates);
  }
});

// **********************************************

// var editableLayers = new L.FeatureGroup();
// map.addLayer(editableLayers);

map.on("draw:created", function(e) {
  var type = e.layerType,
    layer = e.layer;

  editableLayers.addLayer(layer);
});

var north = L.control({
  position: "bottomleft"
});
north.onAdd = function(map) {
  var div = L.DomUtil.create("div", "info legend");
  var imageUrl = northImageUrl;
  div.innerHTML =
    '<img src="' + imageUrl + '" style="height: 20px; width: 30px;">';
  return div;
};
north.addTo(map);

(uri =
  "http://localhost:8080/geoserver/wms?REQUEST=GetLegendGraphic&VERSION=1.0.0&FORMAT=image/png&WIDTH=20&HEIGHT=20&LAYER=topp:states"), {
  // namedToggle: false,
};
L.wmsLegend(uri);
//

// control
// mouse position

//******************************************************************Scale***************************************************************

L.control
  .scale({
    imperial: false,
    maxWidth: 200,
    metric: true,
    position: "bottomleft",
    updateWhenIdle: false
  })
  .addTo(map);

//**************************************************line mesure*************************************************************
L.control
  .polylineMeasure({
    position: "topleft",
    unit: "kilometres",
    showBearings: true,
    clearMeasurementsOnStop: false,
    showClearControl: true,
    showUnitControl: true
  })
  .addTo(map);

//**********************************************************area measure**********************************************************************
var measureControl = new L.Control.Measure({
  position: "topleft"
});
measureControl.addTo(map);

// search-button______________________________________
            $(document).ready(function() {


              var geojsonLayer; // Reference to the GeoJSON layer
              var geojsonFeatures = []; // Array to store GeoJSON features

              $("#btnData2").click(function() {
                  var selectedValue = $("#search-input").val();
                  // console.log("Selected Value:", selectedValue);

                 

                  $.ajax({
                      url: "/searchOnClick/",
                      method: "GET",
                      data: { "selected_value": selectedValue },
                      dataType: "json",
                      success: function(response) {
                        
                          console.log("Responseghgh:", response);

                          geojsonFeatures = response.features;

                          if (geojsonLayer) {
                            geojsonLayer.removeFrom(map);
                        }
        
                          // Process the response data here
                         geojsonLayer = L.geoJSON(response).addTo(map);
                                                
           
                           map.fitBounds(geojsonLayer.getBounds());
                          
                      },
                      error: function(error) {
                      }
                  });
              });
            });


               $("#btnData1").click(function() {
                  ClearMe();
                });




// table on search area//
console.log("______________________")


  
  







map.on("contextmenu", (e) => {
  let size = map.getSize();
  let bbox = map.getBounds().toBBoxString();
  console.log(bbox,size,"??????????????????")


  var container = document.querySelector('.leaflet-control-layers-overlays');

  var checkboxes = container.querySelectorAll('.leaflet-control-layers-selector');

  var checkedValues = [];
  console.log(checkedValues,'aaaaaaaaaaaaaaaa')
 
  checkboxes.forEach(function(checkbox) {
      // Check if the checkbox is checked
      if (checkbox.checked) {
          // Get the label text associated with the checkbox
          var labelText = checkbox.nextElementSibling.textContent.trim();
          checkedValues.push(labelText);
      }
  });
  
  // Display the checked values
  console.log('Checked Values:', checkedValues);

  let layer = 'zone:'+ checkedValues;
  let style = 'zone:'+ checkedValues;
  console.log(layer,"______________________")
  let urrr =
      `http://localhost:8080/geoserver/zone/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetFeatureInfo&FORMAT=image%2Fpng&TRANSPARENT=true&QUERY_LAYERS=${layer}&STYLES&LAYERS=${layer}&exceptions=application%2Fvnd.ogc.se_inimage&INFO_FORMAT=application/json&FEATURE_COUNT=50&X=${Math.round(e.containerPoint.x)}&Y=${Math.round(e.containerPoint.y)}&SRS=EPSG%3A4326&WIDTH=${size.x}&HEIGHT=${size.y}&BBOX=${bbox}`


      // `http://localhost:8080/geoserver/zone/wms?service=WMS&version=1.1.0&request=GetMap&layers=zone%3AVillage_Boundary&bbox=73.31581115722656%2C18.128164291381836%2C74.46541595458984%2C18.988113403320312&width=768&height=574&srs=EPSG%3A4326&styles=&format=application/openlayers`

  // you can use this url for further processing such as fetching data from server or showing it on the map
  console.log(urrr,"first debug")

/////////////////////////////



if (urrr) {
  fetch(urrr)


    .then((response) => response.json()) // Parse the JSON response
    .then((data) => {
     
      geojsonLayer = L.geoJSON(data).addTo(map); // Create a GeoJSON layer
      

      map.fitBounds(geojsonLayer.getBounds()); // Fit the map to the GeoJSON layer bounds
      
    });

    if (geojsonLayer) {
            geojsonLayer.removeFrom(map);
          }
}
////////////////////////////////////////////

  if (urrr) {
    console.log(urrr,"second debug")
      fetch(urrr)

          .then((response) => response.json())
          .then((html) => {

              var htmldata = html.features[0].properties;
              let keys = Object.keys(htmldata);
              let values = Object.values(htmldata);
              let txtk1 = "";
              var xx = 0
              for (let gb in keys) {
                  txtk1 += "<tr><td>" + keys[xx] + "</td><td>" + values[xx] + "</td></tr>"
                  ;
                  
                  xx += 1
                  console.log(xx,"second debug")

              };
              let detaildata1 =
              //     `<div><table  style='width:70%;' class='popup-table' >" +
              // ${txtk1} + "<tr><td>Co-Ordinates</td><td>" + ${e.latlng} +
              //     "</td></tr>+"<tr><td>Co-Ordinates</td><td>" + ${e.latlng} +
              //     "</td></tr></table></div>`

                  `<div><table  style='width:70%;' class='popup-table' > 
                  ${txtk1}  <tr><td>Co-Ordinates</td><td>  ${e.latlng} 
                      </td></tr> <tr><td>Co-Ordinates</td><td>  ${e.latlng} 
                      </td></tr></table></div>`
                      
                      

                      

                  console.log(detaildata1,"detailed data")
         
              L.popup()
                  .setLatLng(e.latlng)
                  .setContent(detaildata1)
                  .openOn(map);
          


            
  // $(document).ready(function () {
  //   console.log("______________+==================")
  //   $('#layerSelect').change(function () {
  //     console.log("_+++++++++++++++++++++++++")
  //       var selectedLayer = $(this).val(); // Get the selected layer value
  //       console.log(selectedLayer,"+++++++++++++++++++++++++++++")
  //       // Send an AJAX request to your Django view
  //       $.ajax({
  //           type: 'GET',  // or 'POST' depending on your view
  //           url: '/getInfoValues/',
  //           data: { 'selected_layer': selectedLayer },  // Send the selected layer value
  //           success: function (response) {
  //               // Update the result element with the response from the view
  //               $('#result').html(response);
  //           },
  //       });
  //   });
  // });
  



          });

  };




});





// for trial
                // $(document).ready(function() {


                //   var geojsonLayer; // Reference to the GeoJSON layer
                //   var geojsonFeatures = []; // Array to store GeoJSON features
    
                //   $("#btnData2").click(function() {
                //       var selectedValue = $("#search-input").val();
                //       console.log("Selected Value second time:", selectedValue);
    
                //       $.ajax({
                //           url: "/Out_table/",
                //           method: "GET",
                //           data: { "selected_value": selectedValue },
                //           dataType: "json",
                //           success: function(response) {
                            
                //               console.log("Response second:", response);
                //               console.log("Response taluka:", response.Taluka_Name);
                //               console.log("Response village:", response.Village_Name);
                //               console.log("Response gut:", response.Gut_Number);

                //               for (let i = 0; i < response.selected_values.length; i++) {
                //                 const value = response.selected_values[i];
                //                 console.log(value)
                //                 // Do something with each value, such as adding it to the PDF table
                //                 // Example: pdf.text(x, y + i * lineHeight, value);
                //             }
                              
                //           },
                //           error: function(error) {
                //               console.log("Error:", error);
                //           }
                //       });
                //   });
                // });
    
    
//                    $("#btnData1").click(function() {
//                       ClearMe();
//                     });
    
    


 //pdf____________________________________________________________
 


 function downloadPDF(username, email) {
 const { jsPDF } = window.jspdf;
  
 html2canvas(document.getElementById('map'), {
     useCORS: true
 }).then(function(canvas) {
     var imgData = canvas.toDataURL('image/png');

     const pdf = new jsPDF('p', 'px', [canvas.width, canvas.height]);
   
     const fontSize = 36;
     const text = 'TCPLgeo';
  
     const textWidth = pdf.getStringUnitWidth(text) * fontSize / pdf.internal.scaleFactor;
     const textHeight = fontSize / pdf.internal.scaleFactor;

     // Calculate the center position
     const pageWidth = pdf.internal.pageSize.getWidth();
     const pageHeight = pdf.internal.pageSize.getHeight();
     const x = (pageWidth - textWidth) / 2;
     const y = 70;

          
      // Set the line width for the border
      pdf.setLineWidth(2);

      // Draw a rectangle around the page to simulate a border
      pdf.rect(5, 5, pageWidth - 10, pageHeight - 10); // Adjust the values for margins
      
// Draw the inner rectangle to simulate the inner line of the border
pdf.rect(10, 10, pageWidth - 20, pageHeight - 20); // Adjust the values for margins

     pdf.addImage(logoimage, 'PNG',(x-70) , 30, 60, 60);
     // Get the height of the canvas element and add it to the PDF
     var imgHeight = canvas.height;
          // const fontSize = 25;
          pdf.setFont('Times New Roman', 'bold'); // Use the regular variant
      
      
          //  pdf.setFontSize(15);
          //  pdf.setTextColor('black');
          //  pdf.text((x+50), 90, ` Block number 22, Lokamanya Nagar, Sadashiv Peth, Pune, Maharashtra 411030`);
           

         
           // Add text above the map (centered both horizontally and vertically)
           pdf.setFont('Times New Roman', 'bold');
           pdf.setFontSize(fontSize);
           pdf.setTextColor('#004aac');
           pdf.text(x, y, text);
     


           // Add user's name to the PDF_______________________________________________________
           const uppercaseUsername = username.toUpperCase();
           pdf.setFont('Times New Roman', 'bold');
           pdf.setFontSize(16);
           pdf.setTextColor('black');
           pdf.text(20, 150, `User:       ${uppercaseUsername} `, null, null, 'left');
          
          //  pdf.text(70, 150, username , null, null, 'left');
     
           // Add user's email to the PDF
           pdf.setTextColor('black');
           pdf.setFont('Times New Roman', 'bold');
           pdf.text(20, 170, `Email:`, null, null, 'left');
           pdf.setTextColor('black');
           pdf.text(70, 170, email, null, null, 'left');


          //  Date__________________________________________________________________________________
                  const currentDate = new Date();
        const options = { day: 'numeric', month: 'long', year: 'numeric',};
        const formattedDate = currentDate.toLocaleDateString('en-US', options);

        const rightAlignedX = pdf.internal.pageSize.getWidth() - pdf.getStringUnitWidth(formattedDate) * 12;
        // const y = 110; // Adjust the Y coordinate as needed
        
        // Add the formatted date to the PDF
        pdf.setFontSize(15);
        pdf.setTextColor('black');
        pdf.text(rightAlignedX, 150, `Date: ${formattedDate}`, null, null, 'right');

        pdf.setFontSize(15);
        pdf.setTextColor('black');
        pdf.text(rightAlignedX, 1350, 'TCPLgeo', null, null, 'right');
// map_______________________________________________________________________
     
             // Add the image to the PDF without any scaling or clipping
           pdf.addImage(imgData, 'PNG', 30, 200, 780, 700);

          //  legend___________________________________________________________________

           pdf.addImage(imageUrl, 'PNG', 30, 900, 750, 200); // Adjust the coordinates and size as needed


          //  table________________________________________________________________
                         
           var selectedValue = $("#search-input").val();
          //  console.log("Selected Value second time:", selectedValue);
           
           $.ajax({
               url: "/Out_table/",
               method: "GET",
               data: { "selected_value": selectedValue },
               dataType: "json",
               success: function(response) {
                var startY = 1150; 
                
                pdf.autoTable({
                  head: [['TALUKA_NAME', 'VILLAGE_NAME','GUT_NUMBER','PLU_ZONE']],
                  body: [[response.Taluka_Name, response.Village_Name,response.Gut_Number,response.selected_values]
                  // ,['','','',response.selected_values[1]],['','','',response.selected_values[2]]
                ],
                  startY: startY,
                  styles: {
                    cellPadding: 5,
                    fontSize: 12,
                    fontStyle: 'bold',
                   
                    lineWidth: 0.2
                }
                });
                // console.log(response.selected_values,'aaaaaaaaa')

 //  NOTE________________________________________________________________

                // pdf.setFont('MyCustomFont');
                pdf.setFontSize(15);
                pdf.setTextColor('black');
                pdf.text(30, 1300, 'NOTE :  This is sample data of Zone-Certificate');
                // Sign_____________________________
            
               
                
                          pdf.save('TCPLmaps.pdf');
               },
               error: function(error) {
                  //  console.log("Error:", error);
               }
           });
                
           
    
          });
         }
    
// Bookmark_____________________________________________________________________
$(document).ready(function() {
  var saveBtn = document.getElementById('saveBtn');

  saveBtn.addEventListener('click', function() {
    var center = map.getCenter(); // Get the center of the map
    var latitude = center.lat;
    var longitude = center.lng;

    // Show popup for entering location name
    Swal.fire({
      title: 'Enter Location Name',
      input: 'text',
      inputPlaceholder: 'Location Name',
      showCancelButton: true,
      confirmButtonText: 'Save',
      showLoaderOnConfirm: true,
      preConfirm: function(name) {
        return new Promise(function(resolve, reject) {
          if (name) {
            resolve(name);
          } else {
            reject('Invalid name');
          }
        });
      },
      
      allowOutsideClick: false,
      customClass: {
        title:'my_swal_title',
        container: 'my-swal-container', // CSS class for the container
        confirmButton: 'my-swal-button', // CSS class for the confirm button
        cancelButton: 'my-swal-button', // CSS class for the cancel button
        input: 'my-swal-input', // CSS class for the input field
      },
    }).then(function(name) {
      if (name.isConfirmed) {
        var locationName = name.value;
        var username = '{{ request.user.username }}'; // Assuming you are using Django's authentication system

        saveLocationToDB(latitude, longitude, locationName, username);
      }
    }).catch(function(error) {
      Swal.showValidationMessage(error);
    });
  });

  function saveLocationToDB(latitude, longitude, locationName, username) {
    $.ajax({
      url: '/save-location/',
      method: 'POST',
      data: {
        latitude: latitude,
        longitude: longitude,
        name: locationName,
        username: username
      },
      success: function(response) {
        // console.log(response.message); // Log the response message
      },
      error: function(xhr, errmsg, err) {
        // console.log(xhr.status + ': ' + xhr.responseText);
      }
    });
  }

  $(document).on('click', '#locationTable td.name', function() {
    var latitude = parseFloat($(this).data('latitude'));
    var longitude = parseFloat($(this).data('longitude'));
    map.flyTo([latitude, longitude], 17);
  });
                                                // for zoom
  function fetchLocations() {
          $.ajax({
            url: "/get-locations/",
            method: "GET",
            success: function (response) {
              var locations = response.locations;
              var tableBody = $("#locationTable tbody");
              tableBody.empty();

              $.each(locations, function (index, location) {
                var row = $("<tr>");
                row.data("location-id", location.id); // Store the location ID in the row data attribute
                $("<td>", {
                  class: "name",
                  text: location.name,
                  "data-latitude": location.latitude,
                  "data-longitude": location.longitude,
                }).appendTo(row);
                // $("<td>", { text: location.latitude }).appendTo(row);
                // $("<td>", { text: location.longitude }).appendTo(row);
                var deleteButton = $("<button>", { text: "Delete"  });
                var deleteButtonWrapper = $("<td>", {
                  class: "delete-button",
                }).append(deleteButton);
                row.append(deleteButtonWrapper);
                row.appendTo(tableBody);
              });
            },
            error: function (xhr, errmsg, err) {
              // console.log(xhr.status + ": " + xhr.responseText);
            },
          });
        }

      
                                            // for Delete
  $(document).on("click", ".delete-button button", function () {
    var row = $(this).closest("tr");
    var locationId = row.data("location-id");

    Swal.fire({
      title: "Confirm Deletion",
      text: "Are you sure you want to delete this location?",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#dc3545",
      confirmButtonText: "Delete",
      cancelButtonText: "Cancel",
      reverseButtons: true,
      customClass: {
        text:"my_swal_text",
        title:"my_swal_title",
        icon:"my_icon",
        container: "my-swal-delete-container",
        confirmButton: "my-swal-button",
        cancelButton: "my-swal-button",
        actions: "my-swal-actions",
      },
    }).then(function (result) {
      if (result.isConfirmed) {
        deleteLocationFromDB(locationId, row);
      }
    });
  });

  function deleteLocationFromDB(locationId, row) {
    $.ajax({
      url: "/delete-location/",
      method: "POST",
      data: {
        locationId: locationId,
      },
      success: function (response) {
        // console.log(response.message); // Log the response message
        row.remove(); // Remove the deleted row from the table
      },
      error: function (xhr, errmsg, err) {
        // console.log(xhr.status + ": " + xhr.responseText);
      },
    });
  }

  fetchLocations();
  setInterval(fetchLocations, 1000);
});

//________elivation profile________
//////////////////////////////////////

// Define an array of coordinates (latitudes and longitudes) along your route
var coordinates = [
  [lat1, lon1],
  [lat2, lon2],
  // ... Add more coordinates as needed
];

// Create an array to store elevation data
var elevations = [];

// Make a request to the Google Elevation API to fetch elevation data
coordinates.forEach(function(coord) {
  var url = `https://maps.googleapis.com/maps/api/elevation/json?locations=${coord[0]},${coord[1]}&key=YOUR_API_KEY`;

  fetch(url)
      .then(response => response.json())
      .then(data => {
          if (data.status === 'OK') {
              elevations.push(data.results[0].elevation);
          }
      });
});


// Create a Chart.js chart to display the elevation profile graph
var ctx = document.getElementById('elevation-profile').getContext('2d');
var elevationChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [], // Add labels for each point if needed
        datasets: [{
            label: 'Elevation Profile',
            data: elevations,
            borderColor: 'blue',
            borderWidth: 1,
        }]
    },
    options: {
        // Configure chart options as needed
    }
});



/////////////////////////////////////////
   