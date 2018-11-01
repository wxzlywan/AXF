$(function () {
    // 隐藏滚动条
    $('.home').width(innerWidth);
    // 顶部轮播图
     new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        effect: 'cube',
        grabCursor: true,
        cube: {
            shadow: true,
            slideShadows: true,
            shadowOffset: 20,
            shadowScale: 0.94
        },
        autoplay:2500,
        loop:true
    });
        new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        spaceBetween: 10,
        loop:true
    });
});
