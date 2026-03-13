# Quick Deployment Steps

Follow these exact steps to deploy your Heart Risk Predictor to the cloud.

---

## ✅ Phase 1: Prepare Files (DONE!)

Your deployment files are ready:
- ✓ `requirements.txt` - Updated with gunicorn
- ✓ `Procfile` - Production startup configuration  
- ✓ `runtime.txt` - Python version specification
- ✓ `.gitignore` - Git ignore patterns
- ✓ `n.py` - Updated for production

---

## 📝 Phase 2: Push Code to GitHub (5 minutes)

### Step 1: Open PowerShell Terminal

```powershell
cd "c:\Users\VIJAYASOORIYAN.K\Desktop\ML Start\webApp"
```

### Step 2: Check Git Status

```powershell
git status
```

You should see all files listed.

### Step 3: Add All Files

```powershell
git add .
```

### Step 4: Commit Changes

```powershell
git commit -m "Add production deployment configuration (Procfile, requirements.txt, runtime.txt)"
```

### Step 5: Push to GitHub

```powershell
git push origin main
```

**You may be asked to authenticate:**
- Go to: https://github.com/settings/tokens
- Generate new token (Personal access tokens → Classic)
- Copy the token
- Paste it as password when prompted

### Step 6: Verify on GitHub

Visit: `https://github.com/vijayasooriyan/heart-risk-predictor`

You should see all files including:
- ✓ Procfile
- ✓ requirements.txt
- ✓ runtime.txt
- ✓ .gitignore
- ✓ All templates and models

---

## 🚀 Phase 3: Deploy to Render.com (5 minutes)

### Step 1: Create Account

1. Go to https://render.com
2. Click **Sign Up**
3. Choose **Sign up with GitHub** (recommended)
4. Authorize GitHub connection

### Step 2: Create New Web Service

1. Click **Dashboard**
2. Click **New** → **Web Service**

### Step 3: Select Repository

1. Under "Connect repository", click **Connect account**
2. Find `heart-risk-predictor`
3. Click **Connect**

### Step 4: Fill Out Form

| Field | Value |
|-------|-------|
| **Name** | `heart-risk-predictor` |
| **Environment** | `Python 3` |
| **Region** | Choose closest to you |
| **Branch** | `main` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn n:app` |
| **Instance Type** | `Free` |

### Step 5: Deploy

Click **Create Web Service** button at bottom.

### Step 6: Wait for Deployment

Watch the logs. It will show:
```
=== Deploying...
Building...
Installing dependencies...
Starting server...
```

Once complete (2-3 minutes), you'll see:
```
✓ Service deployed
```

### Step 7: Get Your Live URL

Click the URL shown (like `https://heart-risk-predictor.onrender.com`)

**🎉 Your app is LIVE!**

---

## 🧪 Phase 4: Test Your Deployed App (5 minutes)

### Test 1: Home Page
- Open: `https://heart-risk-predictor.onrender.com/`
- Should see: Landing page with features

### Test 2: Assessment Form
- Click: "Start Assessment"
- Should load form with all fields

### Test 3: Complete Assessment
1. Fill in fake data:
   - Name: Test User
   - Gender: Male
   - Age: 45
   - TC: 200
   - HDL: 50
   - SBP: 120
   - BP Med: No
   - Smoking: Never
   - Diabetes: No

2. Click: "Submit"
3. Should show: Risk results page

### Test 4: Print Functionality
- Click: "Print Results"
- Should open print preview

### Test 5: Mobile Testing
- Open app on phone/tablet
- Should be responsive and work perfectly

### Test 6: All Navigation
- Click: "New Assessment" → Should go back to form
- Click: "Home" → Should go to landing

**If all tests pass: ✅ DEPLOYMENT SUCCESSFUL!**

---

## 🔗 Share Your Live App

Your app is now live! Share it:

```
https://heart-risk-predictor.onrender.com
```

Send to:
- Friends and family
- Social media
- Portfolio/resume
- GitHub README

---

## ⚙️ Post-Deployment: Add More Features

### Auto-Redeploy on GitHub Push

Every time you push code to GitHub, Render will:
1. Automatically detect the push
2. Rebuild your app
3. Redeploy (takes 2-5 minutes)

To add features:

```powershell
# Make changes to files
# Then:
git add .
git commit -m "Description of changes"
git push origin main

# App automatically redeploys!
```

### Check Application Logs

On Render Dashboard:
1. Click your service
2. Go to **Logs** tab
3. See real-time app output and errors

---

## 🎯 Next Steps

### Immediate (This Week)
- [ ] Deploy to Render.com (follow above)
- [ ] Test all features
- [ ] Share link with feedback group
- [ ] Gather user feedback

### Short Term (This Month)
- [ ] Add custom domain (optional)
- [ ] Monitor app logs
- [ ] Fix any bugs reported
- [ ] Add user reviews/ratings

### Medium Term (3 Months)
- [ ] Add user authentication
- [ ] Store assessment history
- [ ] Export results as PDF
- [ ] Email results functionality
- [ ] Advanced analytics

### Long Term (6 Months)
- [ ] Mobile app using React Native
- [ ] Integration with wearables
- [ ] Telehealth provider integration
- [ ] Clinical trial data integration

---

## 🆘 Troubleshooting

### App Shows Blank Page
- Check Render logs
- Verify all `.sav` files uploaded to GitHub
- Check browser console (F12) for errors

### Deployment Failed
- Check build logs on Render
- Verify `Procfile` format (no `.txt` extension)
- Check `requirements.txt` has gunicorn
- Try redeploying

### Models Not Loading
- Verify `.sav` files in GitHub repo
- Check file paths are correct in `n.py`
- Check Render logs for file not found errors

### First Request is Slow
- Normal! Free tier needs 30-50 seconds to start
- Subsequent requests are fast
- Upgrade to paid tier for faster startup

### Getting Errors in Logs
- Read error message carefully
- Search error on Stack Overflow
- Check Flask/Render documentation
- Update to latest package versions

---

## 📞 Support Resources

### Official Docs
- **Render.com**: https://render.com/docs
- **Flask**: https://flask.palletsprojects.com
- **Gunicorn**: https://gunicorn.org

### Community Help
- Stack Overflow (tag: flask, render)
- GitHub Issues in your repo
- Reddit: r/webdev, r/Python

---

## 🎉 Congratulations!

Your Heart Risk Predictor is now deployed to the cloud and accessible to anyone with the link!

**What you've accomplished:**
✅ Created professional Flask web application  
✅ Implemented 18+ HCI principles  
✅ Deployed to production server  
✅ Made app accessible to the world  
✅ Set up continuous deployment  

**You're now a full-stack web developer!** 🚀

---

## Quick Command Reference

```powershell
# Check git status
git status

# Add all files
git add .

# Commit changes
git commit -m "Description"

# Push to GitHub
git push origin main

# Check local git config
git config --list

# View git log
git log --oneline
```

---

**Ready? Start with Phase 2!**

Next: Open PowerShell and run the commands in Phase 2 → Let's get your app live! 🚀
