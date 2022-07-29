var reader = new FileReader();
reader.onload = function(event) {
	var testo = event.target.result;
	document.getElementById("contenuto").innerHTML = testo;
};
reader.readAsText(file);