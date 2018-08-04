// test to see if it is connected
// alert("this is connnected")

// get the button id



var button = document.querySelector('#button')

// onclick listner

button.addEventListener("click", function() {
  // this redirects url using current url + new Url extension
  console.log("I am connected")
  var BASE_URL = window.location.href ;
   var newUrlExtension = "grapher";

  // Redirect
  window.location.replace(BASE_URL+newUrlExtension);

})
