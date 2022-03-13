function navigateToAddress() {
    document.getElementById("step2").classList.add("completed")
    document.getElementById("personal_info").classList.add("hide-element")
    document.getElementById("address_info").classList.remove("hide-element");
    document.getElementById("sign-in").classList.add("hide-element");
    document.getElementById("step3").classList.remove("completed")
    document.getElementById("step-completed").innerHTML = '3';
}

function navigateToSignIn(){
    document.getElementById("step2").classList.add("completed")
    document.getElementById("step3").classList.add("completed")
    document.getElementById("step-completed").innerHTML = '&#x2714';
    document.getElementById("address_info").classList.add("hide-element");
    document.getElementById("sign-in").classList.remove("hide-element");
}

function navigatePersonalInfo(){
    document.getElementById("step2").classList.remove("completed")
    document.getElementById("personal_info").classList.remove("hide-element")
    document.getElementById("address_info").classList.add("hide-element");
    document.getElementById("sign-in").classList.add("hide-element");
}

function setDefaultVisibility(){
    document.getElementById("personal_info").classList.remove("hide-element")
    document.getElementById("address_info").classList.add("hide-element");
    document.getElementById("step2").classList.remove("completed")
    document.getElementById("step3").classList.remove("completed")
    document.getElementById("step-completed").innerHTML = '3';
    document.getElementById("sign-in").classList.add("hide-element");
}

function submitResendOtp(){
    document.getElementById("resend_otp").classList.remove("hide-element");
    document.getElementById("btn_sendotp").innerHTML = "Submit";
    
}

$(document).ready(function(){
	
    $("#signUp").on('shown.bs.modal', function(){
        let txtPassword = document.getElementById("txt_password");
        txtPassword.onfocus = () => {
            document.getElementById("strong_password").style.display = "block";
        }
        txtPassword.onblur = () => {
            document.getElementById("strong_password").style.display = "none";
        }
        txtPassword.onkeyup = function() {
            $("#txt_password").removeClass("border-color");
            let lowercase = document.getElementById("lowercase")
            let uppercase = document.getElementById("uppercase")
            let number = document.getElementById("number")
            let password = document.getElementById("password_length")
            let special_char = document.getElementById("special_char")
            let lowerCaseLetters = /[a-z]/g;
            if(txtPassword.value.match(lowerCaseLetters)) {
                lowercase.classList.remove("invalid");
                lowercase.classList.add("valid");
            } else {
                lowercase.classList.remove("valid");
                lowercase.classList.add("invalid");
            }
            let upperCaseLetters = /[A-Z]/g;
            if(txtPassword.value.match(upperCaseLetters)) {
                uppercase.classList.remove("invalid");
                uppercase.classList.add("valid");
            } else {
                uppercase.classList.remove("valid");
                uppercase.classList.add("invalid");
            }
            let numbers = /[0-9]/g;
            if(txtPassword.value.match(numbers)) {
                number.classList.remove("invalid");
                number.classList.add("valid");
            } else {
                number.classList.remove("valid");
                number.classList.add("invalid");
            }
            let special = /[!@#$&*]/g;
            if(txtPassword.value.match(special)) {
                special_char.classList.remove("invalid");
                special_char.classList.add("valid");
            } else {
                special_char.classList.remove("valid");
                special_char.classList.add("invalid");
            }
            if(txtPassword.value.length >= 8) {
                password.classList.remove("invalid");
                password.classList.add("valid");
            } else {
                password.classList.remove("valid");
                password.classList.add("invalid");
            }
        }
        
        document.getElementById("txt_renter_password").onkeyup = function() {
            let password1 = $('input[id=txt_password]').val()
            let re_enter_password = $('input[id=txt_renter_password]').val()
            if(password1 == ''){
                $("#txt_password").addClass("border-color");
            }
            if(re_enter_password == '' || password1 == re_enter_password){
                document.getElementById("password_not_match_span").innerText = "";
            }
            if(password1 != re_enter_password){
                document.getElementById("password_not_match_span").innerText = "Password doesn\'t match";
            }
        }

        document.getElementById("btntogglepassword").onclick = () => {
            var txt_password = document.getElementById("txt_password");
            if (txt_password.type === "password") {
                txt_password.type = "text";
                $("#btntogglepassword1").removeClass("glyphicon glyphicon-eye-close")
                $("#btntogglepassword1").addClass("glyphicon glyphicon-eye-open")
            } else if (txt_password.type === "text"){
                txt_password.type = "password";
                $("#btntogglepassword1").removeClass("glyphicon glyphicon-eye-open")
                $("#btntogglepassword1").addClass("glyphicon glyphicon-eye-close")
            }
        }

        document.getElementById("btntogglepassword2").onclick = () => {
            var txt_password = document.getElementById("txt_renter_password");
            if (txt_password.type === "password") {
                txt_password.type = "text";
                $("#btntogglepassword3").removeClass("glyphicon glyphicon-eye-close")
                $("#btntogglepassword3").addClass("glyphicon glyphicon-eye-open")
            } else if (txt_password.type === "text"){
                txt_password.type = "password";
                $("#btntogglepassword3").removeClass("glyphicon glyphicon-eye-open")
                $("#btntogglepassword3").addClass("glyphicon glyphicon-eye-close")
            }
        }
    });
    
    $("#txt_manufacturer").change(function(){
		let mname = $('#txt_manufacturer').val()
		if(mname == ''){
			$('#txt_model').empty();
			$('#txt_model').append('<option value=0>' +'---None---' +'</option>');
			$('#txt_model').val(0)
		}
		else{
			jQuery.ajax({type: "GET",
			url:'/Search',
			data: {'value':mname},
			dataType: 'json',
			success: function (response){
				$('#txt_model').empty();
				$('#txt_model').append('<option value=0>' +'---None---' +'</option>');
				for (var index = 0; index <= response.selected_car_models.length; index++) {
      				$('#txt_model').append('<option value="' + response.selected_car_models[index][0] + '">' + response.selected_car_models[index][2] + '</option>');
   				}
			}
		});
	  }
	});
  });