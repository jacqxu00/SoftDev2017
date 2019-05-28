var fibonacci = function(n) {
	if (n == 0) {
		return 0;
	} else if (n == 1) {
		return 1;
	} else {
		return fibonacci(n-1) + fibonacci(n-2);
	};
};

var gcd = function(a, b) {
	if (a == b) {
		return a;
	} else if (a < b) {
		if (a == 0) {
			return b;
		};
		return gcd(b%a, a);
	} else {
		if (b == 0) {
			return a;
		};
		return gcd(a%b, b);
	};
};

var classes = [ 'Yu Qi', 'Michela', 'Kristin', 'Fabiha', 'Maxim', 'Marcus', 'Ish', 'James', 'Ryan', 'Edward', 'Adeeb', 'Jake', 'Cynthia', 'Kevin', 'Levi', 'Edmond', 'Kyle', 'Andrew', 'Max', 'Jenny', 'Philip', 'Shan', 'Mansour', 'Ray', 'Jake', 'Ida', 'Kerry', 'Stanley', 'Jackie', 'William', 'Tina', 'Michael'];

var randomStudent = function() {
	var i = Math.floor(Math.random() * classes.length);
	return classes[i];
};