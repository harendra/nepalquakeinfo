function displayWait(dispid){
	//requires common.js
	va image=$("<img src='/images/wait.gif'>")
	$("#"+dispid).append(image);
}


function removeWait(dispid){
	$("#"+dispid).empty();
}