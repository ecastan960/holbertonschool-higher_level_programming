$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
})
  .done(function (json) {
    for (const films of json.results) {
      $('#list_movies').append(`<li>${films.title}</li>`);
    }
  });
