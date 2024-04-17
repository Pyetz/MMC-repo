# CHƯƠNG TRÌNH TÍNH TOÁN ĐIỂM THI CHO CÁC LỚP

## Mục Lục

- Tổng quan về ứng dụng
- Cài Đặt
- Chạy Chương Trình

## Tổng quan về ứng dụng

### Tổ chức project và các modules
![image](https://github.com/Pyetz/MMC-repo/assets/146900526/ecb27ada-6aa5-48e1-90d2-23bf254dad6f)

### Chạy project
  1. Khi chạy ứng dụng sẽ xuất hiện menu chính:
     ![image](https://github.com/Pyetz/MMC-repo/assets/146900526/1e30340d-7b71-457c-9e0d-b66a07e39a3c)
     Bạn chỉ được chọn 1 hoặc 2, nếu sai sẽ yêu cầu nhập lại.
  2. Nếu bạn chọn 2, thực hiện thoát ứng dụng.
  3. Nếu bạn chọn 1, chương trình sẽ yêu cầu bạn nhập vào đường dẫn đến file tương ứng với 1 lớp:
     ![image](https://github.com/Pyetz/MMC-repo/assets/146900526/9d3956b4-76d5-477f-b145-b6f22012072e)
     Input được coi là hợp lệ: Data/classX.txt hoặc classX.txt hoặc classX
  4. Sau khi nhập path hợp lệ, chương trình sẽ chuyển đến action menu, nơi bạn có thể thực hiện các thao tác với lớp:
     ![image](https://github.com/Pyetz/MMC-repo/assets/146900526/9f62e394-8757-4dd0-9ffc-0e977eb18902)
  5. Nếu bạn chọn 1, chương trình in ra kết quả các thống kê trong task 2
  6. Nếu bạn chọn 2, chương trình in ra kết quả các thống kê trong task 3
  7. nếu bạn chọn 3, chương trình thực hiện chấm điểm cho các học sinh có câu trả lời hợp lệ trong lớp và ghi kết quả vào file Grades/classX_grades.txt
  8. Nếu bạn chọn 4, trở về menu chính

## Cài đặt và chạy chương trình

### Yêu cầu tối thiểu:
  - Sử dụng phiên bản python 3.
    - Chạy lênh sau để kiểm tra bạn đã cài python hay chưa (nếu có sẽ hiển thị phiên bản python 3.x.x):
      ```
      python --version
      ```
    - Nếu chưa có, bạn có thể cài một phiên bản [python 3](https://www.python.org/downloads/) bất kỳ.
    - (nhớ check vào add python.exe to path trong quá trình cài đặt).
    - khởi động lại cmd và chạy lệnh python --version.
  - Đã cài đặt các thư viện: pandas, numpy. Nếu chưa, thực hiện chạy lệnh sau:
    ```
    pip install pandas numpy
    ```

### Cài đặt
  - Thực hiện clone project về folder
  - Mở Terminal trên macos/linux hoặc Command Prompt (cmd) trên windows, di chuyển đến folder bạn muốn clone dự án về bằng lệnh cd:
    ```cd
    cd (your path)
  - Thực hiện clone project về folder nơi bạn đang đứng:
    ```clone
    git clone https://github.com/Pyetz/MMC-repo.git

### Chạy chương trình
  - Di chuyển đến folder chứa project
    - Mở terminal/cmd từ folder MMC-repo và di chuyển đến folder chứa project
      ```
      cd Module_1/Final_Project
      ```
    - Hoặc mở terminal/cmd từ folder Final_Project
  - Chạy project bằng lệnh sau:
    ```
     python Phat_Vu_grade_the_exams.py
    ```
