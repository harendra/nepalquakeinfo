function NewReportHandler(){
	
	this.initialize=function(){
		//initialize map
		var maphandler=new MapHandlerG();
		var defaultlocation=[27.7000,85.3333];
		maphandler.createMarkableMap(mapCallback,defaultlocation,"canvas");
		
		//send report
	}
	
	function sendReport(){
		
		
	}
	
	function mapCallback(latlon,address,countryname){
		
		$(".latitude").val(latlon.lat());
		$(".longitude").val(latlon.lng());
		$(".help_address").val(address);
		
	}
	
}