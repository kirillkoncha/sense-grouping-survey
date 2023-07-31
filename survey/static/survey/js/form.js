var current_part = 1;

$(document).ready(function(){
    $('.submit').on('click', function () {
        var $form = $(this).closest('form');
        if ($form.hasClass('start-form')) {
            submit_start_form($form);
        } else if ($form.hasClass('feedback-form')) {
            submit_feedback_form($form);
        } else {
            next_part();
        }
    });
    $('div.link').on('click', function () {
        window.location = $(this).find('a').attr('href');
    });
});

function submit_start_form($form) {
    var inputs = $form.find('.input');
    var error = false;
    inputs.each(function () {
        var val = $(this).val();
        if (val == '') {
            error = true;
            alert('Заполните все поля');
            return false;
        }
    });
    if (error) {
        return;
    }
    var age = $('[name = "age"]').val();
    if (age < 17 || age > 70) {
        alert('В исследовании могут принимать участие лица от 17 до 70 лет');
        return;
    }
    send_ajax($form);
}

function submit_feedback_form($form) {
    var hasMessage = Boolean($form.find('textarea[name=feedback]').val().trim());
    var hasEmail = Boolean($form.find('input[name=email]').val().trim());
    if (!hasMessage && !hasEmail) {
        $('#success-image').hide();
        $('#success-message').text('Спасибо за участие в опросе! Ваш код: 236549 — вы можете скопировать и вставить его в толоку для получения денег.');
    } else if (!hasMessage) {
        $('#success-message').text('Мы получили ваш адрес почты. Спасибо! Ваш код: 236549 — вы можете скопировать и вставить его в толоку для получения денег.');
    }
    send_ajax($form);
}

function send_ajax($form) {
    $.ajax({
        url: './',
        method: 'POST',
        data: $form.serialize(),
        success: function (response) {
            if (response.next) {
                $('#next').attr('href', response.next);
            }
            next_part();
        }
    });

}

function next_part() {
    var $current = $('.part' + current_part);
    var $next = $('.part' + (current_part + 1));
    $current.removeClass('open').addClass('hide');
    $next.addClass('open');
    current_part += 1;
    window.scrollTo(0, 0);
}


