# Python Foundation

Repository luyện tập Python cơ bản phục vụ lộ trình Freelancer.

## Requirements

- Python 3.x
- Git
- VS Code
- Remote: local-only
## Activate virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

## Run exercises

```powershell
python .\01_profile.py
python .\02_greeting.py
python .\03_sum_two_numbers.py
python .\05_temperature.py
python .\07_expense_cli.py
```

## Debug log

### Case 1: String concatenation

- Symptom: `2 + 3` cho kết quả `23`.
- Cause: `input()` trả về `str`.
- Fix: chuyển bằng `int()` hoặc `float()`.

### Case 2: ValueError

- Symptom: `float("abc")` tạo traceback.
- Cause: input không phải số.
- Fix: validation bằng `try/except ValueError`.


## Week 1 retrospective

### Keep

1. Luôn chạy chương trình từ terminal.
2. Kiểm tra `git status` trước và sau commit.

### Problem

1. Đôi khi quên kích hoạt `.venv`.
2. Dễ nhầm dữ liệu từ `input()` là số.

### Try

1. Kiểm tra `Get-Command python` ở đầu mỗi buổi.
2. Viết test case trước khi coi chương trình đã hoàn thành.
