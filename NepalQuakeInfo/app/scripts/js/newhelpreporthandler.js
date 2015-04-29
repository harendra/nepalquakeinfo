function NewReportHandler(){
	
	this.initialize=function(){
		//initialize map
		var maphandler=new MapHandlerG();
		var defaultlocation=[27.7000,85.3333];
		maphandler.createMarkableMap(mapCallback,defaultlocation,"canvas");
		
		//send report
		$(".submit").click(function(){
			sendReport();
		});
	}
	
	function sendReport(){
		
		var reporter_name=$(".reporter_name").val();
		if(reporter_name.length==0){
			alert("Please enter your name");
			return;
		}
		var reporter_email=$(".reporter_email").val();
		if(reporter_email.length==0){
			alert("Please enter your email");
			return;
		}
		var reporter_phone=$(".reporter_phone").val();
		if(reporter_phone.length==0){
			alert("Please enter your phone number");
			return;
		}
		var help_type=$("#help_type").val();
		var details=$(".details").val();
		if(details.length==0){
			alert("Please enter details of the help");
			return;
		}
		var help_address=$(".help_address").val();
		if(help_address.length==0){
			alert("Please enter the address/area.");
			return;
		}
		var latitude=$(".latitude").val();
		var longitude=$(".longitude").val();
		var imagelink=$(".imagelink").val();
		
		var sendobject={
				reporter_name:reporter_name,
				reporter_email:reporter_email,
				reporter_phone:reporter_phone,
				help_type:help_type,
				details:details,
				help_address:help_address,
				latitude:latitude,
				longitude:longitude,
				imagelink:imagelink
		};
		
		displayWait("wait");
		console.log(sendobject);
		
		$.post("/addnewhelpreport",sendobject,function(result){
			console.log(result);
			result=JSON.parse(result);
			console.log(result);
			if(result["result"]=="success"){
				window.location="/thanks"
			}
		});
	}
	
	function mapCallback(latlon,address,countryname){
		/*
		 * Add latitude/longitude and address in the respective fields once
		 * the user clicks the map.
		 */
		$(".latitude").val(latlon.lat());
		$(".longitude").val(latlon.lng());
		$(".help_address").val(address);
		
	}
	
}

