# Heart Risk Predictor - Deployment Guide

Complete step-by-step guide to deploy your application to the cloud.

---

## Table of Contents

1. [Step 1: Prepare Your Project](#step-1-prepare-your-project)
2. [Step 2: Push to GitHub](#step-2-push-to-github)
3. [Step 3: Choose Hosting Platform](#step-3-choose-hosting-platform)
4. [Step 4: Deploy to Render.com (Recommended)](#step-4-deploy-to-rendercom-recommended)
5. [Step 5: Deploy to Railway.app (Alternative)](#step-5-deploy-to-railwayapp-alternative)
6. [Step 6: Post-Deployment Testing](#step-6-post-deployment-testing)
7. [Troubleshooting](#troubleshooting)

---

## Step 1: Prepare Your Project

### 1.1 Create `requirements.txt`

Create a file named `requirements.txt` in your project root with all Python dependencies:

```bash
cd "c:\Users\VIJAYASOORIYAN.K\Desktop\ML Start\webApp"
```

Create the file with this content:

```
flask==2.3.0
numpy==1.24.0
joblib==1.2.0
gunicorn==21.2.0
```

**Why Gunicorn?** Flask's built-in server is not production-ready. Gunicorn is a production WSGI HTTP Server.

### 1.2 Create `Procfile`

Create a file named `Procfile` (no extension) in your project root:

```
web: gunicorn n:app
```

This tells the hosting platform how to run your app.

### 1.3 Create `runtime.txt`

Create a file named `runtime.txt` to specify Python version:

```
python-3.11.0
```

### 1.4 Update `n.py` for Production

Your Flask app needs one small change to work on production servers:

**Find:**
```python
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
```

**Change to:**
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

**Add this import at the top of `n.py`:**
```python
import os
```

### 1.5 Create `.gitignore`

Create a file named `.gitignore` in your project root:

```
.venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.DS_Store
.env
*.egg-info/
dist/
build/
```

---

## Step 2: Push to GitHub

### 2.1 Initialize Git (if not already done)

```powershell
cd "c:\Users\VIJAYASOORIYAN.K\Desktop\ML Start\webApp"
git init
```

### 2.2 Configure Git

```powershell
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

### 2.3 Add Remote Repository

```powershell
git remote add origin https://github.com/vijayasooriyan/heart-risk-predictor.git
```

### 2.4 Add All Files

```powershell
git add .
```

### 2.5 Create Initial Commit

```powershell
git commit -m "Initial commit: Heart Risk Predictor application with HCI optimization"
```

### 2.6 Push to GitHub

```powershell
git branch -M main
git push -u origin main
```

**Note:** You may be prompted for GitHub authentication. Use:
- **Username**: Your GitHub username
- **Password**: Your GitHub personal access token (create at https://github.com/settings/tokens)

### 2.7 Verify on GitHub

Visit: `https://github.com/vijayasooriyan/heart-risk-predictor`

You should see all your files uploaded ✓

---

## Step 3: Choose Hosting Platform

### Comparison of Popular Options

| Platform | Cost | Ease | Startup Time | Best For |
|----------|------|------|--------------|----------|
| **Render.com** | Free tier available | ⭐⭐⭐⭐⭐ | 2-3 min | Beginners (Recommended) |
| **Railway.app** | Free tier available | ⭐⭐⭐⭐ | 3-5 min | Developers |
| **PythonAnywhere** | Free tier available | ⭐⭐⭐⭐ | 5-10 min | Python specialists |
| **Heroku** | Paid only now | ⭐⭐⭐⭐ | 2-3 min | Professional apps |
| **AWS** | Pay-as-you-go | ⭐⭐ | 15-30 min | Enterprise |

**For beginners: Use Render.com** (easiest and fastest)

---

## Step 4: Deploy to Render.com (Recommended)

### 4.1 Create Render.com Account

1. Go to https://render.com
2. Click **Sign Up**
3. Sign up with GitHub (recommended for easy deployment)

### 4.2 Create New Web Service

1. Click **Dashboard** (top right)
2. Click **New** (top left)
3. Select **Web Service**

### 4.3 Connect GitHub Repository

1. Under "Connect a repository":
   - Click **Connect your account** (GitHub)
   - Select your repository: `heart-risk-predictor`
   - Click **Connect**

### 4.4 Configure Deployment Settings

Fill in the form:

| Field | Value |
|-------|-------|
| **Name** | heart-risk-predictor |
| **Environment** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn n:app` |
| **Instance Type** | Free |
| **Region** | Choose closest to you |

### 4.5 Click Deploy

Click **Create Web Service** at the bottom.

**Wait 2-3 minutes** for deployment to complete.

### 4.6 Get Your Live URL

Once deployment is complete:
- You'll see a URL like: `https://heart-risk-predictor.onrender.com`
- Click it to visit your live app! 🎉

---

## Step 5: Deploy to Railway.app (Alternative)

### 5.1 Create Railway Account

1. Go to https://railway.app
2. Click **Start Project**
3. Sign up with GitHub

### 5.2 Import from GitHub

1. Click **Import from GitHub**
2. Find and select `heart-risk-predictor`
3. Click **Deploy Now**

### 5.3 Configure Environment Variables

1. Go to **Variables** tab
2. No special variables needed for basic deployment

### 5.4 Set Start Command

Go to **Settings** → **Deployment**:

```
gunicorn n:app
```

### 5.5 Deploy

Click **Deploy** and wait 3-5 minutes.

---

## Step 6: Post-Deployment Testing

### 6.1 Test All Pages

Visit these URLs:
- ✓ **Home Page**: `https://your-app-name.onrender.com/`
- ✓ **Assessment Form**: `https://your-app-name.onrender.com/patient`
- ✓ **Sample Assessment**: Fill form and submit

### 6.2 Test Features

1. **Form Validation**: Try entering invalid data
2. **Risk Assessment**: Complete form and verify results
3. **Print**: Click print button on results
4. **Keyboard Shortcuts**: Test Ctrl+P, Ctrl+Enter
5. **Mobile**: Open on phone/tablet and test responsiveness

### 6.3 Check Logs

**Render.com:**
- Click your service
- Go to **Logs** tab
- Check for any errors

**Railway.app:**
- Click your project
- Go to **Logs**
- Review application output

---

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'flask'"

**Solution:**
1. Ensure `requirements.txt` exists and has all dependencies
2. Check build logs for errors
3. Redeploy with: `git push` (auto-deploys)

### Problem: "Port already in use"

**Solution:**
Your `n.py` must use environment variable for port:
```python
port=int(os.environ.get('PORT', 5000))
```

### Problem: "Application crash on startup"

**Solution:**
1. Check logs in hosting platform dashboard
2. Verify `Procfile` is formatted correctly
3. Test locally: `gunicorn n:app`

### Problem: "Models not found"

**Solution:**
Ensure `.sav` files are in project root:
```
1heart_risk_regression.sav
1model_poly.sav
1model_qntl_data.sav
1model_qntl_target.sav
```

Files must be pushed to GitHub!

### Problem: "Blank/White page after deployment"

**Solution:**
1. Check browser console (F12) for errors
2. Check application logs
3. Verify static files are served correctly

### Problem: "Very slow page loads"

**Solution:**
- Free tier is slower (~30-50 seconds startup)
- First request is slowest (container cold start)
- Upgrade to paid tier for faster performance

---

## Updating Your Deployed App

After each change to your code:

### 1. Commit Changes

```powershell
git add .
git commit -m "Description of changes"
```

### 2. Push to GitHub

```powershell
git push origin main
```

### 3. Automatic Redeploy

Your hosting platform will **automatically redeploy** within 2-5 minutes!

---

## Enable Custom Domain (Optional)

### Render.com Custom Domain

1. Go to **Settings** → **Domains**
2. Add custom domain (need to own it)
3. Update DNS records at domain registrar
4. SSL certificate auto-generated

### Railway.app Custom Domain

1. Go to **Settings** → **Custom Domain**
2. Add your domain
3. Update DNS records
4. Follow their DNS setup guide

---

## Important Security Notes

### ⚠️ Never commit sensitive data:
- Don't push API keys
- Don't push passwords
- Use environment variables for secrets

### Environment Variables on Render.com:

1. Go to **Environment**
2. Add variables if needed:
   ```
   FLASK_ENV=production
   ```

### Environment Variables on Railway.app:

1. Go to **Variables**
2. Add any needed configuration

---

## Monitoring & Performance

### Check Application Health

**Render.com:**
- Dead after 15 minutes of inactivity? (Free tier)
- First request takes 30-50 seconds (spinning up container)

**Solution:** Upgrade to paid tier or use uptime monitoring service

### Uptime Monitoring (FREE)

Use https://uptimerobot.com to:
- Ping your app every 5 minutes
- Get alerts if it goes down
- Keep it from sleeping

---

## Next Steps

### 1. Share Your App
- Send live URL to friends/family
- Test with real users
- Gather feedback

### 2. Monitor Performance
- Check logs regularly
- Fix any errors quickly
- Optimize slow pages

### 3. Add Features
1. User authentication
2. Result history
3. PDF export
4. Email results
5. Mobile app

### 4. Upgrade to Production
- Use paid tier for reliability
- Add custom domain
- Set up monitoring
- Enable auto-scaling

---

## Support & Resources

### Official Documentation
- **Render.com**: https://render.com/docs
- **Railway.app**: https://docs.railway.app
- **Flask**: https://flask.palletsprojects.com
- **Gunicorn**: https://gunicorn.org

### Community Help
- Stack Overflow: Tag `flask` and `deployment`
- GitHub Issues: Ask in your repo
- Reddit: r/webdev, r/learnprogramming

### DNS Configuration Help
- Namecheap DNS docs
- GoDaddy DNS docs
- Route 53 (AWS)

---

## Deployment Checklist

Before deploying, verify:

- [ ] `requirements.txt` exists and is complete
- [ ] `Procfile` exists and is correct
- [ ] `runtime.txt` specifies Python version
- [ ] `.gitignore` includes unnecessary files
- [ ] All `.sav` model files are in project root
- [ ] `n.py` uses `os.environ.get('PORT', ...)`
- [ ] `n.py` has `debug=False` for production
- [ ] All files committed to GitHub
- [ ] GitHub repo is set to public
- [ ] No sensitive data in code
- [ ] App runs locally with `gunicorn n:app`
- [ ] Tests pass: form validation, results page, all features

---

## Quick Reference

### Deploy to Render.com (5 minutes)
```
1. Push code to GitHub
2. Go to render.com → New Web Service
3. Select heart-risk-predictor repo
4. Set Build: pip install -r requirements.txt
5. Set Start: gunicorn n:app
6. Click Deploy
7. Wait 2-3 minutes
```

### Deploy to Railway.app (5 minutes)
```
1. Push code to GitHub
2. Go to railway.app → Import from GitHub
3. Select heart-risk-predictor
4. Set start command: gunicorn n:app
5. Click Deploy
6. Wait 3-5 minutes
```

---

**Your app will be live in < 5 minutes!** 🚀

Questions? Check troubleshooting section above.

---

**Last Updated**: March 13, 2026
