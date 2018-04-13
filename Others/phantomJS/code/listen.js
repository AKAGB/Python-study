/**
 * 网络监听
 * onResourceRequested 监听请求报文
 * onResoutceReceived 监听响应报文
 */

var url = 'http://dreamgqk.cn/';
var page = require('webpage').create();
page.onResourceRequested = function (request) {
    console.log('Request ' + JSON.stringify(request, undefined, 4));
};
page.onResourceReceived = function (response) {
    console.log('Receive ' + JSON.stringify(response, undefined, 4));
};
page.open(url);