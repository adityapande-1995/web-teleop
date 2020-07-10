#!python
from __future__ import print_function
from flask import Flask, render_template, request
import rospy, json
from geometry_msgs.msg import Twist
from threading import Thread

btn_state = {"side": "none" , "front":"none"}
rospy.init_node('gui_teleop', anonymous=True)
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10) # 10hz

def Node():
    #global btn_state, pub, rate
    while True:
        pub.publish( gen_msg(btn_state) )
        rate.sleep()

def gen_msg(state):
    t = Twist()
    if state["side"] == "R" : t.angular.z = 0.1
    if state["side"] == "L" : t.angular.z = -0.1

    if state["front"] == "U" : t.linear.x = 0.1
    if state["front"] == "D" : t.linear.x = -0.1

    return t

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Wont need to hard refresh browser

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/status_update', methods=['POST'])
def update_status():
    global btn_state
    if request.method == 'POST':
        s = json.loads(request.data)
        btn_state["side"] = s["side"] ; btn_state["front"] = s["front"]
        print("Received: ", btn_state)
        return "update done"

if __name__ == '__main__':
    t1 = Thread(target=Node) ; t1.start()
    app.run(debug=True, host='0.0.0.0')
    #t2 = Thread(target=app.run ,args=dict(host='10.0.0.253')) ; t2.start() 
    t1.join() ;
    #t2.join()
    
