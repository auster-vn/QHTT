# Báo Cáo Chương Trình Giải Bài Toán Quy Hoạch Tuyến Tính

## Mục lục

- [1. Giới thiệu chương trình](#gioi-thieu-chuong-trinh)
- [2. Hướng dẫn sử dụng](#huong-dan-su-dung)
- [3. Ưu điểm & Hạn chế](#uu-diem--han-che)
- [4. Tài liệu tham khảo](#tai-lieu-tham-khao)
- [5. Phân công và đánh giá](#phan-cong-va-danh-gia)

---

## <a name="gioi-thieu-chuong-trinh"></a>1. Giới thiệu chương trình

Chương trình được viết bằng Python nhằm giải các bài toán Quy hoạch tuyến tính (Linear Programming – LP) với khả năng:
- Nhập liệu bài toán: hàm mục tiêu, ràng buộc, loại biến.
- Hỗ trợ biến tự do và có giới hạn âm/dương.
- Giải bài toán sử dụng thư viện `pulp`.
- Hiển thị kết quả trực quan bằng bảng (`rich`) và vẽ vùng nghiệm khả thi với `matplotlib`.

Ví dụ: Bài toán LP sau (trích từ ảnh) có thể được giải dễ dàng:

```
max    x₁ + 3x₂
s.t.  -x₁ - x₂ ≤ -3
      -x₁ + x₂ ≤ -1
      -x₁ + 2x₂ ≤ 2
       x₁, x₂ ≥ 0
```

### Giải thích một số đoạn mã quan trọng

```python
problem = pulp.LpProblem("Linear_Problem", pulp.LpMaximize if objective_type == "max" else pulp.LpMinimize)
```
➡️ Tạo một bài toán LP với kiểu Max hoặc Min.

```python
var = pulp.LpVariable(f"x{i+1}", lowBound=0)
```
➡️ Khởi tạo biến với ràng buộc không âm.

```python
if vtype == "tự do":
    x_pos = pulp.LpVariable(f"x{i+1}_pos", lowBound=0)
    x_neg = pulp.LpVariable(f"x{i+1}_neg", lowBound=0)
    real_vars.append(x_pos - x_neg)
```
➡️ Biến tự do được thay thế bằng hiệu của 2 biến không âm.

```python
problem += expr <= b[i]
```
➡️ Thêm ràng buộc tuyến tính vào bài toán.

```python
problem.solve()
```
➡️ Gọi hàm giải bài toán bằng `pulp`.

```python
plot_2d_feasible_region(...)
```
➡️ Hàm vẽ hình minh họa vùng nghiệm và hàm mục tiêu khi bài toán có 2 biến.

---

## <a name="huong-dan-su-dung"></a>2. Hướng dẫn sử dụng

### Cài đặt yêu cầu

```bash
pip install pulp rich matplotlib numpy
```

### Chạy chương trình

```bash
python code.py
```

### ✍️ Nhập input mẫu (bài toán trong ảnh)

```
🔢 Nhập số biến: 2
🎯 Nhập loại hàm mục tiêu: max
🧮 Nhập hệ số hàm mục tiêu: 
>> 1 3
Biến x1 có loại gì? >=0
Biến x2 có loại gì? >=0
🔒 Nhập số ràng buộc: 3
...
```

### Output mẫu

- Bảng giá trị các biến.
- Giá trị tối ưu.
- Đồ thị vùng nghiệm và hàm mục tiêu.

---

## <a name="uu-diem--han-che"></a>3. Ưu điểm & Hạn chế

### Ưu điểm:
- Giao diện dòng lệnh thân thiện, có màu.
- Hỗ trợ biến tự do, biến âm.
- Có hình minh họa hình học 2D.

### Khuyết điểm:
- Chỉ vẽ hình với bài toán 2 biến.
- Nhập liệu thủ công, dễ sai sót.
- Không có kiểm tra ràng buộc trùng lặp.

---

## <a name="tai-lieu-tham-khao"></a>4. Tài liệu tham khảo

- [PuLP Documentation](https://coin-or.github.io/pulp/)
- [Rich – Text formatting](https://rich.readthedocs.io/)
- [Matplotlib](https://matplotlib.org/)
- Giáo trình Toán Rời Rạc & Quy Hoạch Tuyến Tính – HCMUS.

---

## <a name="phan-cong-va-danh-gia"></a>5. Phân công và đánh giá

| Họ tên         | MSSV       | Nhiệm vụ                            |
|----------------|------------|----------------------------------------|
| Trần Châu Phú | 22110158   | Viết mã chương trình, kiểm thử, báo cáo |
