$(document).ready(() => {
    console.log('Document is ready');
    // const handleIn = () => {
    //     $('.submit-button').addClass('hover');
    // };
    // const handleOut = () => {
    //     $('.submit-button').removeClass('hover');
    // };
    // $('.submit-button').hover(handleIn, handleOut);

    // console.log($('textarea').val('this is a question'));

    $('.questions-button').on('click', () => {
        console.log('test');

        // const request = new XMLHttpRequest();
        // request.open('GET', '/getTotalQuestions');
        // request.onreadystatechange = () => {
        //     if(request.readyState === 4 && request.status === 200) {
        //         console.log(request.response);
        //         const response = JSON.parse(request.response);
        //         $('.total-questions').text(response.totalQuestions)
        //     } else {
        //         console.log(request.status);
        //     }
        // };
        // request.send();

        $.ajax({
            url: 'getTotalQuestions',
            type: 'GET',
            success: (data, statusCode) => {
                // const response = JSON.parse(data);
                $('.total-questions').text(data.totalQuestions)
            },
            error: (xhr, statusCode, error) => {
                console.log(error);
            },
        });
    });
});