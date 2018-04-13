/**
 * page.viewportSize 用来设置浏览器窗口大小
 * page.clipRect 设置截图尺寸
 */


var url = 'http://dreamgqk.cn/';
var page = require('webpage').create();
page.viewportSize = {width: 1024, height: 768};
page.clipRect = {top: 0, left: 0, width: 1024, height: 768};
page.open(url, function (status) {
    console.log('Status: ' + status);
    if (status === 'success') {
        page.render('akagb.png');    
    }
    phantom.exit();
});