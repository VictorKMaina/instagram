$(document).ready(function(){
    let username = $('input#id_username')
    let username_label = $('[for="id_username"]')
    $(username).on("input", function(){
        if (username.val().length == 0) {
            username_label.hide()
        } else {
            username_label.show()
        }
    })
    
    let password = $('input#id_password')
    let password_label = $('[for="id_password"]')
    $(password).on("input", function(){
        if (password.val().length == 0) {
            password_label.hide()
        } else {
            password_label.show()
        }
    })
})