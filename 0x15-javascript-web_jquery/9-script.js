$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json'
})
  .done(function (json) {
    $('#hello').text(json.hello).appendTo('div');
  });
