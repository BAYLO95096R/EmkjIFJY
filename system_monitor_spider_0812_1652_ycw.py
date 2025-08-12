# 代码生成时间: 2025-08-12 16:52:07
import scrapy
def get_system_stats():
    # 该函数用于获取系统性能统计信息
    try:
        # 导入psutil模块来获取系统信息
        import psutil
        
        # 获取CPU使用率
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # 获取内存使用信息
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        
        # 获取磁盘使用信息
        disk_usage = psutil.disk_usage('/')
        disk_usage_percent = disk_usage.percent
        
        # 获取网络使用信息
        net_io = psutil.net_io_counters()
        net_sent = net_io.bytes_sent
        net_recv = net_io.bytes_recv
        
        # 将系统统计信息返回
        return {
            'cpu_usage': cpu_usage,
            'memory_usage': memory_usage,
            'disk_usage': disk_usage_percent,
            'net_sent': net_sent,
            'net_recv': net_recv
        }
    except Exception as e:
        # 错误处理
        print(f"Error getting system stats: {e}")


class SystemMonitorSpider(scrapy.Spider):
    name = 'system_monitor'
    allowed_domains = []
    start_urls = []
    
    def start_requests(self):
        # 启动请求，这里我们使用无限循环来模拟持续监控
        while True:
            try:
                # 调用get_system_stats函数获取系统性能数据
                stats = get_system_stats()
                
                # 打印系统性能数据
                self.log(f"CPU Usage: {stats['cpu_usage']}%")
                self.log(f"Memory Usage: {stats['memory_usage']}%")
                self.log(f"Disk Usage: {stats['disk_usage']}%")
                self.log(f"Network Sent: {stats['net_sent']} bytes")
                self.log(f"Network Received: {stats['net_recv']} bytes")
                
                # 休眠一段时间后再次检查
                scrapy.sleep(10)
            except Exception as e:
                # 异常处理
                self.log(f"Error monitoring system: {e}")
                scrapy.sleep(10)
