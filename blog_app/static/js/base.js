function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// $('.likebtn').click(function(){
//     let id = $(this).attr('id');
//     $.ajax(
//         {
//             type:"GET",
//             url: '{% url "like" %}',
//             data:{
//                      post_id: id
//             },
//         success: function( data )
//         {
//             // $( '#like'+ id ).removeClass('btn btn-primary btn-lg');
//             // $( '#like'+ id ).addClass('btn btn-success btn-lg');
//             alert(123);
//         }
//     })
// });


// $('.likebtn').click(function(){
//     const csrftoken = getCookie('csrftoken');
//     $.ajax({
//         url:  "like", // /like url
//         type: "POST",
//         data: {
//             'content_id': $(this).attr('id'),
//             'operation':'like_submit',
//             'csrfmiddlewaretoken': csrftoken
//         },
//         dataType: "json",
//         success: function(response) {
//             alert(1123);
//             selector = document.getElementsByName(response.content_id);
//                 if(response.liked==true){
//                   $(selector).css("color","blue");
//                 }
//                 else if(response.liked==false){
//                   $(selector).css("color","black");
//                 }
//           }
//         });
//   })

// $(document).ready(function () {
//     (function () {
//         document.body.addEventListener("click", clickButtons);
//
//         function clickButtons(evt) {
//             const from = evt.target;
//             if (from.id.includes("likebtn")) {
//                 const id = from.id.slice(8);
//                 $.ajax({
//                     type: "POST",
//                     url: "{% url liker id %}",
//                     data: form.serialize(), // serializes the form's elements.
//                     success: function (data) {
//                         alert(123); // show response from the php script.
//                     }
//                 });
//             }
//         }
//     }())
// })