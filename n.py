from flask import Flask, render_template, request, jsonify
from flask import send_file
import joblib
import numpy as np
import os
import logging
from datetime import datetime

# Configure logging for HCI: System Status Visibility
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load models with error handling
try:
    model = joblib.load('1heart_risk_regression.sav')
    model_poly = joblib.load('1model_poly.sav')
    model_qntl_data = joblib.load('1model_qntl_data.sav')
    model_qntl_target = joblib.load('1model_qntl_target.sav')
    logger.info("✓ All models loaded successfully")
except Exception as e:
    logger.error(f"✗ Failed to load models: {str(e)}")
    raise

# Initialize Flask app
app = Flask(__name__)

# Configure app
app.config['STATIC_FOLDER'] = 'static'
app.config['TEMPLATES_FOLDER'] = 'templates'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1MB max request size

# HCI: Input validation ranges (for user feedback)
VALIDATION_RANGES = {
    'age': (18, 120),
    'tc': (0, 1000),
    'hdl': (0, 500),
    'sbp': (0, 300)
}

CATEGORICAL_OPTIONS = {
    'gender': ['male', 'female'],
    'smoke': ['no', 'yes'],
    'bpm': ['no', 'yes'],
    'diab': ['no', 'yes']
}


@app.route('/')
def index():
    """Home page route - HCI: Clear entry point"""
    logger.info("User accessed home page")
    return render_template('index.html')


@app.route('/patient')
def patient():
    """Patient assessment form route - HCI: Visible form"""
    logger.info("User accessed patient form")
    return render_template('patient_details.html')


