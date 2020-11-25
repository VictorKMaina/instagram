$(document).ready(function () {
    // Auth interactivity
    let labels = $("form label");
    labels.hide()
    for (let i = 0; i < labels.length; i++) {
        let id = $(labels[i]).attr("for");
        let label = $("[for='" + id + "']")
        let input = $("#" + id);
        console.log(label)

        $(input).on("input", function () {
            if (input.val().length == 0) {
                label.hide();
            } else {
                label.show();
            }
        });
    }

    // Index functions
    

});