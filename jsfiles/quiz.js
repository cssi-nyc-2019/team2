var correct = 0;
var incorrect = 0;
var question = "none";
var input = "none";
var answer = "none";

var ask = function(){ 
	input = prompt(question);
};

var score = function(){ 
	if(input == answer){ 
        correct = correct+1;
    }
    
    else{
    	incorrect = incorrect+1;
    	alert("incorrect");
    }
};

var lazy = function(){
	ask();
	score();
};

