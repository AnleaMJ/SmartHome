from flask import Flask, jsonify
import numpy as np
import tensorflow as tf
from openvino.inference_engine import IECore

app = Flask(__name__)

# Example data
energy_data = [10, 12, 11, 14, 9, 12]  # Example energy consumption data in kWh

@app.route('/api/energy-consumption')
def energy_consumption():
    return jsonify({'consumption': sum(energy_data)})

@app.route('/api/recommendations')
def recommendations():
    avg_consumption = np.mean(energy_data)
    if avg_consumption > 10:
        recommendation = "Reduce usage during peak hours."
    else:
        recommendation = "Energy consumption is optimal."
    return jsonify({'recommendations': recommendation})

@app.route('/api/predicted-usage')
def predicted_usage():
    # Example predictive model using Intel Optimized TensorFlow and OpenVINO
    model = tf.keras.models.load_model('energy_model.h5')
    ie = IECore()
    net = ie.read_network(model=model)
    exec_net = ie.load_network(network=net, device_name='CPU')
    
    # Predict future usage (dummy example)
    future_usage = exec_net.infer(inputs={'input': np.array([energy_data])})
    return jsonify({'usage': future_usage[0]})

if __name__ == '__main__':
    app.run(debug=True)
