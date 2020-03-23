//-----------------------------------<Side NAV>----------------------------------------------------
$(document).ready(function() {
  $("#sidebar").mCustomScrollbar({
    theme: "minimal"
  });

  $("#dismiss, .overlay").on("click", function() {
    $("#sidebar").removeClass("active");
    $(".overlay").removeClass("active");
  });

  $("#sidebarCollapse").on("click", function() {
    $("#sidebar").addClass("active");
    $(".overlay").addClass("active");
    $(".collapse.in").toggleClass("in");
    $("a[aria-expanded=true]").attr("aria-expanded", "false");
  });
});
//--------------------------------------------<Side Nav End>------------------------------------

$(document).on("submit", "#post-form", function(e) {
  e.preventDefault();
  $.ajax({
    type: "POST",
    url: "/atlus",
    data: {
      title: "vipul",
      info: $("#info").val(),
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      action: "post"
    },
    success: function(json) {
      document.getElementById("post-form").reset();
      $(".posts").prepend(
        '<div class="col-md-6">' +
          '<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">' +
          '<div class="col p-4 d-flex flex-column position-static">' +
          '<h3 class="mb-0">' +
          json.title +
          "</h3>" +
          '<p class="mb-auto">' +
          json.info +
          "</p>" +
          "</div>" +
          "</div>" +
          "</div>"
      );
    },
    error: function(xhr, errmsg, err) {
      $("#results").html(
        "<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " +
          errmsg +
          " <a href='#' class='close'>&times;</a></div>"
      ); // add the error to the dom
      console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
  });
});
//----------------------------------------------<File Upload>-------------------------------
var loadFile = function(event) {
  var output = document.getElementById("output");
  output.src = URL.createObjectURL(event.target.files[0]);
};

$(".custom-file-input").on("change", function() {
  var fileName = $(this)
    .val()
    .split("\\")
    .pop();
  $(this)
    .siblings(".custom-file-label")
    .addClass("selected")
    .html(fileName);
});
