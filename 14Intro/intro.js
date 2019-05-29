var fib = function(n){
    if( n<= 1) return n;
    return fib(n -1) + fib(n -2);
}

//================== methods ==================

// adds in a new list element to the first list
var i = 8;
var addToList = function(e){
	var li = document.createElement('li');
	var node = document.createTextNode("item " + i);
	li.appendChild(node);
	var list = document.getElementById('thelist');
	list.appendChild(li);
	i++;
	liEvents(li);
};

// adds in a new list element to the second list
var j = 1;
var addToList2 = function(e){
	var li = document.createElement('li');
    	var node = document.createTextNode("item " + fib(j));
	li.appendChild(node);
	var list = document.getElementById('list2');
	list.appendChild(li);
	j++;
};

// changes heading to the item in the list the mouse is hovering over
var changeHeading = function(e){
  var head = document.getElementById('h');
	head.innerHTML = this.innerHTML;
};

//changes heading back to "Hello World!" when mouse isn't hovering over anything
var revertHeading = function(e){
	var head = document.getElementById('h');
	head.innerHTML = "Hello World!";
};


//removes item from list when mouse clicks on it
var removeItem = function(e) {
	var list = document.getElementById('thelist');
	list.removeChild(this);
};

var liEvents = function(e) {
	e.addEventListener('mouseover',changeHeading);
	e.addEventListener('mouseleave',revertHeading);
	e.addEventListener('click',removeItem);
}


//================== run function ==================
var b = document.getElementById('b');
b.addEventListener('click',addToList);

var b2 = document.getElementById('b2');
b2.addEventListener('click',addToList2);

var list1 = document.getElementById('thelist');
var c = list1.getElementsByTagName('li');
for (each of c) {
	liEvents(each);
};

