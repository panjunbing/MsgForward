//定义post方法
function posthttp(url, data) {
    var xhr = new XMLHttpRequest();
    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            flash(this.responseText); //显示返回消息,可删除本行
        }
    });
    xhr.open("POST", url, false);
    xhr.send(data);
    return xhr.responseText;
}

//发送消息(文本)
var SMSRB = global('SMSRB');
var data = JSON.stringify({
    "msg": "haha",
    "role": "1",
});
var send = "http://192.168.1.104:8000/insert_msg/";
posthttp(send, data);