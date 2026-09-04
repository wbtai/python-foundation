# Python Foundation

Repository luyện tập Python cơ bản phục vụ lộ trình Freelancer.

## Requirements

- Python 3.x
- Git
- VS Code

## Activate virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

## Run exercises

```powershell
python scripts/01_profile.py
python scripts/02_greeting.py
python scripts/03_sum_two_numbers.py
python scripts/04_age_next_year.py
python scripts/05_temperature.py
```

## Example: Temperature converter

Input:

```text
Nhiệt độ Celsius: 25
```

Output:

```text
25.0°C = 77.0°F
```

## Security

Không commit `.env`, API key, mật khẩu hoặc thông tin cá nhân nhạy cảm.


## Expense CLI manual tests

| Test | Input | Expected result | Actual result |
|---|---|---|---|
| Valid | Food, 500 | food — ¥500.00; discount ¥450.00 | Passed |
| Empty category | spaces, 500 | Category không được để trống. | Passed |
| Invalid amount | transport, abc | Amount phải là một số. | Passed |
| Non-positive amount | coffee, 0 | Amount phải lớn hơn 0. | Passed |

Run command:

```powershell
python scripts/07_expense_cli.py
```

Input format:

- Category: text.
- Amount: positive number using `.` for decimals.
- Example: `500` or `500.5`.