const close_icon = document.querySelector('.menu>.close')
const menu = document.querySelector('.menu')
const burder_menu = document.querySelector('.burger_menu')


burder_menu.addEventListener('click', () => {

    burder_menu.classList.add('none')
    menu.classList.remove('none')
})

close_icon.addEventListener('click', () => {

    burder_menu.classList.remove('none')
    menu.classList.add('none')
})


const password_img = document.querySelector('.section>.fon+form>label>.password')
const password_input = document.querySelector('.section>.fon+form>label>input.password')


if (password_img) {
    password_img.addEventListener('click', () => {

        if (password_input.type == 'password') {

            password_input.type = 'text'

        } else {
            password_input.type = 'password'
        }
    })

}



const messag_tim = document.querySelector('.messag')


setTimeout(() => {
    messag_tim.classList.toggle('messag_none')
    setTimeout(() => {
        messag_tim.classList.toggle('messag')
    }, 1000)
}, 5000)


const header_user = document.querySelector('.select_user>h2')
const header_user_img = document.querySelector('.select_user>h2>img')
const ul_user = document.querySelector('.select_user>h2+ul')


if (header_user) {

    header_user.addEventListener('click', () => {

        ul_user.classList.toggle('none')

        if (header_user_img.className == 'select-top') {
            header_user_img.classList.add('select-bottom')
            header_user_img.classList.remove('select-top')
        }else {
            header_user_img.classList.remove('select-bottom')
            header_user_img.classList.add('select-top')
        }
    })
}