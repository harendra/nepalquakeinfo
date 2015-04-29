function MapHandlerG() {
    var map = null;
    var marker = null;
    var mapcontainerid = null;
    var locationcontainerid = null;
    var searchbuttonid = null;
    var countryname = null;
    var birdid = null;
    var geolocationprefix = "geo";
    defaultmaplocation = [37.0625, -95.677068];
    var markersarray=[];
    
    var infowindow = new google.maps.InfoWindow({
        size : new google.maps.Size(150, 50)
    });
    
    function createMap(lat, lon, zoomlevel) {
        if (zoomlevel == null) {
            zoomlevel = 13;
        }
        var myOptions = {
            zoom : zoomlevel,
            center : new google.maps.LatLng(lat, lon),
            mapTypeControl : true,
            mapTypeControlOptions : {
                style : google.maps.MapTypeControlStyle.DROPDOWN_MENU
            },
            navigationControl : true,
            mapTypeId : google.maps.MapTypeId.ROADMAP
        }
        map = new google.maps.Map(document.getElementById(mapcontainerid), myOptions);
        google.maps.event.addListener(map, 'click', function() {
            infowindow.close();
        });
    }
    
    this.clearAllmarkers=function(){
    	 for (var i = 0; i < markersarray.length; i++ ) {
    			markersarray[i].setMap(null);
  		}
    }
    
    // A function to create the marker and set up the event window function
    function createMarker(latlng, name, html) {
        var contentString = html;
        var marker = new google.maps.Marker({
            position : latlng,
            map : map,
            zIndex : Math.round(latlng.lat() * -100000) << 5
        });
        markersarray.push(marker);
        return marker;
    }
    
    this.createMapWithMarker = function(containerID, lat, lng, zoomlevel) {
        if (zoomlevel == null) {
            zoomlevel = 5;
        }
        var myOptions = {
            zoom : zoomlevel,
            center : new google.maps.LatLng(lat, lng),
            mapTypeControl : true,
            mapTypeControlOptions : {
                style : google.maps.MapTypeControlStyle.DROPDOWN_MENU
            },
            navigationControl : true,
            mapTypeId : google.maps.MapTypeId.ROADMAP
        }
        map = new google.maps.Map(document.getElementById(containerID), myOptions);
        if (marker) {
            marker.setMap(null);
            marker = null;
        }
        var latlng = new google.maps.LatLng(lat, lng, true);
        createMarker(latlng, 'name', 'location');
    }
    
    function createMarkerWithLinks(latlng, name, html, link) {
        marker = createMarker(latlng, name, html);
        google.maps.event.addListener(marker, 'click', function() {
            window.location = link;
        });
    }
    
    this.addNewMarker = function(latlng) {
        var newmarker = createMarker(latlng, 'name', 'location');
        map.setCenter(newmarker.getPosition());
        //map.setZoom(5);
    }
    
    this.addMarkerByPoint=function(point){
    	 var latlng=new google.maps.LatLng(point[0], point[1]);
         var marker=createMarker(latlng,'name','location');
    	
    }
    
    this.addMultipleMarkers=function(locationlist){
        for(var i=0;i<locationlist.length;i++){
            var currentlocation=locationlist[i];
            var latlng=new google.maps.LatLng(currentlocation[0], currentlocation[1]);
            var marker=createMarker(latlng,'name','location');
        }
        map.setCenter(marker.getPosition());
        //map.setZoom(12);
    }
    
    this.changeFocus=function(latlng,zoomlevel){
    	console.log(latlng[0]);
    	console.log(latlng[1]);
        var lat=parseFloat(latlng[0]);
        var lng=parseFloat(latlng[1]);
        var location=new google.maps.LatLng(lat, lng);
        map.setCenter(location);
        if(zoomlevel!=null && map.getZoom()<zoomlevel){
        	map.setZoom(zoomlevel);
        }
    }
    
    this.initialize = function(mapcanvas) {
        //alert('here');
        mapcontainerid = mapcanvas;
        countryname = 'California';
        var geocoder = new google.maps.Geocoder();
        geocoder.geocode({
            'address' : countryname
        }, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                var result = results[0];
                var geom = result['geometry'];
                var latlon = geom['location'];
                var lat = 12.618897;
                var lon = 26.861572;
                //createMap(latlon['Ua'], latlon['Va']);
                createMap(lat, lon);
                handleSearch();
                handleMarkerEvent();
            }
        });
    }
    
    this.createClickableMap = function(callback, defaultlocation, canvasid) {
        if (defaultlocation != null) {
            var lat = defaultlocation[0];
            var lon = defaultlocation[1];
        } else {
            var lat = defaultmaplocation[0];
            var lon = defaultmaplocation[1];
        }
        mapcontainerid = canvasid;
        createMap(lat, lon);
        handleMarkerEvent(callback);
    }

    this.createMarkableMap = function(callback, defaultlocation, canvasid) {
        if (defaultlocation != null) {
            var lat = defaultlocation[0];
            var lon = defaultlocation[1];
        } else {
            var lat = defaultmaplocation[0];
            var lon = defaultmaplocation[1];
        }
        mapcontainerid = canvasid;
        createMap(lat, lon);
        handleMarkerAddEvent(callback);
    }
    
    function handleMarkerAddEvent(callback){
        google.maps.event.addListener(map, 'click', function(event) {
            //call function to create marker
            if (marker) {
                marker.setMap(null);
                marker = null;
            }
            marker = createMarker(event.latLng);
            getReverseGeoCode(event.latLng, callback);
        });
    	
    }
    
    function getCountryName(latlng,callback){
    	var geocoder=new google.maps.Geocoder();
    	geocoder.geocode({
    		latLng:latlng,
    		language:'en'
    	},function(results,status){
    		var addresscomp=results[0].address_components;
    		for(var i=0;i<addresscomp.length;i++){
    			if(addresscomp[i].types[0]=='country'){
    				var countryname=addresscomp.shortname
    			}
    		}
    		
    	});
    }
    
    function getReverseGeoCode(latlng, callback) {
        var geocoder = new google.maps.Geocoder();
        //var latlng = new google.maps.LatLng(lat, lng, true);
        geocoder.geocode({
            latLng : latlng
        }, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                if (results[0]) {
                    formattedaddress = results[0].formatted_address;
                    addcomp = results[0].address_components;
                    for(var i=0;i<addcomp.length;i++){
    					if(addcomp[i].types[0]=='country'){
    						var countryname=addcomp[i].short_name
    					}
    				}
                    callback(latlng, formattedaddress, countryname);
                }
            }
        });
    }
    
    this.getGeoCode=function(address,callback){
    	console.log(address);
    	var geocoder=new google.maps.Geocoder();
    	geocoder.geocode({
    		address:address
    	},function(results,status){
    		console.log('result');
    		console.log(results);
            if (status == google.maps.GeocoderStatus.OK) {
                if (results[0]) {
                    formattedaddress = results[0].formatted_address;
                    addcomp = results[0].address_components;
                    for(var i=0;i<addcomp.length;i++){
    					if(addcomp[i].types[0]=='country'){
    						var countryname=addcomp[i].short_name
    					}
    				}
    				var latlng=results[0].geometry.location;
    				console.log(latlng);
                    callback(latlng, formattedaddress, countryname);
                }
            }
    	});
    }
    
    function handleMarkerEvent(callback) {
        google.maps.event.addListener(map, 'click', function(event) {
            //call function to create marker
            if (marker) {
                marker.setMap(null);
                marker = null;
            }
            //marker = createMarker(event.latLng);
            getReverseGeoCode(event.latLng, callback);
        });
    }
    
    this.loadDefaultLocation = function(containerid) {
        mapcontainerid = containerid;
        createMap(defaultmaplocation[0], defaultmaplocation[1], 2);
    }
    
    this.addLocationsWithMarker = function(containerid, locations, defaultlocation) {
        mapcontainerid = containerid;
        createMap(defaultlocation[0], defaultlocation[1]);
        for (var i = 0; i < locations.length; i++) {
            var marker = null;
            if (marker) {
                marker.setMap(null);
                marker = null;
            }
            //var link=locations[i]['link'];
            var latlng = new google.maps.LatLng(locations[i][0], locations[i][1], true);
            marker = createMarker(latlng, "name", "disp", null);
        }
    }
}