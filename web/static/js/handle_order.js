;

var handleOrderForm = function(form) {
    var emailField = document.getElementsByClassName('order-crtl--client-email')[0];
    var email = emailField.value;

    orderHandler.requestForEmail(email);
}


var OrderHandler = function(orderStorage, orderService) {
    return {
        requestForEmail: function(email) {
            var request = {
                'email': email,
                'photos': orderStorage.getAllMedias()
            }

            orderService.requestOrder(request);
        }
    }
}

var OrderService = function(confirmationEndpoint, http) {
    return {
        requestOrder: function(request) {
            http.post(confirmationEndpoint, request)
                .then(function (response) {
                    console.log('success');
                })
            ;
        }
    }
}



