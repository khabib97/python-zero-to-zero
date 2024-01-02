## Pre-requisites

সিস্টেমে নিম্নলিখিত software ইনস্টল করা আছে তা নিশ্চিত করুন:

- [python](https://www.python.org/downloads/): পাইথন ইন্সটলার আপনার পিসি তে নামিয়ে নিন, পাইথন 3.6 বা তার উপরের ভার্সন ইন্সটল করুন।
- [pip](https://pip.pypa.io/en/stable/installation/): পাইথনের জন্য প্যাকেজ ইন্সটলার লাগবে পরবর্তীতে


## How to run the project

1. **Download the project:**
   ```bash
   git https://github.com/khabib97/python-zero-to-zero.git
   cd  python-zero-to-zero

2. **Enable virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   কোন প্যাকেজ ইনস্টল করার আগে আপনার ভার্চুয়াল এনভায়রনে অ্যাক্টিভ করা আছে তা নিশ্চিত করুন। এবং নিম্নলিখিত কমান্ডটি চালান। প্রতিদিনের নতুন ফাইল রান করার আগে একবার চালানোর প্রয়োজন হতে পারে।
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the project:**
   যেকোনো দিনের প্রজেক্ট চালানোর জন্য নিম্নলিখিত কমান্ডটি চালান, যেখানে `*` হচ্ছে দিনের নাম:
   ```bash
   python3 code/day_*.py
   ```