"use strict";

/**
 * Dismiss system messages alert
 * set to 20 seconds
 */
setTimeout(function () {
  let messages = document.getElementById('msg');
  let alert = new bootstrap.Alert(messages);
  alert.close();
}, 20000);
