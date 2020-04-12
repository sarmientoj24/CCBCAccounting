jQuery(document).on("click", ".openaddTransaction", function () {
    var member_id = jQuery(this).data('id');
    var add_transaction_action_url = jQuery('#add_transaction_form').attr('action');
    jQuery(".member_transaction #member_id").val( member_id );
    jQuery('#add_transaction_form').attr('action', add_transaction_action_url + member_id + '/');
});


jQuery('#firstfruit_year').each(function() {
    var year = (new Date()).getFullYear();
    var current = year;
    year -= 1;
    for (var i = 0; i < 6; i++) {
        if ((year+i) == current)
            jQuery(this).append('<option selected value="' + (year + i) + '">' + (year + i) + '</option>');
        else
            jQuery(this).append('<option value="' + (year + i) + '">' + (year + i) + '</option>');
    }
});

jQuery('.trans-form').on('input', '.trans-compute', function(){
    var totalSum = 0;
    jQuery('.trans-form .trans-compute').each(function(){
        var inputVal = jQuery(this).val();
        if(jQuery.isNumeric(inputVal)){
            totalSum += parseFloat(inputVal);
        }
    });
    jQuery('#total').val(totalSum);
});

jQuery('#addTransaction').on('hidden.bs.modal', function () {
    jQuery(this).find('form').trigger('reset');
})

jQuery('.openaddTransaction').on('click', function () {
    var today = new Date().toISOString().split('T')[0];
    jQuery('#input_date').val(today);

    var today = new Date();
    var today_time = today.getHours()
    if (today_time > 15){
        jQuery('#service').find('option[value="Gospel"]').attr("selected",true);
    }
    else {
        jQuery('#service').find('option[value="Worship"]').attr("selected",true);
    }

})

jQuery('form').submit(function(e) {
    jQuery(':disabled').each(function(e) {
        jQuery(this).removeAttr('disabled');
    })
});

jQuery('#advanced_button').on("click", function () {
    jQuery("#advanced-search-toggle").toggle('slow');
});






