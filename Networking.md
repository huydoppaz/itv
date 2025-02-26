### OSI Model
The OSI (Open Systems Interconnection) model is a conceptual framework used to describe the functions of a networking system. It divides network communications into seven layers, each with a specific role. Here's a brief overview of each layer:
1. **Physical Layer (Layer 1)**: Làm việc với cơ sở vật lý như cáp mạng, kết nối, và tín hiệu điện. Nó đảm bảo rằng dữ liệu được truyền tải dưới dạng bit một cách chính xác và hiệu quả. Ví dụ về giao thức ở lớp này bao gồm Ethernet, Wi-Fi, và các chuẩn khác liên quan đến truyền dẫn tín hiệu.
    
2. **Data Link Layer (Layer 2)**: Làm việc với việc truyền dữ liệu giữa các nút trong mạng cục bộ. Nó đảm bảo rằng dữ liệu được truyền tải một cách chính xác từ một nút này sang nút khác trong cùng một mạng. Ví dụ về giao thức ở lớp này bao gồm Ethernet, PPP (Point-to-Point Protocol), và các chuẩn khác liên quan đến truyền dẫn dữ liệu trong mạng cục bộ.
3. **Network Layer (Layer 3)**: Xử lý việc định tuyến dữ liệu giữa các mạng khác nhau. Nó đảm bảo rằng dữ liệu được truyền tải một cách hiệu quả từ nguồn đến đích qua nhiều mạng khác nhau. Ví dụ về giao thức ở lớp này bao gồm IP (Internet Protocol), ICMP (Internet Control Message Protocol), và các chuẩn khác liên quan đến định tuyến và địa chỉ hóa mạng.

4. **Transport Layer (Layer 4)**: Xử lý việc truyền tải dữ liệu giữa các ứng dụng trên các máy chủ khác nhau. Nó đảm bảo rằng dữ liệu được truyền tải một cách đáng tin cậy và chính xác. Ví dụ về giao thức ở lớp này bao gồm TCP (Transmission Control Protocol) và UDP (User Datagram Protocol).

5. **Session Layer (Layer 5)**: Quản lý các phiên làm việc giữa các ứng dụng. Nó khởi tạo, duy trì và kết thúc các phiên làm việc. Ví dụ về giao thức ở lớp này bao gồm NetBIOS và RPC (Remote Procedure Call).

6. **Presentation Layer (Layer 6)**: Xử lý định dạng dữ liệu, mã hóa và giải mã hóa. Nó đảm bảo rằng dữ liệu được trình bày dưới dạng có thể hiểu được bởi lớp ứng dụng. Ví dụ về giao thức ở lớp này bao gồm JPEG cho hình ảnh và SSL/TLS cho các giao tiếp an toàn.

7. **Application Layer (Layer 7)**: Lớp ứng dụng cuối cùng, nơi mà các ứng dụng cuối cùng tương tác với người dùng. Nó cung cấp các dịch vụ trực tiếp cho người dùng cuối, chẳng hạn như email, web, và các ứng dụng truyền thông khác. Ví dụ về giao thức ở lớp này bao gồm HTTP, FTP, SMTP, và DNS.

