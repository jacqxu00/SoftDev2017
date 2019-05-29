var box = document.getElementById("box");
var boxHeight = box.offsetHeight;
var boxWidth = box.offsetWidth;

//hardcode target as center
//randomize later

var targetX = boxWidth * Math.random();
var targetY = boxHeight * Math.random();


console.log( "target: ( " + targetX + ", " + targetY +")")
console.log( "box height: " + boxHeight );
console.log( "box width: " + boxWidth );

//calculate distance between current mouse pos and target
var distance = function (x0, y0, x1, y1) {
    return Math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
};


var findIt = function(e) {
    var posX = e.clientX;
    var posY = e.clientY;
		var maxDist = distance(0, 0, boxWidth, boxHeight);
    var dist = distance(posX, posY, targetX, targetY);
    var color = (1-dist/maxDist)*100;
		//console.log(color);
		if ( dist <= 80) {
			document.body.style.backgroundColor = 'hsl(360,100%,41%)';
		}
		else {
			document.body.style.backgroundColor = 'hsl(159,100%,' + color + '%)';
		};
};

/*
your OTHER FXNS
*/

box.addEventListener("mousemove", findIt);
