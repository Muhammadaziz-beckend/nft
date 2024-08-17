const nft_cart = document.querySelector('.nft_cart')
const nft_blok = document.querySelectorAll('.nft_cart>.container>.blok>.bottom')

nft_cart.style.background = 'rgb(201 78 78 / 0%)'

nft_blok.forEach((item) => {
    item.style.background = 'rgb(59, 59, 59)'
})


// background: rgb(59, 59, 59);