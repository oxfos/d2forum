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


    $('button[name="reply"]').click(displayForm);



// EVENT HANDLERS:

    // consider rewriting this function with .load()
    function displayForm(event){
        event.preventDefault();
        var element = this;
        $.ajax({
            url: $(this).closest('form[id="post_reply"]').attr('action'),
            type: 'GET',
            success: function(data){
                $(element).closest('div').append(data);
            }
        });
    };

});