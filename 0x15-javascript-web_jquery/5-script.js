$('DIV#add_item').on('click', function () {
  const parentEL = $('UL.my_list');
  parentEL.append('<li>Item</li>');
});
