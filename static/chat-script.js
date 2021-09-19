const userName = JSON.parse(document.getElementById('name').textContent);
console.log('Hello '+userName);
const chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/chat/'
        );
chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            document.getElementById("content-area").innerHTML+=
                "<div class=\"message\">\n" +
                "<div class=\"message-info\">" + data.name + " " + data.time +"</div>\n" +
                "<div class=\"message-content\">"+ data.message +"</div>\n" +
                "</div>";
            console.log()
            //document.querySelector('#chat-log').value += (data.message + '\n');
            // описать добавление сообщения
    //                  <div class="message">
    //                     <div class="message-info">{{ message.info }}</div>
    //                     <div class="message-content">{{ message.content }}</div>
    //                 </div>
            console.log("got some data: " + data.message);
        };

chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };

function  button_pressed(e) {
    console.log("You pressed some shit with code "+ e.code);
    if (e.code === 'Enter') {  // enter, return
        console.log("You pressed enter");
        document.getElementById('send-form-button').click();
    }
};

function send_message(e) {
    const content = document.getElementById('message-field').value;
    console.log('Just sended your shit, dude! '+content);
    chatSocket.send(JSON.stringify({
        'message': content,
        'name': userName
    }));
    document.getElementById('message-field').value='';

}