**Example**:  
```
import socket
import struct
# Create a raw socket
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
# Receive a packet     
packet = s.recvfrom(65565)
# Parse the Ethernet header
eth_length = 14
eth_header = packet[0][:eth_length]
eth = struct.unpack('!6s6sH', eth_header)
eth_protocol = socket.ntohs(eth[2])
# Print the source and destination MAC addresses
print('Source MAC: ', eth[0].hex(':'))
print('Destination MAC: ', eth[1].hex(':'))
# Check if the protocol is IPv4
if eth_protocol == 8:
    # Parse the IP header
    ip_header = packet[0][eth_length:20+eth_length]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    ip_length = ihl * 4
    ip_ttl = iph[5]
    ip_protocol = iph[6]
    ip_checksum = iph[7]
    ip_src = socket.inet_ntoa(iph[8])
    ip_dst = socket.inet_ntoa(iph[9])
    # Print the source and destination IP addresses
    print('Source IP: ', ip_src)
    print('Destination IP: ', ip_dst)
    # Check if the protocol is TCP
    if ip_protocol == 6:
        # Parse the TCP header
        tcp_header = packet[0][eth_length+ip_length:eth_length+ip_length+20]
        tcph = struct.unpack('!HHLLBBHHH', tcp_header)
        tcp_src_port = tcph[0]
        tcp_dst_port = tcph[1]
        tcp_seq = tcph[2]
        tcp_ack_seq = tcph[3]
        tcp_doff_reserved = tcph[4]
        tcp_doff = tcp_doff_reserved >> 4
        tcp_flags = tcph[5]
        tcp_window = tcph[6]
        tcp_checksum = tcph[7]
        tcp_urg_ptr = tcph[8]
        # Print the source and destination ports
        print('Source Port: ', tcp_src_port)
        print('Destination Port: ', tcp_dst_port)
    # Check if the protocol is UDP
    elif ip_protocol == 17:
        # Parse the UDP header
        udp_header = packet[0][eth_length+ip_length:eth_length+ip_length+8]
        udph = struct.unpack('!HHHH', udp_header)
        udp_src_port = udph[0]
        udp_dst_port = udph[1]
        udp_length = udph[2]
        udp_checksum = udph[3]
        # Print the source and destination ports
        print('Source Port: ', udp_src_port)
        print('Destination Port: ', udp_dst_port)
    # Check if the protocol is ICMP
    elif ip_protocol == 1:
        # Parse the ICMP header
        icmp_header = packet[0][eth_length+ip_length:eth_length+ip_length+8]
        icmph = struct.unpack('!BBH', icmp_header)
        icmp_type = icmph[0]
        icmp_code = icmph[1]
        icmp_checksum = icmph[2]
        # Print the ICMP type and code
        print('ICMP Type: ', icmp_type)
        print('ICMP Code: ', icmp_code)
```

### Differences between TCP and UDP

- **Connection-Oriented vs. Connectionless**: TCP là kết nối có hướng (định hướng kết nối) và UDP là kết nối không định hướng (connectionless). TCP thiết lập kết nối trước khi gửi dữ liệu, trong khi UDP gửi dữ liệu mà không cần thiết lập kết nối trước.
- **Reliability**: TCP cung cấp giao tiếp đáng tin cậy với kiểm tra lỗi và xác nhận gói tin. UDP không cung cấp kiểm tra lỗi hoặc xác nhận gói tin.
- **Flow Control**: TCP bao gồm cơ chế kiểm soát lưu lượng để ngăn chặn người gửi làm quá tải người nhận. UDP không có kiểm soát lưu lượng.
- **Ordering**: TCP đảm bảo rằng các gói tin đến người nhận theo đúng thứ tự mà chúng được gửi. UDP không đảm bảo thứ tự gói tin.

- **Header Size**: TCP có kích thước tiêu đề lớn hơn so với UDP, do nó chứa nhiều thông tin hơn như số thứ tự, số nhận diện, cờ kiểm soát, v.v. UDP có kích thước tiêu đề nhỏ hơn và chỉ chứa thông tin cần thiết như cổng nguồn, cổng đích, độ dài, và checksum.

- **Use Cases**: TCP sử dụng trong các ứng dụng yêu cầu sự tin cậy và độ chính xác cao, như truyền tải dữ liệu quan trọng, truy cập web, email, và các ứng dụng truyền tải dữ liệu lớn. UDP được sử dụng trong các ứng dụng yêu cầu tốc độ truyền tải cao hơn độ tin cậy, như trò chơi trực tuyến, phát trực tiếp video, và các ứng dụng thời gian thực khác.

**Example** :
- Các giao thức sử dụng TCP : HTTP, HTTPS, FTP, SMTP, Telnet, SSH, và nhiều giao thức khác.
- Các giao thức sử dụng UDP : DNS, DHCP, ... 


