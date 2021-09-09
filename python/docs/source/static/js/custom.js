$(document).ready(function () {
   // external links open in a separate tab
   $('a[href^="http://"], a[href^="https://"]').not('a[class*=internal]').attr('target', '_blank');
});