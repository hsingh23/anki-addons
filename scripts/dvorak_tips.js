



$(document).ready(function(){

    $('#pinky').qtip({
        content: {
            text:'The semicolon “;” work as well, like this, \
it should work for the programmer dvorak variant as well.',
        },
        style: {
            classes: 'ui-tooltip-rounded ui-tooltip-shadow',
        },
        show: {
	    solo: true
	}
    });

});
