$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function()
{
    // console.log("plus clicked")
    var id=$(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    // console.log(id)
    $.ajax(
        {
            type:"GET",
            url:"/pluscart",
            data:{
                prod_id:id
            },
            success:function(data)
            {
                // console.log(data)
                // console.log("success")
                eml.innerText = data.quantity;
                document.getElementById("amount").innerText = data.amount.toFixed(2);
                document.getElementById("total").innerText = data.total;
            }
        })
})


$('.minus-cart').click(function()
{
    // console.log("plus clicked")
    var id=$(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    // console.log(id)
    $.ajax(
        {
            type:"GET",
            url:"/minuscart",
            data:{
                prod_id:id
            },
            success:function(data)
            {
                // console.log(data)
                // console.log("success")
                eml.innerText = data.quantity;

                document.getElementById("amount").innerText = data.amount;

                document.getElementById("total").innerText = data.total;
            }
        })
})


$('.remove').click(function()
{
    // console.log("plus clicked")
    var id=$(this).attr("pid").toString();
    var eml = this
    console.log(id)
    $.ajax(
        {
            type:"GET",
            url:"/removeitem",
            data:{
                prod_id:id
            },
            success:function(data)
            {
                document.getElementById("amount").innerText = data.amount;
                document.getElementById("total").innerText = data.total;
                // document.getElementById("remove").innerText = data.msg;

                eml.parentNode.parentNode.parentNode.parentNode.remove()

               
            }
        })
})