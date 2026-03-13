# Heart Risk Predictor - User Guide

Welcome to the Heart Risk Predictor! This guide will help you navigate and use the application effectively.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Understanding the Pages](#understanding-the-pages)
3. [Filling Out the Assessment](#filling-out-the-assessment)
4. [Understanding Your Results](#understanding-your-results)
5. [Keyboard Shortcuts](#keyboard-shortcuts)
6. [Accessibility Features](#accessibility-features)
7. [Troubleshooting](#troubleshooting)
8. [Important Disclaimers](#important-disclaimers)

---

## Getting Started

### Step 1: Launch the Application
1. Run the Flask application (`python n.py`)
2. Open your web browser to `http://127.0.0.1:5000`
3. You'll see the landing page with project information

### Step 2: Navigate to Assessment
- Click the **"Start Assessment"** button
- Or use the navigation menu to go to the assessment form

---

## Understanding the Pages

### **Page 1: Landing Page (Home)**

This is your welcome page. It shows:
- **What is This Tool**: Overview of heart disease risk assessment
- **Key Features**: Benefits and capabilities demonstrated
- **How It Works**: 4-step process explanation
- **Start Assessment Button**: Entry point to begin your evaluation

**Accessibility Features:**
- Skip main content link for keyboard users
- All text readable with screen readers
- Dark mode automatically supported

---

### **Page 2: Patient Assessment Form**

This is where you provide your health information.

#### **Form Organization:**

The form is organized into 4 sections for easy completion:

1. **📋 Personal Information**
   - Name (for personalization)
   - Gender (Male/Female)
   - Age (in years)

2. **❤️ Blood Cholesterol**
   - Total Cholesterol (TC) in mg/dL
   - HDL Cholesterol in mg/dL

3. **🩸 Blood Pressure & Medication**
   - Systolic Blood Pressure (SBP) in mm Hg
   - Blood Pressure Medication (Yes/No)

4. **🚭 Lifestyle & Medical Conditions**
   - Smoking Status (Never/Former/Current)
   - Diabetes Status (Yes/No)

#### **Form Features:**

- **Progress Indicator**: Shows "Step X of 4" at the top
- **Field Descriptions**: Helpful hints below each field explain normal ranges
- **Real-Time Validation**: Green checkmark when input is correct
- **Error Prevention**: Red highlight with specific message if data is invalid
- **Required Fields**: Marked with red asterisk (*)

---

### **Page 3: Results & Recommendations**

After submitting the form, you'll see your personalized results.

#### **What You'll See:**

1. **Risk Level Display**
   - Your exact risk percentage
   - Color-coded risk category badge
   - Visual risk indicator bar showing your position

2. **Risk Category Interpretation**
   - **Low Risk (0-33%)**: Your risk level is relatively low
   - **Moderate Risk (33-66%)**: Consider lifestyle modifications
   - **High Risk (66%+)**: Consult healthcare provider

3. **Personalized Recommendations**
   - Tailored health tips based on your risk level
   - Specific actions you can take
   - When to seek medical advice

4. **Assessment Details**
   - Your name (for personalization)
   - Date and time of assessment
   - Your health metrics summary

5. **Action Buttons**
   - **Print**: Print or save as PDF for your records
   - **New Assessment**: Perform another risk evaluation
   - **Home**: Return to landing page

---

## Filling Out the Assessment

### **Field-by-Field Guide:**

#### **1. Name**
- **What to enter**: Your full name or initials
- **Example**: "John Smith" or "JS"
- **Purpose**: For personalization in results
- **Required**: Yes

#### **2. Gender**
- **What to select**: Your biological sex
- **Options**: Male / Female
- **Why it matters**: Gender affects heart disease risk profiles
- **Required**: Yes

#### **3. Age**
- **What to enter**: Your age in years
- **Valid Range**: 18 to 120 years
- **Hint**: Must be between 18 and 120
- **Example**: 45, 62, 28
- **Required**: Yes

#### **4. Total Cholesterol (TC)**
- **What to enter**: Your total cholesterol level
- **Unit**: Milligrams per deciliter (mg/dL)
- **Valid Range**: 0 to 1000 mg/dL
- **Hint**: Normal total cholesterol is less than 200 mg/dL
- **Where to find**: From recent blood test results
- **Example**: 195, 240, 180
- **Required**: Yes

#### **5. HDL Cholesterol**
- **What to enter**: Your HDL (good cholesterol) level
- **Unit**: Milligrams per deciliter (mg/dL)
- **Valid Range**: 0 to 500 mg/dL
- **Hint**: Higher HDL is better (normal: 40+ for men, 50+ for women)
- **Where to find**: From recent blood test results
- **Example**: 55, 42, 60
- **Required**: Yes

#### **6. Systolic Blood Pressure (SBP)**
- **What to enter**: Your systolic (top number) blood pressure
- **Unit**: Millimeters of mercury (mm Hg)
- **Valid Range**: 0 to 300 mm Hg
- **Hint**: Normal blood pressure is less than 120 mm Hg
- **Where to find**: From recent blood pressure reading
- **Example**: 120, 140, 100
- **Required**: Yes

#### **7. Blood Pressure Medication**
- **What to select**: Are you currently taking blood pressure medication?
- **Options**: 
  - **No** (not taking medication)
  - **Yes** (taking blood pressure medication)
- **Why it matters**: Indicates hypertension management
- **Required**: Yes

#### **8. Smoking Status**
- **What to select**: Your smoking history
- **Options**:
  - **Never** (never smoked)
  - **Former** (used to smoke, quit)
  - **Current** (actively smoking)
- **Why it matters**: Smoking significantly increases heart disease risk
- **Required**: Yes

#### **9. Diabetes**
- **What to select**: Do you have diabetes?
- **Options**:
  - **No** (no diabetes diagnosis)
  - **Yes** (has diabetes type 1, 2, or gestational)
- **Why it matters**: Diabetes increases heart disease risk
- **Required**: Yes

### **Tips for Accurate Results:**

1. **Use Recent Data**: Get information from blood tests within last year
2. **Check with Your Doctor**: If unsure about your metrics
3. **Be Honest**: Accurate information produces accurate predictions
4. **Take Your Time**: No rush to complete the form
5. **Use Keyboard Navigation**: Tab between fields, Enter to submit

---

## Understanding Your Results

### **The Risk Percentage**

Your risk percentage represents the probability of developing heart disease.

**Example Interpretations:**
- **15% Risk**: 15 out of 100 people with your characteristics might develop heart disease
- **45% Risk**: 45 out of 100 people with your characteristics might develop heart disease
- **75% Risk**: 75 out of 100 people with your characteristics might develop heart disease

### **Risk Categories Explained**

#### **🟢 Low Risk (0-33%)**

**What it means:**
- Your current health metrics indicate lower heart disease risk
- Your lifestyle factors are generally favorable

**What you should do:**
- Maintain current healthy habits
- Continue regular health check-ups
- Stay physically active (150 min/week moderate activity)
- Maintain healthy diet (fruits, vegetables, whole grains)
- Monitor your cholesterol and blood pressure regularly

#### **🟡 Moderate Risk (33-66%)**

**What it means:**
- You have some risk factors for heart disease
- Lifestyle modifications could reduce your risk

**What you should do:**
- Schedule an appointment with your healthcare provider
- Consider making lifestyle changes:
  - Increase physical activity
  - Adopt heart-healthy diet (Mediterranean or DASH diet)
  - Reduce salt and sugar intake
  - Quit smoking if applicable
  - Manage stress through meditation or yoga
- Monitor blood pressure and cholesterol regularly
- Reduce alcohol consumption if applicable

#### **🔴 High Risk (66%+)**

**What it means:**
- You have significant heart disease risk factors
- Medical consultation is strongly recommended

**What you should do:**
- **Schedule an appointment with your healthcare provider immediately**
- Do not delay medical evaluation
- Discuss your results with your doctor
- Follow medical recommendations for:
  - Medication (if prescribed)
  - Lifestyle modifications
  - Regular monitoring and follow-up tests

### **What These Results Are NOT**

- **Not a diagnosis**: This tool does not diagnose heart disease
- **Not medical advice**: Results do not replace professional medical consultation
- **Not a guarantee**: Risk percentage is a statistical estimate, not a certainty
- **Not comprehensive**: Many factors affecting heart disease are not included

### **Important Notes**

⚠️ **Medical Consultation**: Always consult qualified healthcare professionals for proper evaluation and diagnosis.

✅ **Use as Tool**: Use these results as motivation for lifestyle improvements or discussion point with your doctor.

---

## Keyboard Shortcuts

The application supports keyboard shortcuts for efficiency:

| Shortcut | Action |
|----------|--------|
| **Tab** | Move to next field |
| **Shift + Tab** | Move to previous field |
| **Enter** | Submit form (when on form) |
| **Ctrl + Enter** | Submit form (from any field) |
| **Ctrl + P** | Print results |
| **Alt + Home** | Go to home page (from any page) |
| **Alt + Back** | Go back to previous page |
| **Space** | Select/activate button or checkbox |

### **Using Keyboard Navigation:**

1. Press **Tab** to move through form fields
2. Use **Arrow Keys** to select options in dropdowns
3. Press **Space** or **Enter** to select an option
4. Press **Ctrl + Enter** to submit the form
5. Press **Ctrl + P** on results page to print

---

## Accessibility Features

### **For Keyboard Users**
- All functionality accessible without mouse
- Logical tab order through form
- Skip link to jump to main content
- Focus indicators visible on all interactive elements
- Keyboard shortcuts for common actions

### **For Screen Reader Users**
- All form fields have descriptive labels
- Help text properly associated with fields
- Error messages announced during validation
- Status updates announced live
- Semantic HTML for proper document structure
- Navigation landmarks (header, main, footer)

### **For Vision-Impaired Users**
- High contrast mode support
- Text remains readable in high contrast
- Color not the only indicator of status
- Icons paired with text labels
- Sufficient font size (base 16px)

### **For Motor-Impaired Users**
- Large touch targets (44×44px minimum)
- Buttons and links easy to activate
- No requirement for precise timing
- Form can be completed entirely with keyboard
- No hover-only content

### **For Users Preferring Reduced Motion**
- Animations respect `prefers-reduced-motion` setting
- All content accessible without animation
- Smooth transitions optional
- No auto-playing content

### **Dark Mode**
- Automatic dark theme on dark mode system setting
- Maintains readability and contrast
- Colors adjusted for comfort in low light
- Can be toggled based on system preference

### **Print-Friendly**
- Results page prints beautifully
- All important information included
- Unnecessary UI elements hidden in print
- Use **Ctrl + P** or Print button to print

---

## Troubleshooting

### **"The page won't load"**

**Potential Causes & Solutions:**
- **Port 5000 already in use**: Try different port (change in `n.py`)
- **Flask not installed**: Run `pip install flask`
- **Connection rejected**: Ensure application is running (`python n.py`)

**Try:**
1. Stop any other services on port 5000
2. Restart the Flask application
3. Clear browser cache (Ctrl + Shift + Delete)
4. Try different browser

---

### **"Form validation keeps failing"**

**Check Your Input:**
- **Age**: Must be 18-120 (not younger or older)
- **Cholesterol**: Must be 0-1000 mg/dL
- **HDL**: Must be 0-500 mg/dL
- **Blood Pressure**: Must be 0-300 mm Hg
- **All fields**: Must have a selection/value

**Red error text** appears below field explaining the issue.

---

### **"Progress indicator not showing"**

**This might mean:**
- JavaScript not enabled in browser
- Page didn't load completely
- Browser cache issue

**Try:**
1. Refresh page (F5 or Cmd+R)
2. Clear cache and cookies
3. Enable JavaScript in browser settings
4. Try different browser

---

### **"Print button not working"**

**Try:**
1. Use keyboard shortcut: **Ctrl + P**
2. Use browser menu: File → Print
3. Right-click and select "Print"
4. Press **Cmd + P** on Mac

---

### **"Results page looks different on my device"**

**This is normal!** The application is responsive and adapts to:
- Different screen sizes
- Portrait/landscape orientation
- Different browsers
- Mobile, tablet, and desktop

All functionality works the same across devices.

---

### **"I can't access form fields with keyboard"**

**Make sure:**
1. JavaScript is enabled
2. Browser is not blocked by extensions
3. Tab through all fields (don't skip)
4. Check browser compatibility

**Accessibility Check:**
- Tab key navigates all fields
- Enter submits form
- All buttons clickable
- Error messages shown

---

### **"Dark mode colors look wrong"**

**Solutions:**
1. Check your system dark mode setting
2. Adjust browser zoom (Ctrl + +/-)
3. Check browser extensions affecting colors
4. Try clearing browser cache

---

## Important Disclaimers

### ⚠️ **Medical Disclaimer**

This Heart Risk Predictor is an **informational tool only** and is NOT:
- A medical diagnosis
- Medical advice
- A substitute for professional healthcare
- Accurate for all populations
- A guarantee of disease risk

### ✅ **What You Should Do**

- **Always Consult Healthcare Professionals**: For medical evaluation, diagnosis, or treatment
- **Don't Delay Medical Care**: If experiencing cardiac symptoms, seek immediate medical attention
- **Use as Discussion Tool**: Share results with your doctor
- **Follow Medical Guidance**: Your healthcare provider's advice takes precedence

### 📋 **Limitations**

This tool uses statistical models based on:
- Specific population data
- Limited health factors
- Historical patterns
- General population averages

**Factors NOT Considered:**
- Family history of heart disease
- Stress levels
- Sleep quality
- Physical fitness level
- Diet quality
- Other medical conditions
- Medications
- Genetic factors
- Environmental factors

### 🔒 **Privacy & Data**

- **No Data Stored**: Your information is never saved
- **No Tracking**: No cookies or tracking enabled
- **No Sharing**: Information not shared with third parties
- **Local Processing**: All calculations done locally
- **Delete Data**: Clear browser cache to remove any stored info

### 💊 **If You Have Symptoms**

If experiencing any of these symptoms, **seek immediate medical attention**:
- Chest pain or pressure
- Shortness of breath
- Pain in arm, jaw, or neck
- Severe dizziness
- Sudden sweating
- Nausea or vomiting

---

## Getting Help

### **If You Have Technical Questions:**
- Check this guide first
- Review inline help text in the application
- Check browser developer tools (F12) for errors

### **If You Have Medical Questions:**
- Consult your healthcare provider
- Call your doctor's office
- Visit urgent care or emergency room for severe symptoms
- Call emergency services (911) for cardiac emergencies

---

## Tips for Best Experience

### **Best Results:**
1. ✅ Use recent blood test results (within 1 year)
2. ✅ Be honest and accurate with information
3. ✅ Fill out all fields completely
4. ✅ Use a modern browser (Chrome, Firefox, Safari, Edge)
5. ✅ Ensure JavaScript is enabled

### **Accessibility Tips:**
1. 🎧 Use a screen reader for best accessibility
2. ⌨️ Navigate entirely with keyboard
3. 🌓 Enable dark mode for comfortable viewing
4. 🔍 Zoom to 200% if needed
5. 🎬 Enable "Reduce Motion" for accessibility

### **Print Tips:**
1. 🖨️ Print results for your records
2. 📄 Share with healthcare provider
3. 🎨 Use color printer for best appearance
4. 📋 Save as PDF for archival

---

## Frequently Asked Questions (FAQ)

### **Q: How accurate is this tool?**
A: This is a statistical estimation tool based on population data. It's meant as a general indicator, not a definitive diagnosis. Accuracy varies by population and individual circumstances.

### **Q: Can I use this tool for someone else?**
A: Yes, but ensure you have their accurate health data. The results should be discussed with their healthcare provider.

### **Q: How often should I run this assessment?**
A: You can run it anytime, especially after significant health changes or new test results. Annual checks are reasonable.

### **Q: Why does my risk score seem high?**
A: Multiple factors affect heart disease risk. Discuss your results with your doctor to understand your specific factors.

### **Q: What if I don't know a specific metric?**
A: You'll need to get recent test results from your healthcare provider. Don't guess or estimate.

### **Q: Can I export my results?**
A: Yes! Use the Print function (Ctrl+P) and save as PDF for a permanent record.

### **Q: Is my data secure?**
A: Your data is never stored or transmitted. All calculations happen locally in your browser.

### **Q: What browser should I use?**
A: Any modern browser works (Chrome, Firefox, Safari, Edge). We recommend the latest version for best compatibility.

### **Q: Can I take the assessment on mobile?**
A: Yes! The application is fully responsive and works on phones and tablets.

---

## Contact & Support

- **Technical Issues**: Check browser console (F12) for error messages
- **Medical Questions**: Consult healthcare provider
- **Application Feedback**: Refer to README.md for project information

---

**Last Updated**: March 13, 2026  
**Version**: 1.0

---

*Always consult healthcare professionals for medical decisions. This tool is for informational purposes only.*
