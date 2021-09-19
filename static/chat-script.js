const userName = JSON.parse(document.getElementById('name').textContent);
const scrollarea = document.getElementById('content-area');
const chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/chat/'
        );
chatSocket.onmessage = function(e) {
    try {
        var need_scroll = document.getElementsByClassName('scrollarea')[0].scrollTop+document.getElementsByClassName('scrollarea')[0].clientHeight+1 >= document.getElementsByClassName('scrollarea')[0].scrollHeight;
    }catch {
        var need_scroll = false;
    };

    const data = JSON.parse(e.data);
            document.getElementById("content-area").innerHTML+=
                "<div class=\"message\">\n" +
                "<div class=\"message-info\">" + data.name + " " + data.time +"</div>\n" +
                "<div class=\"message-content\">"+ data.message +"</div>\n" +
                "</div>";

    if (need_scroll) document.getElementsByClassName('scrollarea')[0].scrollTop = document.getElementsByClassName('scrollarea')[0].scrollHeight+1;
};

chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };

function  button_pressed(e) {
    if (e.code === 'Enter') {  // enter, return
        document.getElementById('send-form-button').click();
    }
};

function send_message(e) {
    const content = document.getElementById('message-field').value;
    if (content){
        chatSocket.send(JSON.stringify({
            'message': content,
            'name': userName
        }));
    }
    document.getElementById('message-field').value='';
    document.getElementById('message-field').focus();

}
window.onload = function (){
    try {document.getElementsByClassName('scrollarea')[0].scrollTop = document.getElementsByClassName('scrollarea')[0].scrollHeight+1;}
    catch {}
}

