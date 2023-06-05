$(function() {

    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, status) {
        parentList = $('UL#list_movies');
        for (let i = 0; i < data.count; i++) {
            console.log(data.results[i].title);
            let item = $("<li></li>").text(data.results[i].title);
            parentList.append(item);
        }
        //$('DIV#character').text(data.name);
    });
});