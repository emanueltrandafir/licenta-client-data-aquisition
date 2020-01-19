
import time
import stomp


class MyListener(stomp.ConnectionListener):
    def on_message(self, headers, message):
        print('MyListener:\nreceived a message "{}"\n'.format(message))
        global read_messages
        read_messages.append({'id': headers['message-id'], 'subscription':headers['subscription']})


class MyStatsListener(stomp.StatsListener):
    def on_disconnected(self):
        super(MyStatsListener, self).on_disconnected()
        print('MyStatsListener:\n{}\n'.format(self))


read_messages = []
hosts = [('localhost', 8090)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('my_listener', MyListener())
conn.set_listener('stats_listener', MyStatsListener())
# conn.start()

conn.connect(wait=True)


conn.subscribe(destination='/updates', id=1, ack='client-individual')
conn.send(body="A Test message", destination='/updates')
time.sleep(3)