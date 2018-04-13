/**
 * 导入额外的库（如jQuery）
 */

var page = require('webpage').create();
page.open('https://www.baidu.com/', function () {
    page.includeJs('http://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js', function() {
        page.evaluate(function () {
            $('#su').click();
        });
    });
    phantom.exit();
})