/**
 * 利用 evaluate 方法我们可以获取网页的源代码。
 * 这个执行是“沙盒式”的，它不会去执行网页外的 JavaScript 代码。
 * evalute 方法可以返回一个对象，然而返回值仅限于对象，不能包含函数（或闭包）
 */

var url = 'https://www.zhihu.com/signup?next=%2F';
var page = require('webpage').create();
page.onConsoleMessage = function (msg) {
    console.log(msg);
};
page.open(url, function (status) {
    var title = page.evaluate(function () {
        return document.title;
    });
    console.log('Page title is ' + title);
    phantom.exit();
});
