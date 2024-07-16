function changeBackgroundColor(color){
if (document.body.style.background === 'red'){
	color = 'yellow';
	document.body.style.background = color;
}
else{
	color = 'red'
	document.body.style.background = color;
}
}
