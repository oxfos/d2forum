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
    $('body').on('click', 'button[name="submit-reply"]', submitReply);


// EVENT HANDLERS:

    // consider rewriting this function with .load()
    function submitReply(event){
        event.preventDefault();
        let form = $(this).closest('form');
        let element = this;
        $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: form.serialize(),
            success: function(response){
                $(element).closest('div#post').find('#my_reply').html(response);
            }
        });
    };

});