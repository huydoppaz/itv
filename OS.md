
# Linux 

**Directory Structure** : 

- `/` : Thư mục gốc
- `/bin` link đến `/usr/bin` : Các chương trình nhị phân cơ bản
- `/boot` : Các tệp cần thiết để khởi động hệ thống
- `/dev` : Các thiết bị 
- `/etc` : Các tệp cấu hình hệ thống
- `/home` : Thư mục cá nhân của người dùng
- `/lib` link đến `/usr/lib` : Các thư viện chung
- `/media` : Các thiết bị gắn kết ngoài
- `/mnt` : thư mục mount
- `/opt` : add-ons application
- `/proc` : Thông tin về các tiến trình đang chạy
- `/root` : Thư mục cá nhân của người dùng root
- `/run` : Các tệp chạy thời gian thực
- `/sbin` link đến `/usr/sbin` : Các chương trình nhị phân hệ thống
- `/srv` : data của các services
- `/sys` : Thông tin về hệ thống
- `/tmp` : Các tệp tạm thời
- `/usr` : Các ứng dụng và thư viện người dùng
- `/var` : Các tệp dữ liệu biến đổi (logs)



Chi tiết về `/proc` : 
- `/proc/cpuinfo` : Thông tin về CPU
- `/proc/meminfo` : Thông tin về bộ nhớ
- `/proc/version` : Thông tin về phiên bản kernel
- `/proc/net` : Thông tin về mạng
- `/proc/self` : Liên kết đến thư mục của tiến trình hiện tại
- `/proc/[pid]` : Thông tin về tiến trình có PID cụ thể
- `/proc/[pid]/status` : Trạng thái tiến trình
- `/proc/[pid]/cmdline` : Lệnh khởi chạy tiến trình
- `/proc/[pid]/fd` : Các file descriptor của tiến trình
- `/proc/[pid]/environ` : Các biến môi trường của tiến trình
- `/proc/[pid]/maps` : Bản đồ bộ nhớ của tiến trình
- `/proc/[pid]/stat` : Thông tin chi tiết về tiến trình
- `/proc/[pid]/statm` : Thông tin về sử dụng bộ nhớ của tiến trình

`/proc/[pid]/maps` : Bản đồ bộ nhớ của tiến trình, bao gồm các vùng nhớ được ánh xạ vào không gian địa chỉ của tiến trình. Mỗi dòng trong file này đại diện cho một vùng nhớ và chứa các thông tin như địa chỉ bắt đầu và kết thúc, quyền truy cập, loại ánh xạ, offset, device, inode, và tên file (nếu có).
https://man7.org/linux/man-pages/man5/proc.5.html


### Kernel Space và User Space

**Kernel Space** là không gian bộ nhớ nơi kernel (trung tâm điều khiển hệ thống) chạy. Kernel Space có quyền truy cập toàn bộ tài nguyên hệ thống, bao gồm cả phần cứng và các tài nguyên phần mềm khác. Kernel Space chịu trách nhiệm quản lý tài nguyên hệ thống, điều phối các tiến trình, xử lý các yêu cầu từ User Space, và thực hiện các tác vụ hệ thống khác. Kernel Space cũng đảm bảo rằng các tiến trình chạy trong User Space không thể truy cập trực tiếp vào các tài nguyên hệ thống quan trọng, giúp bảo vệ hệ thống khỏi các lỗi và tấn công.

**User Space** là không gian bộ nhớ nơi các tiến trình ứng dụng chạy. User Space có quyền truy cập hạn chế vào các tài nguyên hệ thống thông qua các API (Application Programming Interfaces) được cung cấp bởi kernel. Điều này giúp bảo vệ hệ thống khỏi các lỗi hoặc tấn công từ các tiến trình ứng dụng.

