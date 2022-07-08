
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
