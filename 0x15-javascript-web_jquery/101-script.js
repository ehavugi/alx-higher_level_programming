$(document).ready(function() {
    // do something when the document is ready
    $('DIV#add_item').on('click', function() {
        let parentEL = $('UL.my_list');
        parentEL.append('<li>Item</li>');
    })

    $('DIV#remove_item').on('click', function() {
        abandonChild = $('UL.my_list :last-child');
        abandonChild.remove();
    })

    $('DIV#clear_list').on('click', function() {
        let parentEL = $('UL.my_list');
        parentEL.empty();
    })
});