$('document').ready(function() {
    $('INPUT#btn_translate').on('click', function() {
        $.get('https://fourtonfish.com/hellosalut/', {
            lang: $('INPUT#language_code').val()
        }, function(data) {
            $('DIV#hello').text(data.hello)
        });
    });
    $('INPUT#language_code').on('keypress', function(event) {
        var keycode = (event.keyCode ? event.keyCode : event.which);

        if (keycode == '13') {
            $.get('https://fourtonfish.com/hellosalut/', {
                lang: $('INPUT#language_code').val()
            }, function(data) {
                $('DIV#hello').text(data.hello)
            })
        }
    });
})