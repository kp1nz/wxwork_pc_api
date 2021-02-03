#-*- coding: utf-8 -*-

import wxwork
import json
import time
from wxwork import WxWorkManager,MessageType

wxwork_manager = WxWorkManager(libs_path='../../libs')

# 这里测试函数回调d
@wxwork.CONNECT_CALLBACK(in_class=False)
def on_connect(client_id):
    print('[on_connect] client_id: {0}'.format(client_id))

@wxwork.RECV_CALLBACK(in_class=False)
def on_recv(client_id, message_type, message_data):
    print('[on_recv] client_id: {0}, message_type: {1}, message:{2}'.format(client_id, 
    message_type, json.dumps(message_data)))

@wxwork.CLOSE_CALLBACK(in_class=False)
def on_close(client_id):
    print('[on_close] client_id: {0}'.format(client_id))


class EchoBot(wxwork.CallbackHandler):


    @wxwork.RECV_CALLBACK(in_class=True)
    def on_message(self, client_id, message_type, message_data):
        if message_type == MessageType.MT_RECV_TEXT_MSG:
            # reply_content = u'recv msg: {0} ,from '.format(message_data['content'])
            reply_content = "recv msg: "+message_data['content']+"|from: "+message_data['sender_name']
            print(client_id,"|", message_data['conversation_id'],"|", reply_content)
            # wxwork_manager.send_text(client_id, message_data['conversation_id'], reply_content) --R:10696051378022563
            wxwork_manager.send_text(client_id, 'R:10696051378022567', reply_content)

    @wxwork.RECV_CALLBACK(in_class=True)
    def on_image(self, client_id, message_type, message_data):
        if message_type == MessageType.MT_RECV_IMG_MSG:
            print(client_id,"|", message_data['conversation_id'],"|", message_data['file_path'])
            wxwork_manager.send_image(client_id, 'R:10696051378022567', message_data['file_path'])



if __name__ == "__main__":
    echoBot = EchoBot()

    # 添加回调实例对象
    wxwork_manager.add_callback_handler(echoBot)
    wxwork_manager.manager_wxwork(smart=True)

    # 阻塞主线程
    while True:
        time.sleep(0.5)

    # wxwork_manager.on_close
