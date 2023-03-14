$(function (){
        /* receive reviews input */
        bindBtnAddEvent();
        /* send Trip_id to order page */
        bindBtnSendEvent();
        /* delete review  */
        // bindBtnDeleteEvent();
    })
    function bindBtnAddEvent(){
        $("#btnAdd").click(function(){
            var date = new Date();
            var year = date.getFullYear();
            var month = date.getMonth()+1;
            var day = date.getDay()+19;
            var hour = date.getHours();
            var minute = date.getMinutes();
            if (month < 10) {
                month = "0" + month;
            }
            if (day < 10) {
                day = "0" + day;
            }
            if (hour < 10) {
                hour = "0" + hour;
            }
            if (minute < 10) {
                minute = "0" + minute;
            }
            var time = year + "-" + month + "-" +day + " " + hour + ":" +minute;
            var formData = {
                rating: $("#rating").val(),
                content: $("#content").val(),
                time: time,
            }
            $.ajax({
                url:'/review/add/',
                type:'post',
                data:formData,
                success: function (res){
                    // location.reload();
                    console.log(res);
                }
            })
            /* empty user input */
            document.getElementById('rating').value=''
            document.getElementById('content').value=''
        })
    }
    function bindBtnSendEvent(){
        $("#btnSend").click(function(){
            //pass Trip_id to order page
            var trip_id = $("#trip_id").val();
            $.ajax({
               /* url of order page */
               url:'/review/send',
               type:'post',
               data: trip_id,
               success: function (res){
                    console.log(res);
                  }
            })
        })
    }
    // function bindBtnDeleteEvent(){
    //     $("#btnDelete").click(function(){
    //     })
    // }