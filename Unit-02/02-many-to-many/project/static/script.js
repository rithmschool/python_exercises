$(document).ready(function(){
    function length_less_than_six(string){
    	if(string.length<=6) return true
    	return false
    }

    $("input").on('keyup', function(e){
    	var value = $('input').val()
    	// Can't extract the input value. Is it encrypted??
    	console.log(value)
    	if(length_less_than_six(value)){
    		$('.error').text("Enter a value greater than six characters")
    	} 
    })
});