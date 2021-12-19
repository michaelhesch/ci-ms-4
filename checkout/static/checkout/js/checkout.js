/*
    Core logic/payment flow for this comes from:
    https://stripe.com/docs/payments/accept-a-payment/
    CSS comes from here:
    https://stripe.com/docs/stripe-js/
*/
/*jshint esversion: 6 */

var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
  base: {
    color: "#000",
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};
var card = elements.create("card", { style: style });
card.mount("#card-element");

// Handle validation errors from the card element in real time
card.addEventListener("change", function (event) {
  var errorDiv = document.getElementById("card-errors");
  if (event.error) {
    var html = `
      <span class="icon" role="alert">
        <i class="fas fa-times"></i>
      </span>
      <span>${event.error.message}</span>
    `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = "";
  }
});

// Handle form submission
var form = document.getElementById('checkout-form');
var orderNumber = $('input[name="order_num"]').val();

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    var saveDefaults = Boolean($('#id-save-defaults').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
      'csrfmiddlewaretoken': csrfToken,
      'client_secret': clientSecret,
      'save_defaults': saveDefaults,
      'order_num': orderNumber,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
      // Execute Stripe function if 200 server response returned
      stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
              name: $.trim(form.full_name.value),
              phone: $.trim(form.phone.value),
              email: $.trim(form.email.value),
              address: {
                line1: $.trim(form.address1.value),
                line2: $.trim(form.address2.value),
                city: $.trim(form.city.value),
                state: $.trim(form.state.value),
                country: $.trim(form.country.value),
              }
            }
        },
        shipping: {
          name: $.trim(form.full_name.value),
          phone: $.trim(form.phone.value),
          address: {
            line1: $.trim(form.address1.value),
            line2: $.trim(form.address2.value),
            city: $.trim(form.city.value),
            state: $.trim(form.state.value),
            postal_code: $.trim(form.zipcode.value)
          }
        },
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
  }).fail(function() {
    // If 200 response not returned, reload page to display Django error message
    location.reload();
  });
});