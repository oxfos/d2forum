$(document).ready(function(){


// CSRF AJAX HEADER

    var csrftoken = Cookies.get('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


// EVENT TRIGGERS:

    $('button[name="reply"]').click(submitReply);

// EVENT HANDLERS:

    function submitReply(event){
        event.preventDefault();
        var reply = $(this).val();
        var data = $(this).closest('form').serialize();
        $.ajax({
            url: $(this).closest('form').attr('action'),
            type: 'POST',
            data: {
                reply: reply
            },
            success: function(data){
                console.log(data)
            }
        });
    };

});