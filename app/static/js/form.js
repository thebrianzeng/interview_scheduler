(function(window) {

    function _getAvailabilities() {
        var availabilities = [];
        $('.highlighted').each(function() {
            var dayAndTimeSlot = $(this).data('day') + ':' + $(this).data('time-slot');
            availabilities.push(dayAndTimeSlot);
        });

        return availabilities;
    }

    function setupSubmit(postUrl) {

        $('#submit-availabilities-button').click(function() {
            var availabilities = _getAvailabilities();
            var name = $('#name').val();

            var nameAndAvailabilities = {
                name: name,
                availabilities: availabilities
            };

            var nameAndAvailabilitiesJSON = JSON.stringify(nameAndAvailabilities);

            $.ajax({
                type: "POST",
                contentType: "application/json; charset=utf-8",
                url: postUrl,
                data: nameAndAvailabilitiesJSON,
                success: function (data) {
                    // TODO: this does not work yet
                    console.log('success');
                },
                dataType: "json"
            });
        });
    }

    window.setupSubmit = setupSubmit;

})(window);
