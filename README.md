# Giải Bài Toán Quy Hoạch Tuyến Tính

---

## Mục lục

1. [Giới thiệu chương trình](#1-giới-thiệu-chương-trình)  
2. [Hướng dẫn sử dụng](#2-hướng-dẫn-sử-dụng)  
3. [Ưu điểm và khuyết điểm](#3-ưu-điểm-và-khuyết-điểm)  
4. [Tài liệu tham khảo](#4-tài-liệu-tham-khảo)

---

## 1. Giới thiệu chương trình

Chương trình này giúp giải bài toán Quy Hoạch Tuyến Tính (Linear Programming) với nhiều biến và ràng buộc khác nhau.  
- Hỗ trợ các loại biến: không âm (≥0), không dương (≤0), và biến tự do (có thể âm hoặc dương).  
- Người dùng nhập vào hàm mục tiêu (tối đa hoặc tối thiểu), hệ số biến, các ràng buộc tuyến tính với dấu ≤, ≥, =.  
- Sử dụng thư viện **PuLP** để giải bài toán và **Rich** để hiển thị giao diện dòng lệnh thân thiện, trực quan.  
- Nếu bài toán có 2 biến, chương trình còn hỗ trợ vẽ đồ thị vùng nghiệm khả thi và hàm mục tiêu, giúp hình dung trực quan bài toán.

---

## 2. Hướng dẫn sử dụng

1. Chạy chương trình: `python <tên_file>.py`  
2. Nhập số biến của bài toán.  
3. Chọn loại hàm mục tiêu: tối đa (max) hoặc tối thiểu (min).  
4. Nhập hệ số hàm mục tiêu (cách nhau bằng dấu cách).  
5. Nhập loại biến cho từng biến (≥0, ≤0, hoặc tự do).  
6. Nhập số ràng buộc.  
7. Lần lượt nhập hệ số cho từng ràng buộc, chọn dấu ràng buộc (≤, ≥, =) và nhập giá trị b tương ứng.  
8. Chương trình sẽ in ra kết quả: trạng thái bài toán, giá trị tối ưu và giá trị các biến.  
9. Nếu số biến là 2, chương trình sẽ tự động vẽ đồ thị vùng nghiệm khả thi và hàm mục tiêu.

---

## 3. Ưu điểm và khuyết điểm

### Ưu điểm

- **Dễ sử dụng** với giao diện dòng lệnh rõ ràng và tương tác trực tiếp qua Rich.  
- **Hỗ trợ đầy đủ** các loại biến, phù hợp với nhiều dạng bài toán thực tế.  
- **Đồ thị minh họa** cho bài toán 2 biến giúp người dùng hình dung vùng nghiệm khả thi và hàm mục tiêu.  

### Khuyết điểm

- **Chỉ hỗ trợ bài toán tuyến tính.** Không giải được bài toán phi tuyến hay các bài toán tối ưu khác.  
- **Đồ thị chỉ vẽ được cho 2 biến.** Với số biến lớn hơn 2, không có hình ảnh trực quan.  
- **Phần nhập liệu thủ công**, có thể gây lỗi nếu nhập sai định dạng hoặc số lượng hệ số.  

---

## 4. Tài liệu tham khảo

- [PuLP Documentation](https://coin-or.github.io/pulp/)  
- [Rich Documentation](https://rich.readthedocs.io/en/stable/)  
- Winston, Wayne L. *Operations Research: Applications and Algorithms*, 4th Edition.  
- Hillier, Frederick S., and Lieberman, Gerald J. *Introduction to Operations Research*, 10th Edition.  

---

*Chương trình được viết bằng Python, sử dụng các thư viện mở PuLP và Rich, kết hợp Matplotlib để vẽ đồ thị.*

