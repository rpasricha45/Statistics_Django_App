// test to see if it is connected
// alert("this is connnected")

// get the button id



var button = document.querySelector('#button')

// onclick listner

button.addEventListener("click", function() {
  // this redirects url using current url + new Url extension


  var BASE_URL = window.location.href ;
  concole.log(BASE_URL)
   var newUrlExtension = "/grapher";

  // Redirect
  window.location.replace(BASE_URL+newUrlExtension);


})
