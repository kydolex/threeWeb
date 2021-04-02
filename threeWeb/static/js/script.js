window.onload = function() {
    $(function(){
        // MENUボタンがクリックされたときの処理
        $('#menu_btn').on('click', function(){
        if($(this).hasClass('active')) {
            $(this).removeClass('active');
            $(this).html('<i class="fas fa-bars my-gray"></i>');
            $('#menu').removeClass('open');
            $('.menu-background').removeClass('open');
        } else {
            $(this).addClass('active');
            $(this).html('<i class="fas fa-times my-gray"></i>');
            $('#menu').addClass('open');
            $('.menu-background').addClass('open');
        }
        });
    })
    $(function(){ 
        // メニューの背景がクリックされたときの処理
        $('.menu-background').on('click', function(){
        if($(this).hasClass('open')) {
            $(this).removeClass('open');
            $('#menu_btn').removeClass('active').html('<i class="fas fa-bars my-gray"></i>');
            $('#menu').removeClass('open');
        }
        });
    })

}