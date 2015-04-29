function displayWait(dispid){
	//requires common.js
	var image=$("<img src='/images/wait.gif'>")
	$("#"+dispid).append(image);
}


function removeWait(dispid){
	$("#"+dispid).empty();
}