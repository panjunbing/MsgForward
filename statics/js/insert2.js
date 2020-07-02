var SMSRB = global('SMSRB');
data = { msg: SMSRB,
         role: 1,
         key: fFk^fkU$2521Fk3&f223YhGHh
};

$.ajax({
    url:"http://101.201.238.141:28080/insert_msg/",
    async: false,
    data: data,
    type: 'post',
    success:function (data) {
        flash(data)
    }
});