$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();

    // event listener to trigger ajax call to cancel an order
    $(".cancel").on("click", function() {
        let clicked = $(this);
        let orderid = $(this).attr('data-orderid');
        $.ajax({type: "GET", 
        url: "{% url 'order:cancelorder' %}", 
        data: "order_id=" + orderid, 
        success: function(message) { 
            clicked.closest("tr").find('td').eq(4).text(message).attr('class', 'text-danger');
            clicked.hide();
        } 
});
});
});