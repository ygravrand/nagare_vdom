Gator(document).on('click', '.nagare-callback', function(e) {
    e.preventDefault();
    nagare_getAndEval(this.getAttribute('data-nagare-callback'));
});