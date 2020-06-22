var SMSRB = global('SMSRB');
data = { msg: SMSRB,
         role: 1,
};

$.ajax({
    url:"http://192.168.1.104:8000/insert_msg/",
    async: false,
    data: data,
    type: 'post',
    success:function (data) {
        flash(data)
    }
});