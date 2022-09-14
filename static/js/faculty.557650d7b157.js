$('.sidebar-btn').click(function() {
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

// function openAddDept() {
//     var w = 480, h = 340;
//     if (document.getElementById) {
//         w = screen.availWidth;
//         h = screen.availHeight;
//     }
//     var popW = 450, popH = 500;
//     var leftPos = (w - popW) / 2;
//     var topPos = (h - popH) / 2;
//     msgWindow = window.open("{% url 'adddepartment' %}", 'popup', 'width=' + popW + ',height=' + popH + ',top=' + topPos + ',left=' + leftPos + ', scrollbars=yes');
// }
// function openAddSubject() {
//     var w = 480, h = 340;
//     if (document.getElementById) {
//         w = screen.availWidth;
//         h = screen.availHeight;
//     }
//     var popW = 450, popH = 550;
//     var leftPos = (w - popW) / 2;
//     var topPos = (h - popH) / 2;
//     msgWindow = window.open("{% url 'addsubject' %}", 'popup', 'width=' + popW + ',height=' + popH + ',top=' + topPos + ',left=' + leftPos + ', scrollbars=yes');
// }
// function openExam() {
//     var w = 480, h = 340;
//     if (document.getElementById) {
//         w = screen.availWidth;
//         h = screen.availHeight;
//     }
//     var popW = 600, popH = 660;
//     var leftPos = (w - popW) / 2;
//     var topPos = (h - popH) / 2;
//     msgWindow = window.open("{% url 'addexam' %}", 'popup', 'width=' + popW + ',height=' + popH + ',top=' + topPos + ',left=' + leftPos + ', scrollbars=yes');
// }
// function openObjective() {
//     var w = 480, h = 340;
//     if (document.getElementById) {
//         w = screen.availWidth;
//         h = screen.availHeight;
//     }
//     var popW = 750, popH = 750;
//     var leftPos = (w - popW) / 2;
//     var topPos = (h - popH) / 2;
//     msgWindow = window.open("{% url 'addobjective' %}", 'popup', 'width=' + popW + ',height=' + popH + ',top=' + topPos + ',left=' + leftPos + ', scrollbars=yes');
// }
// function openSubjective() {
//     var w = 480, h = 340;
//     if (document.getElementById) {
//         w = screen.availWidth;
//         h = screen.availHeight;
//     }
//     var popW = 700, popH = 550;
//     var leftPos = (w - popW) / 2;
//     var topPos = (h - popH) / 2;
//     msgWindow = window.open("{% url 'addsubjective' %}", 'popup', 'width=' + popW + ',height=' + popH + ',top=' + topPos + ',left=' + leftPos + ', scrollbars=yes');
// }
// function openCoding() {
//     var w = 480, h = 340;
//     if (document.getElementById) {
//         w = screen.availWidth;
//         h = screen.availHeight;
//     }
//     var popW = 700, popH = 550;
//     var leftPos = (w - popW) / 2;
//     var topPos = (h - popH) / 2;
//     msgWindow = window.open("{% url 'addcoding' %}", 'popup', 'width=' + popW + ',height=' + popH + ',top=' + topPos + ',left=' + leftPos + ', scrollbars=yes');
// }