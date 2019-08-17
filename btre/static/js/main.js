const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

// Time out for error message
setTimeout(function() {
  // jQuery
  $("#message").fadeOut("slow");
}, 3000);
