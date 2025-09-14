# 🐍 po - Python Library Generator

**po**: Creates Python libraries starters ✨

## 🚀 What (else) does it do?

It creates:
- 📁 A complete project folder with proper structure
- ⚙️ All the setup files you need (setup.py, requirements.txt, etc.)
- 🖥️ A command-line tool that works from anywhere
- 👋 A "Hello World" example to get you started
- 📝 A comprehensive `.gitignore` file
- 🔧 An initialized git repository with "init commit"
- 🎯 Ready-to-go virtual environment setup

## 📦 Installation

```bash
pip install -e .
```

## 🎯 How to use it

### Quick start:
```bash
po -n my-awesome-tool
```

That's it! 🎉 This creates a new library called `my-awesome-tool` in your `~/dev` folder.

### What you get:
When you run `po -n my-library`, it creates this structure:

```
my-library/                    📁 Your project folder
├── setup.py                  ⚙️ Package configuration
├── README.md                 📖 Documentation
├── requirements.txt          📋 Dependencies
└── my_library_lib/          🐍 Your Python code
    ├── __init__.py          🏠 Package entry point
    ├── __main__.py          🚀 Run with python -m
    └── cli.py               🖥️ Command-line interface
```

## 🎮 Using your new library

After **po** creates your library, here's how to use it:

```bash
# 1. Go into your new project
cd ~/dev/my-library

# 2. Create a virtual environment (keeps things clean!)
python3 -m venv .venv
source .venv/bin/activate

# 3. Install your library
pip install -e .

# 4. Use your new command!
my-library --help
my-library --name "Your Name"
```

## 🌟 Cool features

- 🏠 **Smart defaults**: Creates projects in `~/dev` by default
- 🎯 **Simple prompts**: Just asks for project name and location
- 🔧 **Ready to go**: Everything works immediately after creation
- 📱 **Cross-platform**: Works on Mac, Windows, and Linux

## 💡 Why use po?

- ⏰ **Save time**: No more manually creating project files
- 🎯 **Focus on code**: Spend time on your ideas, not setup
- 📚 **Learn**: See how Python libraries are structured
- 🚀 **Ship faster**: Get from idea to working tool in minutes

## 🎉 Examples

```bash
# Create a tool called "weather"
po -n weather

# Create a tool in a specific folder
po -n calculator -o ~/my-projects

# Create a tool in current directory
po -n todo -o .
```

**po** is perfect for beginners who want to learn Python packaging, or experienced developers who want to quickly prototype new tools! 🎯