@app.route('/getresults', methods=['POST'])
def getresults():
    """Process form data and generate risk prediction
    
    HCI Principles Applied:
    - Error Prevention: Input validation
    - Error Recovery: Clear error messages
    - Feedback: Processing status and results
    - Accessibility: Proper error handling
    """
    try:
        logger.info("--- New Assessment Started ---")
        
        # Get form data
        result = request.form

        # Extract and validate form inputs - HCI: Error Prevention
        input_data = {
            'name': str(result.get('name', 'Patient')).strip(),
            'gender': result.get('gender', '').lower(),
            'age': result.get('age', '0'),
            'tc': result.get('tc', '0'),
            'hdl': result.get('hdl', '0'),
            'sbp': result.get('sbp', '0'),
            'smoke': result.get('smoke', '').lower(),
            'bpm': result.get('bpm', '').lower(),
            'diab': result.get('diab', '').lower()
        }

        # Validate categorical inputs - HCI: Input Validation
        for field, value in input_data.items():
            if field in CATEGORICAL_OPTIONS:
                if value not in CATEGORICAL_OPTIONS[field]:
                    logger.warning(f"Invalid {field} value: {value}")
                    return render_template(
                        'patient_details.html',
                        error=f"Invalid {field} selected. Please try again.",
                        error_type='validation'
                    ), 400

        # Convert numeric inputs with validation - HCI: Error Prevention
        try:
            age = float(input_data['age'])
            tc = float(input_data['tc'])
            hdl = float(input_data['hdl'])
            sbp = float(input_data['sbp'])
        except ValueError as e:
            logger.warning(f"Invalid numeric input: {str(e)}")
            return render_template(
                'patient_details.html',
                error="Please enter valid numbers for health metrics.",
                error_type='validation'
            ), 400

        # Validate input ranges - HCI: Feedback & Error Prevention
        validation_errors = []
        if not (VALIDATION_RANGES['age'][0] <= age <= VALIDATION_RANGES['age'][1]):
            validation_errors.append(f"Age must be between {VALIDATION_RANGES['age'][0]} and {VALIDATION_RANGES['age'][1]} years")
        if not (VALIDATION_RANGES['tc'][0] <= tc <= VALIDATION_RANGES['tc'][1]):
            validation_errors.append(f"Total Cholesterol must be between {VALIDATION_RANGES['tc'][0]} and {VALIDATION_RANGES['tc'][1]} mg/dL")
        if not (VALIDATION_RANGES['hdl'][0] <= hdl <= VALIDATION_RANGES['hdl'][1]):
            validation_errors.append(f"HDL Cholesterol must be between {VALIDATION_RANGES['hdl'][0]} and {VALIDATION_RANGES['hdl'][1]} mg/dL")
        if not (VALIDATION_RANGES['sbp'][0] <= sbp <= VALIDATION_RANGES['sbp'][1]):
            validation_errors.append(f"Systolic BP must be between {VALIDATION_RANGES['sbp'][0]} and {VALIDATION_RANGES['sbp'][1]} mm Hg")

        if validation_errors:
            logger.warning(f"Validation failed: {validation_errors}")
            return render_template(
                'patient_details.html',
                error="Validation Error: " + "; ".join(validation_errors),
                error_type='validation'
            ), 400

        # Prepare data for prediction - HCI: System Status (verbose logging)
        logger.info(f"User: {input_data['name']} | Gender: {input_data['gender']} | Age: {age}")
        logger.info(f"Metrics - TC: {tc}, HDL: {hdl}, SBP: {sbp}")
        logger.info(f"Lifestyle - Smoke: {input_data['smoke']}, BP Med: {input_data['bpm']}, Diabetes: {input_data['diab']}")

        # Dictionary mappings for categorical variables
        gender_dict = {'female': 0, 'male': 1}
        smoke_dict = {'no': 0, 'yes': 1}
        bmp_dict = {'no': 0, 'yes': 1}
        diab_dict = {'no': 0, 'yes': 1}

        # Prepare test data: [gender, age, tc, hdl, smoke, bpm, diab]
        test_data = np.array([
            gender_dict[input_data['gender']],
            age,
            tc,
            hdl,
            smoke_dict[input_data['smoke']],
            bmp_dict[input_data['bpm']],
            diab_dict[input_data['diab']]
        ]).reshape(1, -1)

        logger.info("Applying feature transformations...")
        
        # Apply transformations
        test_data = model_qntl_data.transform(test_data)
        test_data = model_poly.transform(test_data)

        logger.info("Running prediction model...")
        
        # Make prediction
        prediction = model.predict(test_data)

        # Inverse transform to get actual risk percentage
        prediction = model_qntl_target.inverse_transform(prediction)

        # Ensure risk is between 0 and 100 - HCI: Data Validation
        risk_value = float(prediction[0][0])
        risk_value = max(0, min(100, risk_value))

        logger.info(f"✓ Prediction successful: {risk_value}%")

        resultDict = {
            "name": input_data['name'],
            "risk": round(risk_value, 2)
        }

        logger.info("--- Assessment Completed Successfully ---")
        return render_template('patient_results.html', results=resultDict)

    except Exception as e:
        # HCI: Error Recovery - Clear error message
        logger.error(f"✗ Error during prediction: {str(e)}", exc_info=True)
        return render_template(
            'patient_details.html',
            error='An unexpected error occurred. Please check your inputs and try again.',
            error_type='server_error'
        ), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint - HCI: System Status"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'models_loaded': True
    }), 200


@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors - HCI: Error Recovery"""
    logger.warning(f"Bad request error: {str(error)}")
    return render_template('patient_details.html', 
                         error='Invalid input. Please check the form and try again.',
                         error_type='client_error'), 400


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors - HCI: Navigation Help"""
    logger.warning(f"Not found error: {request.url}")
    return render_template('index.html'), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors - HCI: Error Recovery"""
    logger.error(f"Server error: {str(error)}", exc_info=True)
    return render_template(
        'patient_details.html',
        error='Server error. Please try again later.',
        error_type='server_error'
    ), 500


@app.after_request
def log_response(response):
    """Log response for HCI: System Status Visibility"""
    if response.status_code != 200:
        logger.info(f"Response: {response.status_code} for {request.method} {request.path}")
    return response


# HCI: Better logging on startup
if __name__ == '__main__':
    logger.info("=" * 50)
    logger.info("Heart Disease Risk Predictor - Starting Application")
    logger.info("=" * 50)
    logger.info(f"Flask Debug Mode: {os.environ.get('FLASK_ENV') == 'development'}")
    logger.info(f"Server: http://0.0.0.0:{os.environ.get('PORT', 5000)}")
    logger.info("=" * 50)
    
    # Run the Flask app - Production ready
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
