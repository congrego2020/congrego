
$(document).ready(function() {
    var API_URL = "https://o3uuqjbs00.execute-api.us-east-2.amazonaws.com/prod/getdata"
    var returnedObject = {}
    var indeedArray = []
    var simplyHiredArray = []
        $.ajax({
            type: 'GET',
            url: API_URL,

            success: function(data) {
                returnedObject = data
                returnedObject.body['Items'].forEach(function(item) {
                    if (item.WEBSITE === "simplyhired.com") {
                        var tag = document.createElement("tr");
                        var table = document.getElementsByClassName('table100-body')
                        var td1 = document.createElement("td");
                        document.getElementById('ohBaby').firstChild.data
                        td1.className ="cell100 column1";
                        tag.appendChild(td1);
                        table[0].children[0].appendChild(tag)
                        console.log(item)
                        simplyHiredArray.push(item)
                    } else {
                        indeedArray.push(item)
                    }

                })
            }
        })
})
