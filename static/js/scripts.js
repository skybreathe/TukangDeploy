{% load staticfiles %}
function draw_button(){
var imageObj = new Image();
imageObj.src = "{% static 'img/favicon.png' %}";
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
//ctx.fillRect(20,20,20,20);
ctx.drawImage(imageObj, 10,20,80,70 );
var canvasOffset=$("#myCanvas").offset();
var offsetX=canvasOffset.left;
var offsetY=canvasOffset.top;
var canvasWidth=c.width;
var canvasHeight=c.height;
var isDragging=false;
	function handleMouseDown(e){
	  canMouseX=parseInt(e.clientX-offsetX);
	  canMouseY=parseInt(e.clientY-offsetY);
	  // set the drag flag
	  isDragging=true;
	  
	}

	function handleMouseUp(e){
	  canMouseX=parseInt(e.clientX-offsetX);
	  canMouseY=parseInt(e.clientY-offsetY);
	  // clear the drag flag
	  isDragging=false;
	}

	function handleMouseOut(e){
	  canMouseX=parseInt(e.clientX-offsetX);
	  canMouseY=parseInt(e.clientY-offsetY);
	  // user has left the canvas, so clear the drag flag
	  //isDragging=false;
	}

	function handleMouseMove(e){
	  canMouseX=parseInt(e.clientX-offsetX);
	  canMouseY=parseInt(e.clientY-offsetY);
	  // if the drag flag is set, clear the canvas and draw the image
	  if(isDragging){
		  ctx.clearRect(0,0,canvasWidth,canvasHeight);
		  ctx.drawImage(imageObj,canMouseX-128/2,canMouseY-120/2,80,70);
	  }
	}

	$("#myCanvas").mousedown(function(e){handleMouseDown(e);});
	$("#myCanvas").mousemove(function(e){handleMouseMove(e);});
	$("#myCanvas").mouseup(function(e){handleMouseUp(e);});
	$("#myCanvas").mouseout(function(e){handleMouseOut(e);});
}