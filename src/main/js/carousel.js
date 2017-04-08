class BudsCarousel {
    // constructor(element) {
    //     this.element = element
    // }

    static carousel(element) {
        $(element).slick({
            arrows: false,
            centerMode: true,
            // centerPadding: '60px',
            // slidesToShow: 3,
            slidesToScroll: 1,
            autoplay: true,
            autoplayspeed: 5000,
            dots: true,
            // responsive: [
            //     {
            //         breakpoint: 1024,
            //         settings: {
            //             slidesToShow: 3,
            //             slidesToScroll: 1,
            //             infinite: true,
            //         }
            //     },
            //     {
            //         breakpoint: 600,
            //         settings: {
            //             slidesToShow: 2,
            //             slidesToScroll: 1,
            //             arrows: false
            //         }
            //     },
            //     {
            //         breakpoint: 480,
            //         settings: {
            //             slidesToShow: 1,
            //             slidesToScroll: 1,
            //             arrows: false
            //         }
            //     }
            // ]
        });
    }

}

export default BudsCarousel;