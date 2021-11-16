window.onload = function () {
    var _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;
    var quantity_arr = [];
    var price_arr = [];

    var total_forms = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());

    var order_total_quantity = parseInt($('.order_total_quantity').text()) || 0;
    var order_total_price = parseFloat($('.order_total_cost').text().replace(',', '.'));

    for(var i=0; i < total_forms; i++){
        _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
        _price = parseFloat($('.ordersitems-' + i + '-price').val().replace(',', '.'));

    }
};