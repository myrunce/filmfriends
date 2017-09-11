var api = 'http://data.tmsapi.com/v1.1/movies/showings?startDate=2017-07-27&zip=78701&api_key=sszbbjhadk82fc9nh469bs2k'
html = ''
$(document).ready(function(){

    $.get(api, function(data){
        for (var i = 0; i < 5; i++){
                movieInfo = {
                    title: data[i].title
                }
            console.log(movieInfo.title);   
            html += '<div class= "movies">'
            html += '<p>Movie title: ' + movieInfo.title + '</p>'
            html += '</div>' 

            $('#movies').html(html);
        }
    })
})