# 🐍 po - Python Library Generator

## 🚀 What does it do?

**Creates Python libraries starters** ✨

## 🚀 What (else) does it do?

It creates:
- 📁 A complete project folder with proper structure
- ⚙️ All the setup files you need (setup.py, requirements.txt, etc.)
- 🖥️ A command-line tool that works from anywhere
- 👋 A "Hello World" example to get you started
- 📝 A comprehensive `.gitignore` file
- 🔧 An initialized git repository with "init commit"
- 🎯 Ready-to-go virtual environment setup

## 📦 Installation from GitHub

### 🎯 Complete Setup Guide (GitHub → Working `po`)

**Step 1: Clone the repository**
```bash
git clone https://github.com/yourusername/po.git
cd po
```

**Step 2: Create virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**Step 3: Install po**
```bash
pip install -e .
```

**Step 4: Verify installation**
```bash
po --help
```

**🎉 That's it! You now have `po` working!**

### 🚀 Quick Install (One-liner)
```bash
git clone https://github.com/yourusername/po.git && cd po && python3 -m venv .venv && source .venv/bin/activate && pip install -e .
```

### 💡 Pro Tips
- **Always activate the virtual environment** before using `po`
- **Keep the virtual environment active** while working with `po`
- **Use `deactivate`** when you're done to exit the virtual environment

### 🔄 Daily Usage Workflow
```bash
# Every time you want to use po:
cd ~/path/to/po
source .venv/bin/activate
po -n my-new-tool
```

## 🎯 How to use it

### Quick start:
```bash
po -n my-awesome-tool

# or just po for interactive mode
```

### What you get:
- ✅ Virtual environment created (.venv)
- ✅ Package installed in editable mode
- ✅ Git repository initialized