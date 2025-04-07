from auth_utils import require_api_key

from flask import Flask, jsonify, request
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

ai_engine_app = Flask(__name__)

@ai_engine_app.route('/process_trade', methods=['POST'])
def process_trade():
    try:
        data = request.json
        logger.info(f"Processing trade with data: {data}")
        decision = "buy"
        logger.info(f"Trade decision: {decision}")
        return jsonify({"status": "success", "decision": decision}), 200
    except Exception as e:
        logger.error(f"Error in processing trade: {e}")
        return jsonify({"status": "failure", "error": str(e)}), 500