function ReportList(){
	
	this.initialize=function(){
		
		//handle map
		var mapdata=JSON.parse($(".mapdata").text());
		var maphandler=new MapHandlerG();
		var defaultlocation=[27.7000,85.3333];
		maphandler.createMapWithMarker("canvas",defaultlocation[0],defaultlocation[1],11);
		var locations=[];
		for(var i=0;i<mapdata.length;i++){
			locations.push([mapdata[i]["latitude"],mapdata[i]["longitude"]]);
		}
		maphandler.addMultipleMarkers(locations);
	}
}