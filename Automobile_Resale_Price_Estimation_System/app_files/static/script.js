function navigateToAddress() {
    document.getElementById("step2").classList.add("completed")
    document.getElementById("personal_info").classList.add("hide-element")
    document.getElementById("address_info").classList.remove("hide-element");
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
}

function returnToHome(){
    document.getElementById("personal_info").classList.remove("hide-element")
    document.getElementById("address_info").classList.add("hide-element");
    document.getElementById("step2").classList.remove("completed")
    document.getElementById("step3").classList.remove("completed")
    document.getElementById("step-completed").innerHTML = '3';
    document.getElementById("sign-in").classList.add("hide-element");
}