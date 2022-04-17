$(document).ready(function () {
    setInterval(function() {
        let url = '/api/get/'
        let obj = $('.number')
        $.ajax({
            type: "GET",
            url: url,
            dataType: "json",
            success: function(response) {
                obj.text(response['number'])
            },
            error: function(response) {
                console.log(response.responseJSON.errors)
            }
        })
    }, 5000)
})

