// [1] Helped me with having half stars for fractional ratings over 0.5
$( document ).ready(function() {
    $('.star-rating').each(function (event) {
        let rating = parseFloat($(this).attr('rating'));
        var decimal = Math.floor(rating)
        var fraction = rating%1
        rating = parseFloat(rating)
        if(rating % 1 > 0){
            if (fraction >= 0.5){
                $(this).find('i.fa-star').eq(decimal).removeClass('far');
                $(this).find('i.fa-star').eq(decimal).addClass('fas');
                $(this).find('i.fa-star').eq(decimal).addClass('fa-star-half-alt');
                $(this).find('i.fa-star').eq(decimal).css("color", "gold");
                $(this).find('i.fa-star').eq(decimal).removeClass('fa-star');
                
            }
        }
    });
});
