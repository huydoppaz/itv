### Only Advance Technique 

### SQL Injection : 
- Timebased SQL Injection : Kĩ thuật đây tận dụng việc truy vấn SQL có thể bị chậm lại hoặc bị treo để xác định xem một điều kiện cụ thể có đúng hay không. Điều này thường được thực hiện bằng cách sử dụng các hàm như `sleep()` hoặc `pg_sleep()` trong SQL.
- Error-based SQL Injection : Kỹ thuật này tận dụng các thông báo lỗi từ cơ sở dữ liệu để thu thập thông tin về cấu trúc cơ sở dữ liệu, tên bảng, tên cột, v.v. Thông báo lỗi có thể tiết lộ thông tin chi tiết về truy vấn SQL bị lỗi, giúp kẻ tấn công xây dựng các truy vấn SQL độc hại hơn.
- Union-based SQL Injection : Kỹ thuật này tận dụng phép kết hợp `UNION` trong SQL để kết hợp kết quả của hai truy vấn khác nhau. Kẻ tấn công có thể sử dụng kỹ thuật này để truy xuất dữ liệu từ các bảng khác nhau trong cơ sở dữ liệu mà không cần biết tên của chúng.
- Boolean-based SQL Injection : Kỹ thuật này dựa trên việc kiểm tra các điều kiện logic (đúng hoặc sai) thông qua các phản hồi từ ứng dụng. Kẻ tấn công sẽ thử nghiệm các điều kiện khác nhau để xác định xem điều kiện nào đúng và từ đó suy luận về cấu trúc cơ sở dữ liệu.

**Các case SQL -> RCE** : 

Với db postgresql , quyền user postgres có thể RCE 
Với db mssql , user SA có thể RCE 
Với mysql có thể đọc file bằng LOAD_FILE() và ghi file bằng INTO OUTFILE() sau đó thực thi file đó thông qua các kỹ thuật khác nhau như sử dụng UDF (User Defined Function) hoặc sử dụng các lỗ hổng trong các ứng dụng web khác để thực thi file đó. điều kiện : `secure_file_priv`

### 


### Insecure Deserialization 

**PHP** : 
- Sử dụng các hàm như `unserialize()`, `json_decode()` để phân tích chuỗi được mã hóa thành đối tượng PHP. Nếu chuỗi được phân tích không được kiểm tra kỹ lưỡng, kẻ tấn công có thể thực thi mã tùy ý trên máy chủ.

- Magic method trong PHP : 
- `__wakeup()` : Được gọi khi đối tượng được unserialize.
- `__destruct()` : Được gọi khi đối tượng bị hủy.
- `__toString()` : Được gọi khi đối tượng được chuyển đổi thành chuỗi.
- `__invoke()` : Được gọi khi đối tượng được gọi như một hàm.
- `__set()` : Được gọi khi gán một giá trị cho một thuộc tính không tồn tại hoặc không thể truy cập.
- `__get()` : Được gọi khi truy cập một thuộc tính không tồn tại hoặc không thể truy cập.
- `__isset()` : Được gọi khi sử dụng isset() hoặc empty() trên một thuộc tính không tồn tại hoặc không thể truy cập.
- `__call()` : Được gọi khi gọi một phương thức không tồn tại hoặc không thể truy cập.
- `__construct()` : Được gọi khi một đối tượng được tạo ra.
- `__clone()` : Được gọi khi một đối tượng được nhân bản.   

**Java** : 













