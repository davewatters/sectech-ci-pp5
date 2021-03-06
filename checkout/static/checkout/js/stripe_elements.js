
/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/js/elements_object/create
    CSS from here:
    https://stripe.com/docs/js/appendix/style
    https://stripe.com/docs/elements/appearance-api
    https://stripe.com/docs/js  ??
*/

var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
var clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var elCard = elements.create('card', {
  style: {
    base: {
      iconColor: '#0972c0',
      color: '#000',
      fontFamily: 'Helvetica Neue", Helvetica, sans-serif',
      fontSize: '16px',
      fontSmoothing: 'antialiased',
      ':-webkit-autofill': {
        color: '#fce883',
      },
      '::placeholder': {
        color: '#aab7c4',
      },
    },
    invalid: {
      color: '#dc3545',
      iconColor: '#dc3545',
    },
  },
});

elCard.mount('#card-element');

// Handle realtime validation errors on the card element
elCard.addEventListener('change', function (event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
      var html = `
          <span class="icon" role="alert">
              <i class="fas fa-times"></i>
          </span>
          <span>${event.error.message}</span>
      `;
      $(errorDiv).html(html);
  } else {
      errorDiv.textContent = '';
  }
});


// Handle form submit
// credit: from CI Boutique Ado, with mods
var form = document.getElementById('checkout-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    elCard.update({ 'disabled': true});
    $('#submit-btn').attr('disabled', true);
    $('#checkout-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var cust_ref = $('input[name="cust_ref"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'cust_ref': cust_ref,
    };
    // cache our checkout info so we can access in stripe webhook
    var url = '/checkout/cache_checkout_data/';
    $.post(url, postData).done(function () {
        var cust_name = JSON.parse(document.getElementById('id_cust_name').textContent).slice(1, -1).trim;
        var cust_email = JSON.parse(document.getElementById('id_cust_email').textContent).slice(1, -1).trim;
        var cust_country = JSON.parse(document.getElementById('id_cust_country').textContent).slice(1, -1).trim;
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
              card: elCard,
              billing_details: {
                  name: cust_name,
                  email: cust_email,
                  address:{
                    country: cust_country,
                  }
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
                $('#checkout-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                elCard.update({ 'disabled': false});
                $('#submit-btn').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    });
});
