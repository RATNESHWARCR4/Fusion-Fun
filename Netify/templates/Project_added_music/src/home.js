function fun(){
    if(document.getElementById("txt").value == "example@gmail.com"){
        window.location.href = "src/section.html";
        alert("Login Successful");
    }
    else{
        alert("Invalid Email address!!");
    }
}
