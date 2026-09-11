# Test Report — 06 Bill Calculator

## Test environment

- Python: `.venv`
- Script: `06_bill_calculator.py`
- Date: 2026-09-11

---

## T01

### Input
Asakusa morning,
220,
160,
0,
8
### Expected
Total 380.0
cost/clip 47.5
You have a lot of usable clips!
### Actual
ASAKUSA MORNING
380.0
47.5
You have a lot of usable clips!

### Result
PASS

## T02

### Input
Solo shot
220
160
0
1

### Expected
Cost/clip 380.0
7 more clips needed to reach 8 usable clips.

### Actual
SOLO SHOT
380.0
380.0


### Result
PASS
