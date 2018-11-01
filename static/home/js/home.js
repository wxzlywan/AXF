$(function () {
    // 隐藏滚动条
    $('.home').width(innerWidth);
    // 顶部轮播图
        new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        autoplay: 2500,
        loop: true,
    });
        new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        spaceBetween: 10,
        loop:true
    });
});
