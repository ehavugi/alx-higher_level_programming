$('document').ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    $.get('https://fourtonfish.com/hellosalut/', {
      lang: $('INPUT#language_code').val()
    }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
