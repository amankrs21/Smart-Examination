$('.sidebar-btn').click(function () {
    $('.sidebar').toggleClass("show");
    $('.container-body').toggleClass("show")
});

$('.dept-btn').click(function () {
    $('nav ul .dept-show').toggleClass("show");
    $('nav ul .first').toggleClass("rotate");
});
$('.subj-btn').click(function () {
    $('nav ul .subj-show').toggleClass("show2");
    $('nav ul .third').toggleClass("rotate");
});
$('.exam-btn').click(function () {
    $('nav ul .exam-show').toggleClass("show3");
    $('nav ul .fourth').toggleClass("rotate");
});
$('.ques-btn').click(function () {
    $('nav ul .ques-show').toggleClass("show4");
    $('nav ul .fifth').toggleClass("rotate");
});
$('.result-btn').click(function () {
    $('nav ul .result-show').toggleClass("show5");
    $('nav ul .sixth').toggleClass("rotate");
});
$('.user-btn').click(function () {
    $('nav ul .user-show').toggleClass("show6");
    $('nav ul .seventh').toggleClass("rotate");
});
$('nav ul li').click(function () {
    $(this).addClass("active").siblings().removeClass("active");
});

function startTime() {
    const today = new Date();
    let d = today.getDate();
    let mo = today.getMonth();
    let y = today.getFullYear()
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('datetime').innerHTML = h + ":" + m + ":" + s + " & " + d + "/" + mo + "/" + y;
    setTimeout(startTime, 1000);
}

function checkTime(i) {
    if (i < 10) { i = "0" + i };  // add zero in front of numbers < 10
    return i;
}