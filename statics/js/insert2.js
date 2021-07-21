addScript("https://zeptojs.com/zepto.min.js");
//var SMSRB = global('SMSRB');
var SMSRB = 'haha'
data = { msg: SMSRB,
    role: 1,
    key: fFk^fkU$2521Fk3&f223YhGHh
};

$.ajax({
    url:"http://106.53.70.169:28080/insert_msg/",
    async: false,
    data: data,
    type: 'post',
    success:function (data) {
        flash(data)
    }
});