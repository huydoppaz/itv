# JWT (JSON Web Token)

JWT bao gồm 3 phần : Header, Payload và Signature. Mỗi phần được mã hóa bằng Base64Url và được phân cách bằng dấu chấm (.).

## Header

Header thường bao gồm hai phần: loại token (JWT) và thuật toán mã hóa được sử dụng (ví dụ: HMAC SHA256 hoặc RSA).

### Payload

Payload chứa các thông tin về người dùng và các thông tin tùy chỉnh khác. Payload cũng được gọi là claims. Có ba loại claims chính:

### Signature

Signature được tạo ra bằng cách mã hóa header, payload và một khóa bí mật sử dụng thuật toán được chỉ định trong header. Signature được sử dụng để xác minh rằng người gửi JWT là người đã tạo ra nó và đảm bảo rằng JWT không bị thay đổi.

### Các lỗi bảo mật JWT 

### Chấp nhận token không có signature

JWT header tồn tại trường alg , trường này quy định thuật toán được dùng để sign token , do đó nếu không có signature thì JWT không thể xác thực được. Tuy nhiên, một số ứng dụng có thể chấp nhận JWT không có signature, điều này có thể dẫn đến việc một người dùng có thể tạo ra một JWT giả mạo mà không cần biết khóa bí mật.

Ví dụ kẻ tấn công sửa alg thành none và gửi JWT giả mạo , lúc này server sẽ không kiểm tra signature và chấp nhận JWT đó . 

### Brute Force secretkey 

Một vài thuật toán như HS256 (HMAC + SHA256) sử dụng secret key để tạo và xác thực JWT. Nếu kẻ tấn công có thể đoán hoặc brute force secret key, họ có thể tạo ra JWT hợp lệ mà không cần quyền truy cập hợp lệ.



### JWT header parametr injections 

Theo tài liệu về JWS , chỉ có alg là bắt buộc . Trên thực tế JWT header có thể tồn tại nhiều parameters . Các headers sau có thể interes : 

- jwk (JSON Web Key) : Cung cấp một đối tượng JSON để biểu diễn key

- jku (JSON Web Key Set URL) : Cung cấp URL mà máy chủ có thể lấy một bộ khóa chứa khóa chính xác

- kid (Key ID) : Cung cấp ID mà máy chủ có thể sử dụng để xác định khóa chính xác trong trường hợp có nhiều khóa để lựa chọn. Tùy thuộc vào định dạng của khóa, điều này có thể có tham số kid khớp.



### Inject self-signed JWTS qua jwk parameter

Ví dụ về 1 JWT headers : 

```
{
    "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
    "typ": "JWT",
    "alg": "RS256",
    "jwk": {
        "kty": "RSA",
        "e": "AQAB",
        "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
        "n": "yy1wpYmffgXBxhAUJzHHocCuJolwDqql75ZWuCQ_cb33K2vh9m"
    }
}
```