![Comparison of TCP and UDP](https://www.profiber.eu/files/aplikacie/obrazky/TCPvsUDP/obr1.png)


### Firewall

**Summary**:
Firewall là một hệ thống bảo mật mạng được sử dụng để kiểm soát lưu lượng mạng vào và ra khỏi mạng nội bộ. Nó hoạt động như một bộ lọc, chỉ cho phép lưu lượng mạng phù hợp đi qua và chặn các lưu lượng không mong muốn hoặc có thể gây hại. Firewalls có thể được triển khai phần cứng, phần mềm hoặc cả hai.



**Cách Stateless Firewall làm việc** : Stateless Firewall chỉ kiểm tra các gói tin dựa trên các tiêu chí như địa chỉ IP nguồn, địa chỉ IP đích, cổng nguồn và cổng đích. Nếu gói tin phù hợp với các tiêu chí này, nó sẽ được phép đi qua tường lửa. Ngược lại, nó sẽ bị chặn. Stateless Firewall không lưu trữ thông tin về các kết nối mạng trước đó, do đó nó không thể xác định xem gói tin đến có phải là một phần của một kết nối mạng hợp lệ hay không. Điều này có thể dẫn đến việc gói tin độc hại có thể đi qua tường lửa mà không bị phát hiện.


**Cách Stateful Firewall hoạt động:**
Stateful Firewall theo dõi trạng thái của các kết nối mạng và chỉ cho phép lưu lượng qua tường lửa nếu nó thuộc về một kết nối hiện có hoặc được khởi tạo từ bên trong mạng nội bộ. Điều này giúp ngăn chặn các cuộc tấn công từ bên ngoài và đảm bảo rằng chỉ lưu lượng mạng hợp lệ mới được phép đi qua tường lửa.


- Config iptables theo dạng stateless:

```
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

- Config iptables theo dạng stateful:

```
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -m state --state NEW -j ACCEPT
```

### DNS 

- Dns : Domain Name System, dịch tên miền thành địa chỉ IP
- Protocol: UDP, TCP (UDP phổ biến hơn)
- Port hoạt động : 53

Quá trình *DNS lookup* : 
1. Client gửi request DNS đến DNS server gần nhất (DNS resolver) (DNS resolver thường là DNS server của ISP của client hoặc DNS server được cấu hình trong file cấu hình mạng của client.)

2. DNS server tìm kiếm thông tin trong cache của nó. Nếu tìm thấy, nó sẽ trả về thông tin cho client. Nếu không, nó sẽ tiếp tục tìm kiếm thông tin từ các DNS server khác.

3. Nếu DNS server không tìm thấy thông tin trong cache, nó sẽ gửi request DNS đến các DNS server khác, bắt đầu từ root DNS server. Root DNS server sẽ chỉ cho DNS server biết nơi có thể tìm thấy thông tin về tên miền mà client đang tìm kiếm.

4. DNS server tiếp tục tìm kiếm thông tin từ các DNS server khác, như TLD DNS server (ví dụ: .com, .org, .net) và authoritative DNS server (DNS server quản lý thông tin về tên miền cụ thể).

5. Khi tìm thấy thông tin, DNS server sẽ lưu thông tin vào cache của nó và trả về thông tin cho client.

6. Client nhận được thông tin IP address từ DNS server và sử dụng thông tin này để thiết lập kết nối với server chứa trang web mà client đang tìm kiếm.

file config DNS server nằm tại : /etc/bind/named.conf.local

ví dụ về cấu hình DNS server:

```
zone "example.com" {
    type master;
    file "/etc/bind/db.example.com"; // file chứa thông tin về tên miền

};

```

Trong file cấu hình trên, "example.com" là tên miền mà DNS server sẽ quản lý, "type master" chỉ ra rằng DNS server này là máy chủ chính (master) cho tên miền này, và "file" chỉ ra đường dẫn tới file chứa thông tin về tên miền.
File cấu hình DNS server có thể được chỉnh sửa bằng bất kỳ trình soạn thảo văn bản nào như nano, vim, v.v. Sau khi chỉnh sửa, DNS server cần được khởi động lại để áp dụng các thay đổi. 
Ví dụ về nội dung file "/etc/bind/db.example.com":

```
;
; BIND data file for example.com
;
$TTL    604800
@       IN      SOA     ns1.example.com. admin.example.com. (
                              2         ; Serial  
                         604800         ; Refresh
                          86400         ; Retry 
                        2419200         ; Expire 
                         604800 )       ; Negative Cache TTL 
;
@       IN      NS      ns1.example.com.
@       IN      A       192.168.1.1
ns1     IN      A       192.168.1.1
www     IN      A       192.168.1.2
mail    IN      A       192.168.1.3
ftp     IN      A       192.168.1.4
CNAME   IN      CNAME   www.example.com. example.com.

```

*Start Of Authority*: SOA (Start of Authority) là một bản ghi DNS đặc biệt chứa thông tin về tên miền, bao gồm tên máy chủ DNS chính, email của quản trị viên, thời gian cập nhật, và các thông số khác liên quan đến tên miền. SOA bản ghi được sử dụng bởi các DNS server để xác định quyền quản lý của họ đối với tên miền cụ thể.


*A* : Bản ghi IPV4
*AAAA* : Bản ghi IPV6
*CNAME* : Bản ghi tên miền con trỏ đến tên miền khác 
*MX* : Bản ghi Mail Exchange chỉ ra máy chủ email chính và phụ của tên miền
*NS* : Bản ghi Name Server chỉ ra máy chủ DNS chịu trách nhiệm cho tên miền
*PTR* : Bản ghi con trỏ ngược từ địa chỉ IP về tên miền (được sử dụng trong hệ thống DNS ngược)
*TXT* : Bản ghi văn bản chứa thông tin bổ sung về tên miền, thường được sử dụng cho các dịch vụ xác thực như SPF, DKIM, và DMARC.

[Hình minh họa các loại bản ghi DNS](https://www.cloudns.net/blog/wp-content/uploads/2024/05/cloudns-dns-server-types.png)


### ARP 
Address Resolution Protocol (ARP) là một giao thức mạng cấp liên kết dữ liệu được sử dụng để tìm địa chỉ vật lý (MAC address) của một thiết bị trên mạng từ địa chỉ IP của nó. ARP hoạt động trong môi trường mạng LAN (Local Area Network).

**ARP Spoofing** là một kỹ thuật tấn công mạng mà trong đó kẻ tấn công giả mạo địa chỉ MAC của một thiết bị khác trên mạng để đánh cắp thông tin hoặc gây rối loạn hoạt động mạng.

**ARP Spoofing example:** 
Giả sử bạn đang kết nối đến mạng công ty và bạn muốn truy cập vào một máy chủ nội bộ. Kẻ tấn công có thể thực hiện ARP spoofing để giả mạo địa chỉ MAC của máy chủ đó. Khi bạn gửi yêu cầu đến máy chủ, yêu cầu đó sẽ được gửi đến kẻ tấn công thay vì máy chủ thực sự. Kẻ tấn công có thể xem, chỉnh sửa hoặc chặn thông tin mà bạn gửi đến máy chủ.


### DHCP :

**DHCP (Dynamic Host Configuration Protocol)** là một giao thức mạng cho phép các thiết bị mạng tự động nhận được các thông tin cấu hình cần thiết như địa chỉ IP, địa chỉ máy chủ DNS, và cổng mặc định. Điều này giúp giảm bớt công việc quản lý cấu hình mạng thủ công và giảm thiểu lỗi do cấu hình sai lệch. DHCP hoạt động dựa trên mô hình client-server, trong đó máy chủ DHCP phân phối các thông tin cấu hình cho các máy khách (clients).
**Cách DHCP hoạt động:**
1. **Discover:** Máy khách gửi một gói tin DHCP Discover đến mạng để tìm máy chủ DHCP. Máy chủ DHCP nhận được gói tin này sẽ trả lời bằng một gói tin DHCP Offer.
2. **Offer:** Máy chủ DHCP gửi một gói tin DHCP Offer đến máy khách chứa thông tin về địa chỉ IP được đề xuất, thời gian thuê bao, và thông tin về máy chủ DNS.
3. **Request:** Máy khách gửi một gói tin DHCP Request đến mạng để yêu cầu địa chỉ IP được đề xuất từ máy chủ DHCP. Máy chủ DHCP nhận được gói tin này sẽ xác nhận rằng địa chỉ IP đã được cấp cho máy khách.
4. **Acknowledge:** Máy chủ DHCP gửi một gói tin DHCP Acknowledge đến máy khách xác nhận rằng địa chỉ IP đã được cấp cho máy khách. Máy khách sẽ sử dụng địa chỉ IP này cho đến khi thời gian thuê bao hết hạn.

Đây là quá trình cấp phát địa chỉ IP tự động thông qua DHCP. Quá trình này giúp giảm tải công việc quản lý địa chỉ IP cho người quản trị mạng và đảm bảo rằng mỗi máy tính trên mạng đều có một địa chỉ IP duy nhất.

**Lưu ý:** Trong một số trường hợp, máy khách có thể yêu cầu một địa chỉ IP cụ thể mà nó đã sử dụng trước đó. Trong trường hợp này, máy chủ DHCP sẽ kiểm tra xem địa chỉ IP đó có sẵn hay không và cấp phát cho máy khách nếu có thể. Nếu địa chỉ IP đó đã được cấp cho một máy khách khác, máy chủ DHCP sẽ cấp phát một địa chỉ IP khác cho máy khách yêu cầu.




































































