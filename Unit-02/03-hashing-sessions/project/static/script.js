$(document).ready(function(){
    function length_less_than_six(string){
    	if(string.length<=6) return true
    	return false
    }

    $("#password").on('keyup', function(e){
        var value = e.target.value;
        var $inputId = `#${e.target.id}` 
        if (length_less_than_six(value)) {
            console.log($inputId)
            $($inputId).next().text("Make password longer than six characters")
        }
        else {
            $($inputId).next().empty()
        }
    })
});
