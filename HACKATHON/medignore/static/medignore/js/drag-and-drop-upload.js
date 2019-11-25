$(function () {

  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    done: function (e, data) {
      if (data.result.is_valid) {
        $("#gallery tbody").prepend(
          "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
        )
        $("#photo").prepend(
          "<img src='"+ data.result.url +"'><br><h4>추출된 약품 보험코드 : "+data.result.medList+"<h4><hr>"
        )
      }
    }
  });

});
