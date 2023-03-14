$(function (){
        /* receive reviews input */
        bindBtnAddEvent();
        /* send Trip_id to order page */
        bindBtnSendEvent();
        /*  receive details from homepage  */
        bindDetailEvent();
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
                user_id: $("#user_id").val(),
                trip_id: $("#trip_id").val(),
            }
            // no blank review
            if(!content.value){
                alert('Please leave your review!');
            }
            $.ajax({
                url:'/review/add/',
                type:'post',
                data:formData,
                success: function (res){
                    /* refresh the page */
                    window.location.reload();
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
            var formData = {
                tirp_id : $("#trip_id").val(),
            }
            $.ajax({
               /* url of order page */
               url:'/review/send',
               type:'post',
               data: formData,
               success: function (res){
                    console.log(res);
                  }
            })
        })
    }
    function bindDetailEvent(){
        //get URL
        var params = new URLSearchParams(window.location.search);
        var trip_id = params.get('tripid');
        $("#trip_id").val(trip_id);
        var formData = {
                tirp_id : $("#trip_id").val(),
            }

        $.ajax({
            /* url of home page */
            url: "/home/",
            type: "GET",
            data: formData,
            success: function(data) {
                processData(data);
            }
        });
        function processData(data){
            //other details
            var name = data['trip_name']
            $("#trip_name").val(name);
            var detail = data['trip_detail']
            $("#trip_detail").val(detail);
            var price = data['trip_price']
            $("#trip_price").val(price);
            //show several pictures
            //need to be modified
            var pic = data['trip_pic']
            $('#trip_pic1').attr('src', pic[0])
            $('#trip_pic2').attr('src', pic[1])
            $('#trip_pic3').attr('src', pic[2])
        }


    }