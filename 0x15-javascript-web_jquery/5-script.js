$('DIV#add_item').on('click', function() {
    let parentEL = $('UL.my_list');
    parentEL.append('<li>Item</li>');
})