**User Space** thực hiện truy cập vào **Kernel Space** thông qua các hệ thống gọi (system calls). Hệ thống gọi là một giao diện giữa User Space và Kernel Space, cho phép các tiến trình ứng dụng yêu cầu các dịch vụ từ kernel như quản lý bộ nhớ, quản lý tệp tin, quản lý tiến trình, v.v.


**Các hệ thống gọi (system calls)** thường được thực hiện thông qua các lệnh đặc biệt như `int 0x80` trên x86 hoặc `syscall` trên x86-64. Khi một tiến trình thực hiện một hệ thống gọi, nó sẽ chuyển quyền kiểm soát cho kernel thông qua một ngắt phần mềm (software interrupt). Kernel sau đó xử lý yêu cầu của tiến trình và trả về kết quả cho tiến trình đó. 

**Các syscall phổ biến**: 
- `open`: Mở một file.
- `read`: Đọc dữ liệu từ một file.
- `write`: Ghi dữ liệu vào một file.
- `close`: Đóng một file.
- `fork`: Tạo một tiến trình con.
- `exec`: Thực thi một chương trình mới.
- `exit`: Kết thúc một tiến trình.
- `wait`: Chờ một tiến trình con kết thúc.
- `kill`: Gửi một tín hiệu đến một tiến trình.
- `getpid`: Lấy ID của tiến trình hiện tại.
- `getppid`: Lấy ID của tiến trình cha.



### Một vài file phổ biến :

`/etc/passwd` : Chứa thông tin về các tài khoản người dùng trên hệ thống.

Ví dụ : `Debian-exim:x:133:139::/var/spool/exim4:/usr/sbin/nologin` 

Trong đó : 
- `Debian-exim` : Tên tài khoản.
- `x` : Mật khẩu (được mã hóa và lưu ở `/etc/shadow`).
- `133` : UID (User ID).
- `139` : GID (Group ID).
- `::` : Thông tin bổ sung (thường để trống).
- `/var/spool/exim4` : Thư mục home của tài khoản.
- `/usr/sbin/nologin` : Shell mặc định khi đăng nhập (trong trường hợp này, người dùng không được phép đăng nhập).


`/etc/shadow` : Chứa mật khẩu đã được mã hóa của các tài khoản người dùng.

Ví dụ : `kali:$y$j9T$59Q4D77.2KEh1oee7.i..1$PD1XNBwmU8o2DxJzKatgmlAA0QhicizAklwnuA5OME9:19871:0:99999:7:::`

- `kali` : Tên tài khoản.
- `$y$j9T$59Q4D77.2KEh1oee7.i..1$PD1XNBwmU8o2DxJzKatgmlAA0QhicizAklwnuA5OME9` : Mật khẩu đã được băm.

Mật khẩu được mã hóa bằng thuật toán `yescrypt` (được chỉ định bởi `$y$j9T$`). Phần còn lại của chuỗi là các thông số cấu hình cho thuật toán mã hóa và chuỗi ngẫu nhiên được sử dụng để tăng cường bảo mật.
Trong đó : 
`yes crypt` sử dụng hàm băm SHA-256 
`$y$j9T$` : Chỉ định thuật toán mã hóa là `yescrypt`.
`59Q4D77.2KEh1oee7.i..1` : Đây là chuỗi ngẫu nhiên được sử dụng để tăng cường bảo mật (salt).
`PD1XNBwmU8o2DxJzKatgmlAA0QhicizAklwnuA5OME9` : Đây là phần mã hóa chính của mật khẩu. (hash) 
`:19871:0:99999:7:::` : Đây là các thông tin về chính sách mật khẩu và tài khoản:
- `19871`: Ngày thay đổi mật khẩu lần cuối (được tính từ ngày 1/1/1970).
- `0`: Số ngày tối thiểu giữa các lần thay đổi mật khẩu.
- `99999`: Số ngày tối đa giữa các lần thay đổi mật khẩu.
- `7`: Số ngày cảnh báo trước khi mật khẩu hết hạn.

- Các trường còn lại là trống, có nghĩa là không có các hạn chế cụ thể khác.








