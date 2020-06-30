
$(document).ready(function() {
    var API_URL = "https://o3uuqjbs00.execute-api.us-east-2.amazonaws.com/prod/getdata"
        $.ajax({
            type: 'GET',
            url: API_URL,

            success: function(data) {
                console.log(data)
            }
        })
    })
