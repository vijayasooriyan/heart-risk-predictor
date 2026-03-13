# Heart Disease Risk Predictor

A professional web application that uses machine learning to predict heart disease risk based on patient health data.

## Features

- **Modern UI** - Beautiful, responsive interface with Bootstrap 5
- **Patient Assessment Form** - Comprehensive form to collect health metrics
- **AI-Powered Predictions** - Uses machine learning models for accurate risk assessment
- **Risk Visualization** - Interactive risk level indicator with color-coded categories
- **Personalized Recommendations** - Tailored health recommendations based on risk level
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- **Accessibility** - WCAG 2.1 AA compliant with screen reader support, keyboard navigation, dark mode
- **HCI-Optimized** - Implements 18+ human-computer interaction principles for superior UX


## Project Structure

```
webApp/
├── n.py                              # Flask application (main server)
├── requirements.txt                  # Python dependencies
├── README.md                         # This file
│
├── templates/                        # HTML templates
│   ├── index.html                    # Landing/home page
│   ├── patient_details.html          # Patient assessment form
│   └── patient_results.html          # Results and recommendations
│
├── static/                           # Static files (CSS, JS)
│   └── style.css                     # Global styles
│
└── [Model Files]
    ├── 1heart_risk_regression.sav    # Main prediction model
    ├── 1model_poly.sav               # Polynomial features transformer
    ├── 1model_qntl_data.sav          # Quantile data transformer
    └── 1model_qntl_target.sav        # Quantile target transformer
```

## Installation

### 1. Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install flask numpy joblib
```

## Running the Application

1. Navigate to the project directory:

2. Run the Flask application:
```bash
python n.py
```

3. Open your browser and visit:
```
http://127.0.0.1:5000
```

## Pages Overview

### 1. **Landing Page** (`/`)
- Welcome screen with project information
- Key features highlighted
- "Start Assessment" button to begin

### 2. **Patient Assessment Form** (`/patient`)
- Collects patient health information:
  - Personal Information (Name, Gender, Age)
  - Blood Cholesterol Levels (TC, HDL)
  - Blood Pressure Metrics (SBP, Medication)
  - Lifestyle Factors (Smoking, Diabetes Status)
- Real-time form validation
- User-friendly interface with icons and guides

### 3. **Results Page** (`/getresults`)
- Displays calculated risk percentage
- Visual risk indicator (Low/Moderate/High)
- Risk interpretation based on assessment
- Personalized health recommendations
- Action buttons for new assessment or home

## Form Fields Explained

| Field | Range | Notes |
|-------|-------|-------|
| Age | 1-120 | Patient age in years |
| TC (Total Cholesterol) | 0-1000 | In mg/dL |
| HDL Cholesterol | 0-500 | In mg/dL (higher is better) |
| SBP (Systolic Blood Pressure) | 0-300 | In mm Hg |
| Gender | Male/Female | Biological sex |
| Smoking | Yes/No | Current or previous smoking status |
| BP Medication | Yes/No | On blood pressure medication |
| Diabetes | Yes/No | Has diabetes condition |

## Risk Categories

- **Low Risk (0-33%)**: Status is good, maintain healthy lifestyle
- **Moderate Risk (33-66%)**: Consider lifestyle changes and medical consultation
- **High Risk (66%+)**: Consult healthcare professional immediately

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Machine Learning**: scikit-learn (via joblib)
- **Data Processing**: NumPy

## API Endpoints

### GET `/`
Returns the landing page

### GET `/patient`
Returns the patient assessment form

### POST `/getresults`
- **Input**: Form data with patient health metrics
- **Output**: HTML page with risk prediction and recommendations
- **Required Fields**: All form fields must be filled


## Features Explained

### Form Validation
- Client-side validation using Bootstrap validation classes
- Real-time input checking for ranges
- Required field validation

### Risk Prediction Pipeline
1. Collect patient health data via form
2. Encode categorical variables (gender, smoking, etc.)
3. Apply quantile transformation to data
4. Apply polynomial feature transformation
5. Run prediction through ML model
6. Inverse transform to get risk percentage
7. Display results with recommendations

### Responsive Design
- Mobile-first approach using Bootstrap grid system
- Animations for smooth user experience
- Touch-friendly interface elements
- Optimized for all screen sizes

## Future Enhancements

- User authentication and history tracking
- Export results as PDF
- Integration with electronic health records
- Multi-language support
- Advanced analytics dashboard
- API for third-party integrations

## License

Created by Vijayasooriyan Kamarajah.

## Support

For issues or questions, refer to the inline code comments and Flask documentation.

---

**Created**: 2026
**Last Updated**: March 13, 2026
